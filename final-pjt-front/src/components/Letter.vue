<template>
  <div class="col-6 col-sm-6 col-md-4 col-lg-3">
    <div id='form_wrap'>
      <figure @click="getGenres(), getInfo(movie), getMovieId(movie)" data-bs-toggle="modal" data-bs-target="#exampleModal">
        <div class="gallery-img">
          <img :src="posterUrl" class="form" alt="포스터">
        </div>
        <figcaption>
          <p>{{ movie.movie_title }}</p>
        </figcaption>  
      </figure>
    </div>

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="movieModal contentModal" aria-hidden="true">
      <div class="modal-dialog modal-dialog-scrollable d-flex justify-content-cneter">

        <!-- 영화 모달 -->
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="movieModal"></h5>
            <!-- <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button> -->
          </div>
          <div class="modal-body">
            <div class="index d-flex justify-content-center clearfix">
              <img class="movie-poster" src="">
              <div class="simple-info">
                <span class="info-settings">장르</span>
                <div class="movie-genres"></div>
                <br>
                <span class="info-settings">개봉일</span>
                <div class="movie-release-date"></div>
                <br>
                <span class="info-settings">평점</span>
                <div class="movie-vote-average"></div>
              </div>
            </div>
            <br>
            <div class="movie-overview"></div>
          </div>
        </div>

        
        <!-- 로그인 할 경우의 리뷰 모달 -->
        <div class="modal-content" v-if="isLogin">
          <div class="modal-header">
            <h5 class="modal-title" id="contentModal"> </h5>
          </div>
          <div class="modal-body">
            <div class="letter-title"></div>
            <br>
            <div class="letter-content"></div>
            <br>
            <div class="letter-rank"></div>
          </div>
           <div class="modal-footer">
            <button type="button" class="btn btn-link text-decoration-none" style="color:black" data-bs-dismiss="modal">잘 봤어용 ^^</button>
          </div>
        </div>
        
      </div>
    </div>

  </div>  
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: 'Letter',
  props: {
    movie: {
      type: Object
    }
  },
  data: function () {
    return {
      genres: [],
      selectedGenres: [],
      review: {
        user: null,
        movie: null,
        title: null,
        content: null,
        rank: null,
      },
    }
  },
  methods: {
    ...mapActions([
      'getMovieId',
    ]),
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      console.log(config)
      return config
    },
    getInfo: function (movie) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movie.movie_id}/`,
      })
        .then((res) => {
          console.log(res)
          console.log(movie)
          document.querySelector('.modal-title').innerText = res.data.title
          document.querySelector('.movie-poster').setAttribute('src', `https://image.tmdb.org/t/p/w500/${res.data.poster_path}`) 
          res.data.genres.forEach(genre_id => {
            this.genres.forEach(genre => {
              if (genre_id === genre.id) {
                this.selectedGenres.push(genre.name)
              }
            })
          })
          document.querySelector('.movie-genres').innerText = this.selectedGenres.join(', ')
          this.selectedGenres = []
          document.querySelector('.movie-release-date').innerText = res.data.release_date.split('-').join('. ')
          document.querySelector('.movie-vote-average').innerText = res.data.vote_average
          document.querySelector('.movie-overview').innerText = res.data.overview
          document.querySelector('.letter-title').innerText = movie.review_title
          document.querySelector('.letter-rank').innerText = `평점 : ${movie.review_rank}`
          document.querySelector('.letter-content').innerText = movie.review_content
        })
        .catch(err => {
          console.log(err)
        })
    },

    getGenres: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/genres/',
      })
        .then((res) => {
          this.genres = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    submit: function (movieId, review) {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${movieId}/reviews/`,
        headers: this.setToken(),
        data: review,
      })
        .then((res) => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  computed: {
    ...mapGetters([
      'isLogin',
      'config',
      'movieId',
    ]),
    posterUrl: function () {
      const posterId = this.movie.poster_path
      return `https://image.tmdb.org/t/p/w500/${posterId}`
    },
  },
}
</script>

