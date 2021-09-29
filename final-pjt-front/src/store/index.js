import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

Vue.use(Vuex)

const ROOT_URL = process.env.VUE_APP_DJANGO_ROOT_URL

export default new Vuex.Store({
  state: {
    isLogin: false, // 로그인 여부를 나타내는 flag 변수
    config: null, // 토큰 정보를 담는 변수
    movieId: null,
  },

  mutations: {
    // *** accounts ***

    // 회원 가입
    SIGNUP: function (state) {
      console.log(state)
      router.push({ name: 'Login' })
    },

    // 로그인
    LOGIN: function (state, token) {
      localStorage.setItem('jwt', token)
      state.isLogin = true
      router.push({ name: 'Home' })
    },

    // 로그아웃
    LOGOUT: function (state) {
      state.isLogin = false
      localStorage.removeItem('jwt')
      router.push({ name: 'Login' })
    },

    // 토큰 유무 체크
    CHECK_TOKEN: function (state) {
      const token = localStorage.getItem('jwt')
      if (token) {
        state.isLogin = true
      }
    },

    // 토큰 부여
    SET_TOKEN: function (state) {
      const token = localStorage.getItem('jwt')
      state.config = {
        Authorization: `JWT ${token}`
      }
      // console.log(state.config)
    },

    // 회원 탈퇴
    USER_DELETE: function (state) {
      state.isLogin = false
      localStorage.removeItem('jwt')
      router.push({ name: 'Signup' })
    },


    // *** movies ***
    GET_MOVIE_ID: function (state, id) {
      state.movieId = id
    },
  },

  actions: {
    // *** accounts ***

    // 회원 가입
    signup: function ({ commit }, credentials) {
      axios({
        method: 'post',
        url: `${ROOT_URL}/accounts/signup/`,
        data: credentials
      })
        .then(res => {
          console.log(res)
          commit('SIGNUP')
        })
        .catch(err => {
          console.log(err)
        })
    },

    // 로그인
    login: function ({ commit }, credentials) {
      axios({
        method: 'post',
        url: `${ROOT_URL}/accounts/api-token-auth/`,
        data: credentials
      })
        .then(res => {
          console.log(credentials)
          commit('LOGIN', res.data.token)
        })
        .catch(err => {
          console.log(err)
        })
    },

    // 로그아웃
    logout: function ({ commit }) {
      commit('LOGOUT')
    },

    // 토큰 유무 체크
    checkToken: function ({ commit }) {
      commit('CHECK_TOKEN')
    },

    // 토큰 부여
    setToken: function ({ commit }) {
      commit('SET_TOKEN')
    },

    // 회원 탈퇴
    userDelete: function ({ commit }, config) {
      axios({
        method: 'delete',
        url: `${ROOT_URL}/accounts/delete/`,
        headers: config
      })
        .then(res => {
          console.log(res)
          commit('USER_DELETE')
        })
        .catch(err => {
          console.log(err)
        })
    },


    // *** movies ***
    getMovieId: function ({ commit }, movie) {
      commit('GET_MOVIE_ID', movie.id)
    }
  },

  modules: {
  },

  getters: {
    isFirst: function (state) {
      return state.isFirst
    },
    isLogin: function (state) {
      return state.isLogin
    },
    config: function (state) {
      return state.config
    },
    movieId: function (state) {
      return state.movieId
    },
  }
})
