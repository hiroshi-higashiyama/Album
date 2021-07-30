<template>
  <div class="home">
    <div
      class="hero is-fullheight"
      :style="{ backgroundImage: 'url(' + require('@/assets/StockSnap_RTUVC7BMZI.jpg') + ')' }"
    >
      <div class="hero-body">
        <div class="container has-text-centered">
          <h1 class="home title mb-6">Photo Storage</h1>
          <h2 class="home subtitle">The best image</h2>
          <h2 v-if="$store.state.isAuthenticated">
            <router-link to="/posts" class="button is-text mt-5"
              >List</router-link
            >
          </h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  mounted() {
    document.title = "Photo Storage";
  },
};
</script>

<style lang="scss">
.hero {
  @extend .hero;
  background-size: cover;
  background-position: center;
}
.home {
  color: white;
}
</style>
