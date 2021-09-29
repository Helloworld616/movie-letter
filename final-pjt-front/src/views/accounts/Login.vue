<template>
  <div>
    <h1 class="main_login">로그인</h1>
    <br>
    <div>
      <!-- <label for="username">아이디: </label> -->
      <input type="text" id="username" v-model="credentials.username" placeholder="아이디">
    </div>
    <div>
      <!-- <label for="password">비밀번호: </label> -->
      <input type="password" id="password" v-model="credentials.password" placeholder="비밀번호">
    </div>
    <button class="login_btn" @click="login(credentials)">로그인</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    ...mapActions([
      'login'
    ]),
  }

}
</script>

<style scoped>
@font-face {
  font-family: 'Hanyoon';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/naverfont_05@1.0/Hanyoon.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

.main_login {
  font-family: 'Hanyoon';
  font-weight: bold;
  font-size: 50px;
}

.login_btn {
  font-family: 'Hanyoon';
  background-color: #D29953;
  border-radius: 15px;
  font-size: 24px;
  padding: 5px 15px;
  border: 0;
  outline: 0;
  color: white;
}
input::placeholder {
  font-family: 'Hanyoon';
}

input[type="text"],
input[type="password"] {
  display: inline-block;
  justify-content: center;
  box-sizing: border-box;
  margin-bottom: 20px;
  padding: 4px;
  width: 220px;
  height: 32px;
  border: none;
  border-bottom: 1px solid #AAA;
  font-family: 'Roboto', sans-serif;
  font-weight: 400;
  font-size: 15px;
  transition: 0.2s ease;
}
input[type="text"]:focus,
input[type="password"]:focus {
  border-bottom: 2px solid #16a085;
  color: #16a085;
  transition: 0.2s ease;
}
</style>