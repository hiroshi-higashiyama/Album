<template>
  <div class="add-page">
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li><router-link to="/posts">List</router-link></li>
        <li class="is-active">
          <router-link :to="{ name: 'AddPost' }" aria-current="true"
            >Add</router-link
          >
        </li>
      </ul>
    </nav>

    <div class="columns">
      <div class="column is-three-fifths is-offset-one-fifth">
        <div class="column is-12">
          <h1 class="title">Add Post</h1>
        </div>

        <div class="box">
          <form @submit.prevent="submitForm" enctype="multipart/form-data">
            <div class="field">
              <div>Image:</div>
              <label class="file-label">
                <div class="control">
                  <input
                    class="file-input"
                    type="file"
                    @change="getFile($event)"
                    name="file"
                  />

                  <span class="file-cta">
                    <span class="file-icon">
                      <i class="fas fa-file-upload"></i>
                    </span>
                    <span class="file-label">
                      Choose a file…
                    </span>
                  </span>
                </div>
              </label>

              <div class="mt-5" v-if="preview">
                <img :src="preview" />
              </div>
            </div>

            <div class="field mt-5">
              <label>Title:</label>
              <div class="control">
                <input type="text" class="input" v-model="title" />
              </div>
            </div>

            <div class="field mt-5">
              <label>Description:</label>
              <div class="control">
                <textarea class="textarea" v-model="description"></textarea>
              </div>
            </div>

            <div class="field mt-5">
              <div class="control">
                <button class="button is-success">Submit</button>
              </div>
            </div>
          </form>
        </div>
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
      title: "",
      description: "",
      image: null,
      preview: "",
    };
  },
  mounted() {
    document.title = "Add Post";
  },
  methods: {
    getFile(event) {
      const file = event.target.files[0];
      this.image = file;
      if (this.image && this.image.type.match(/^image\/(png|jpeg)$/)) {
        this.preview = URL.createObjectURL(this.image);
      }
    },
    async submitForm() {
      this.$store.commit("setIsLoading", true);

      const formData = new FormData();
      formData.append("title", this.title);
      formData.append("description", this.description);
      formData.append("image", this.image);

      await axios
        .post("/api/v1/posts/", formData, {
          headers: {
            "content-type": "multipart/form-data",
          },
        })
        .then((response) => {
          toast({
            message: "Posted.",
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
