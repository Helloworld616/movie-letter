<template>
  <div>
    <Banner/>
    <MovieList/>
  </div>
</template>

<script>
import Banner from '@/components/Banner.vue'
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'Home',
  components: {
    Banner,
    MovieList
  }
}
</script>

<style>

</style>