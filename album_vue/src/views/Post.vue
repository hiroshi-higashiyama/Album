<template>
  <div class="columns">
    <div class="column is-three-fifths is-offset-one-fifth">
      <div class="box">
        <figure class="image mb-4">
          <img v-bind:src="post.get_image" />
        </figure>
        <div>
          <p class="title is-4"><strong>Title&nbsp;: &nbsp;{{ post.title }}</strong></p>
          <p>Created date&nbsp;: &nbsp;&nbsp;{{ post.created_at }}</p>
          <p v-if="post.description">Description&nbsp;: &nbsp;{{ post.description }}</p>
        </div>

        <div class="buttons mt-5">
          <router-link
            :to="{ name: 'EditPost', params: { id: post.id } }"
            class="button is-success"
            ><strong><i class="fas fa-edit"></i>&nbsp;&nbsp;Edit</strong></router-link
          >
          <button class="button is-danger" @click="submitDelete"><i class="fas fa-trash-alt"></i>&nbsp;&nbsp;delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "Post",
  data() {
    return {
      post: {},
    };
  },
  mounted() {
    this.getPost();
  },
  methods: {
    async getPost() {
      // this.$store.commit("setIsLoading", true);

      const postID = this.$route.params.id;

      await axios
        .get(`/api/v1/posts/${postID}/`)
        .then((response) => {
          this.post = response.data;

          document.title = this.post.title + " | Detail";
        })
        .catch((error) => {
          console.log(error);
        });

      // this.$store.commit("setIsLoading", false);
    },
    async submitDelete() {
      this.$store.commit("setIsLoading", true);

      const postID = this.$route.params.id;

      await axios
        .delete(`/api/v1/posts/${postID}/`)
        .then((response) => {
          toast({
            message: "Deleted.",
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