<style scoped>
  @font-face {
    font-family: 'Cafe24Oneprettynight';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.1/Cafe24Oneprettynight.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }

  @font-face {
    font-family: 'Hanyoon';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/naverfont_05@1.0/Hanyoon.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }

  /* 편지 봉투 */
  #form_wrap { 
		overflow:hidden;  
		position:relative; 
		width: 250px;
		height: 190px;
		top: 0px;
		-webkit-transition: all 1s ease-in-out .3s;
		-moz-transition: all 1s ease-in-out .3s;
		-o-transition: all 1s ease-in-out .3s;
		transition: all 1s ease-in-out .3s;
    margin-bottom: 50px;
  }

	#form_wrap:before {
    content:"";
		position:absolute;
		bottom:10px;
    left:0px;
		background:url('../assets/before.png');
    background-repeat: no-repeat;
		width: 250px;
		height: 180px;
	}

  #form_wrap:after {
    content:"";
    position:absolute;
    bottom:0;
    left:0;
		background:url('../assets/after.png');
    background-repeat: no-repeat;
		width: 250px;
		height: 120px; 
	}

  #form_wrap.hide:after, #form_wrap.hide:before {
    display:none; 
  }

	#form_wrap:hover {
    height:260px;
    top: -60px;
  }

  .form {
		position:relative;
    overflow:hidden;
    width:180px;
    margin:0px;
    border-radius: 25px;
  }

  /* 이미지 호버 */
  figure {
    transition: opacity 0.2s; 
    position: relative;
    margin: 0; 
    display:flex;
    justify-content: center;
    cursor: pointer;
  }

  figure figcaption {
    font-family: 'Cafe24Oneprettynight';
    font-size: 20px;
    color: #fff;
    bottom: 70px; 
    opacity: 0;
    position: absolute; 
    text-align: center; 
    width: 170px;
    transition: all .3s ease;
    bottom: 130px;
    word-break: keep-all;
  }

  figure .gallery-img {
    opacity: 2;
    transition: all 0.3s ease 0s;
    overflow: hidden;
    width: 180px;
    margin: 0;
    border-radius: 25px;
  }

  figure:hover .gallery-img {
    background-color: rgb(31, 31, 31);
  }

  figure:hover img {
    transition: all .3s ease;
    opacity: 0.2;
  }

  figure:hover figcaption {
    opacity: 1;
    transition: all .3s ease; 
  }

  /* 모달창 */
  .modal-dialog {
    max-width: 1200px;
    margin: 1.75rem auto;
  }

  .modal-content {
    margin-left: 20px;
    background-color: #FCF5F5;
  }

  .modal-title {
    font-family: 'Cafe24Oneprettynight';
    font-size: 26px;
    font-weight: bold;
  }

  .modal-body {
    margin: auto;
    font-family: 'Cafe24Oneprettynight';
  }

  .modal-footer {
    font-family: 'Cafe24Oneprettynight';
  }
  .ui-widget-content {border:none}

  .movie-poster {
    margin: auto;
    width: 250px;
  }

  textarea {
    width: 450px;
    height: 350px;
  }

  .review-title {
    width: 450px;
    height: 30px;
  }

  .rank {
    width: 60px;
    height: 30px;
    text-align-last: center;
    text-align: center;
    -ms-text-align-last: center;
    -moz-text-align-last: center;
  }

  .simple-info {
    font-family: 'Cafe24Oneprettynight';
    margin: auto;
    text-align: left;
    width: 200px;
    font-size: 20px;
  }

  .info-settings {
    font-family: 'Cafe24Oneprettynight';
    margin: auto;
    text-align: left;
    width: 200px;
    font-size: 24px;
    font-weight: bold;
  }

  .letter-title {
    font-family: 'Hanyoon';
    font-size: 50px;
    text-align: left;
    /* margin-right: 300px; */
  }

  .letter-content {
    font-family: 'Hanyoon';
    font-size: 35px;
    text-align: left;
    /* margin-right: 300px; */
  }

  .letter-rank {
    font-family: 'Hanyoon';
    font-size: 30px;
    text-align: left;
    /* margin-right: 300px; */
  }

  .modal-header {
    display: flex;
    flex-shrink: 0;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 1rem;
    border-bottom: 0px solid #dee2e6;
    border-top-left-radius: calc(.3rem - 1px);
    border-top-right-radius: calc(.3rem - 1px);
}

.movie-overview {
  font-size: 18px;
}

.modal-footer {
  border-top: 0px;
}
</style>