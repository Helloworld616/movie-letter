<template>
  <div>
    <div class="row g-4 mt-3 mb-3">
      <Letter
        v-for="(movie, idx) in movies.reverse()" 
        :key="idx"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import Letter from '@/components/Letter'
import axios from 'axios'

export default {
  name: 'Letters',
  components: {
    Letter,
  },
  data: function () {
    return {
      movies: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      console.log(config)
      return config
    },
    getMovies: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/recommended/`,
        headers: this.setToken(),
      })
        .then(res => {
          console.log(res.data)
          this.movies = res.data
        })
    },
  },
  created: function () {
    this.getMovies()
  },
}
</script>