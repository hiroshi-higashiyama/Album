<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Edit Post</h1>
      </div>

      <div class="column is-12">
        <form @submit.prevent="submitForm" enctype="multipart/form-data">
          <div class="field">
            <label>Image</label>
            <div class="control">
              <input type="file" @change="getFile($event)" name="file" />
            </div>
          </div>

          <div class="field">
            <label>Title</label>
            <div class="control">
              <input type="text" class="input" v-model="edit.title" />
            </div>
          </div>

          <div class="field">
            <label>Description</label>
            <div class="control">
              <textarea class="textarea" v-model="edit.description"></textarea>
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
  name: "EditPost",
  data() {
    return {
      edit: {
        title: '',
        description: '',
        image: '',
      },
    };
  },
  mounted() {
    this.getPost();
  },
  methods: {
    async getPost() {
      this.$store.commit("setIsLoading", true);

      const postID = this.$route.params.id;

      await axios
        .get(`/api/v1/posts/${postID}/`)
        .then((response) => {
          this.edit = response.data;

          document.title = this.edit.title + " | Edit";
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
    getFile(event) {
      const file = event.target.files[0];
      this.edit.image = file;
    },
    async submitForm() {
      this.$store.commit("setIsLoading", true);

      const postID = this.$route.params.id;

      const formData = new FormData();
      formData.append("title", this.edit.title);
      formData.append("description", this.edit.description);
      formData.append("image", this.edit.image);
      formData.append("thumbnail", '');

      await axios
        .patch(`/api/v1/posts/${postID}/`, formData, {
          headers: {
            "content-type": "multipart/form-data",
          },
        })
        .then((response) => {
          toast({
            message: "編集しました。",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 3000,
            position: "bottom-right",
          });

          this.$router.push("/posts");
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
<style></style>
