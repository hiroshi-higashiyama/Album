<template>
  <div>
    <form @submit.prevent="getLatestThumbnails">
      <div class="field has-addons mb-5">
        <div class="control">
          <input type="text" class="input" placeholder="Search..." v-model="query" />
        </div>
        <div class="control">
          <button class="button is-success">
            <i class="fas fa-search"></i>
          </button>
        </div>
      </div>
    </form>
    <div class="columns is-multiline">
      <ThumbnailBox
        v-for="thumbnail in latestThumbnails"
        v-bind:key="thumbnail.id"
        v-bind:thumbnail="thumbnail"
      >
      </ThumbnailBox>
    </div>

    <!-- <div class="buttons">
      <button
        class="button is-light"
        @click="goToPreviousPage()"
        v-if="showPreviousButton"
      >
        Previous
      </button>
      <button
        class="button is-light"
        @click="goToNextPage()"
        v-if="showNextButton"
      >
        Next
      </button>
    </div> -->
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
      query: "",
      // showNextButton: false,
      // showPreviousButton: false,
      hasNext: true,
      currentPage: 1,
    };
  },
  components: {
    ThumbnailBox,
  },
  mounted() {
    this.getLatestThumbnails();

    window.onscroll = () => {
      let bottomOfWindow =
        document.documentElement.scrollTop + window.innerHeight ===
        document.documentElement.offsetHeight;

      if (bottomOfWindow && this.hasNext) {
        this.currentPage += 1;
        this.getLatestThumbnails();
      }
    };

    document.title = "Posts";
  },
  methods: {
    // goToNextPage() {
    //   this.currentPage += 1;
    //   this.getLatestThumbnails();
    // },
    // goToPreviousPage() {
    //   this.currentPage -= 1;
    //   this.getLatestThumbnails();
    // },
    async getLatestThumbnails() {
      this.$store.commit("setIsLoading", true);

      // this.showNextButton = false;
      // this.showPreviousButton = false;

      await axios
        .get(`/api/v1/posts/?page=${this.currentPage}&search=${this.query}`)
        .then((response) => {
          this.hasNext = false;

          if (response.data.next) {
            this.hasNext = true;
          }
          this.latestThumbnails = response.data.results;

          // if (response.data.next) {
          //   this.showNextButton = true;
          // }
          // if (response.data.previous) {
          //   this.showPreviousButton = true;
          // }
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
