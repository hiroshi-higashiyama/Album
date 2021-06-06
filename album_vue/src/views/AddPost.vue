<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add Post</h1>
      </div>

      <div class="column is-12">
        <form @submit.prevent="submitForm" enctype="multipart/form-data">
          <div class="field">
            <label>Image</label>
            <div class="control">
              <input type="file" @change="onImageUploaded" name="file" />
            </div>
          </div>

          <div class="field">
            <label>Title</label>
            <div class="control">
              <input type="text" class="input" v-model="title" />
            </div>
          </div>

          <div class="field">
            <label>Description</label>
            <div class="control">
              <textarea class="textarea" v-model="description"></textarea>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import { toast } from "bulma-toast";

export default {
  name: "AddPost",
  data() {
    return {
      submittedArticle: {
        title: "",
        description: "",
        image: null
      },
    };
  },
  methods: {
    onImageUploaded(e) {
      // event(=e)から画像データを取得する
      const image = e.target.files[0]
      this.createImage(image)
    },
    createImage(image) {
      const reader = new FileReader()
      // imageをreaderにDataURLとしてattachする
      reader.readAsDataURL(image)
      // readAdDataURLが完了したあと実行される処理
      reader.onload = () => {
        this.image = reader.result
      }
    },
    async submitForm() {
      this.$store.commit("setIsLoading", true);

      const post = {
        title: this.title,
        description: this.description,
        image: this.image,
      }

      await axios
        .post("/api/v1/posts/", post)
        .then((response) => {
          toast({
            message: "追加しました",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          });

          this.$router.push("/posts");
        })
        .catch((error) => {
          console.log(error)
        })

      this.$store.commit("setIsLoading", false);
    }
  }
}
</script>
<style>
</style>
