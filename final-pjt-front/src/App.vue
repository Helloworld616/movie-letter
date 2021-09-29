<template>
  <div id="app">
    <div id="nav">
      <nav class="navbar navbar-expand-lg navbar-light ms-4">
        <div class="container-fluid">
          <router-link :to="{ name: 'Home' }" class="navbar-brand ms-3" aria-current="page">
            무비레터
          </router-link>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-center" id="navbarNav">
            <ul v-if="isLogin" class="navbar-nav me-4">
              <li class="nav-item">
                <router-link :to="{ name: 'Letters' }" class="nav-link active" aria-current="page">
                  편지함
                </router-link>
              </li>
              <li class="nav-item">
                <router-link @click.native="logout()" to="#" class="nav-link active" aria-current="page">
                  로그아웃
                </router-link>
              </li>
              <li class="nav-item">
                <router-link @click.native="setToken(), userDelete(config)" to="#" class="nav-link active" aria-current="page">
                  회원탈퇴
                </router-link>
              </li>
            </ul>
            <ul v-else class="navbar-nav me-4">
              <li class="nav-item">
                <router-link :to="{ name: 'Signup' }" class="nav-link active" aria-current="page">
                  회원가입
                </router-link>
              </li>
              <li class="nav-item">
                <router-link :to="{ name: 'Login' }" class="nav-link active" aria-current="page">
                  로그인
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
    <div class="container">
      <router-view/>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'App',
  methods: {
    ...mapActions([
      'logout',
      'setToken',
      'userDelete',
    ]),
  },
  computed: {
    ...mapGetters([
      'isLogin',
      'config'
    ])
  },
  created: function () {
    this.$store.dispatch('checkToken')
  },
}
</script>

<style scoped>
@font-face {
  font-family: 'Hanyoon';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/naverfont_05@1.0/Hanyoon.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

.navbar-brand {
  font-family: 'Hanyoon';
  font-size: 50px;
}
 
.nav-item {
  font-family: 'Hanyoon';
  font-size: 25px;
}

#app {  
  text-align: center;
}

.navbar-collapse {
  flex-grow: 0;
}

.navbar-toggler:focus {
    box-shadow: 0 0 0 0rem;
}
</style>
