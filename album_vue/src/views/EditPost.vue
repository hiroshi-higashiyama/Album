<template>
  <div class="edit-page">
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li><router-link to="/posts">List</router-link></li>
        <li>
          <router-link :to="{ name: 'Post', params: { id: edit.id } }">
            Detail
          </router-link>
        </li>
        <li class="is-active">
          <router-link
            :to="{ name: 'EditPost', params: { id: edit.id } }"
            aria-current="true"
            >Edit</router-link
          >
        </li>
      </ul>
    </nav>

    <div class="columns">
      <div class="column is-three-fifths is-offset-one-fifth">
        <div class="column is-12">
          <h1 class="title">Edit Post</h1>
        </div>

        <div class="box">
          <figure class="image mb-5">
            <img v-bind:src="edit.get_image" />
          </figure>

          <div>
            <form @submit.prevent="submitForm" enctype="multipart/form-data">
              <div class="field">
                <label>Title:</label>
                <div class="control">
                  <input type="text" class="input" v-model="edit.title" />
                </div>
              </div>

              <div class="field mt-5">
                <label>Description:</label>
                <div class="control">
                  <textarea
                    class="textarea"
                    v-model="edit.description"
                  ></textarea>
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
        title: "",
        description: "",
        get_image: "",
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
    async submitForm() {
      this.$store.commit("setIsLoading", true);

      const postID = this.$route.params.id;

      const formData = new FormData();
      formData.append("title", this.edit.title);
      formData.append("description", this.edit.description);
      // formData.append("image", this.edit.image);
      // formData.append("thumbnail", '');

      await axios
        .patch(`/api/v1/posts/${postID}/`, formData, {
          headers: {
            "content-type": "multipart/form-data",
          },
        })
        .then((response) => {
          toast({
            message: "Edited.",
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
