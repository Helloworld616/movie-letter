<template>
  <div>
    <div class="row g-4 mt-3 mb-3">
      <MovieListItem
        v-for="(movie, idx) in movies"
        :key="idx"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'
import axios from 'axios'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  data: function () {
    return {
      URL: 'http://127.0.0.1:8000/movies/list/',
      movieLength: 0,
      pageNum: 1,
      movies: [],
      isNotEnd: true, 
    }
  },
  methods: {
    getMovieLength: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/all/',
      })
        .then((res) => {
          this.movieLength = res.data.length
        })
    },
    getMovies: function () {
      axios({
        method: 'get',
        url: `${this.URL}?page=${this.pageNum}`,
        headers: {'X-Requested-With': 'XMLHttpRequest'},
      })
        .then(res => {
          res.data.forEach(movie => {
            this.movies.push(movie)
          })
          this.pageNum += 1
        })
    },
    infinityScroll: function () {
      if (this.isNotEnd) {
        const {scrollTop, clientHeight, scrollHeight} = document.documentElement
        if (scrollHeight - scrollTop === clientHeight) {
          this.getMovies()
        }
        if (12 * (this.pageNum - 1) > this.movieLength) {
          this.isNotEnd = false
          document.removeEventListener('scroll', this.infinityScroll);
        }
      }
    }
  },
  created: function () {
    this.getMovies()
    this.getMovieLength()
    document.addEventListener('scroll', this.infinityScroll);
  },
}
</script>
