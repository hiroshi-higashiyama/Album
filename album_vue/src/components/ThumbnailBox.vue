<template>
  <div class="column is-3">
    <div class="box">
      <figure class="image is-3by2 mb-4">
        <router-link :to="{ name: 'Post', params: { id: thumbnail.id } }">
        <img v-bind:src="thumbnail.get_thumbnail" />
        </router-link>
      </figure>

      <h3 class="is-size-4 has-text-centered">{{ thumbnail.title }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductBox",
  props: {
    thumbnail: Object,
  },
};
</script>

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>
