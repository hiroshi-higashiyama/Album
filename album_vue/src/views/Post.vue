<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <figure class="image mb-6">
          <img v-bind:src="post.get_image" />
        </figure>

        <h1 class="title">{{ post.title }}</h1>
        <p>{{ post.created_at }}</p>
        <p>{{ post.description }}</p>
      </div>
    </div>

    <div class="buttons">
      <router-link
        :to="{ name: 'EditPost', params: { id: post.id } }"
        class="button is-success"
        ><strong>編集</strong></router-link
      >
      <button class="button is-danger" @click="submitDelete">削除</button>
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
      this.$store.commit("setIsLoading", true);

      const postID = this.$route.params.id;

      await axios
        .get(`/api/v1/posts/${postID}/`)
        .then((response) => {
          this.post = response.data;

          document.title = this.post.title + ' | Detail'
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
    async submitDelete() {
      this.$store.commit("setIsLoading", true);

      const postID = this.$route.params.id;

      await axios
        .delete(`/api/v1/posts/${postID}/`)
        .then((response) => {
          toast({
            message: "削除しました",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
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
