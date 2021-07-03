<template>
  <div class="home">
    <div class="hero is-fullheight" style="background-image: url('StockSnap_RTUVC7BMZI.jpg')">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h1 class="home title mb-6">Welcome to Title</h1>
          <h2 class="home subtitle">The best image</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
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
