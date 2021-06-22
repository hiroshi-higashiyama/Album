<template>
  <div class="columns is-multiline">
    <ThumbnailBox
      v-for="thumbnail in latestThumbnails"
      v-bind:key="thumbnail.id"
      v-bind:thumbnail="thumbnail"
    >
    </ThumbnailBox>
  </div>
</template>

<script>
import axios from "axios";

import ThumbnailBox from "@/components/ThumbnailBox";

export default {
  name: "Posts",
  data() {
    return {
      latestThumbnails: [],
    };
  },
  components: {
    ThumbnailBox,
  },
  mounted() {
    this.getLatestThumbnails();

    document.title = "Posts";
  },
  methods: {
    async getLatestThumbnails() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("/api/v1/posts/")
        .then((response) => {
          this.latestThumbnails = response.data;
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
