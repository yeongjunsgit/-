<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="login">
      <p>
      <label for="username">아이디 : </label>
      <input id="username" v-model.trim="username" type="text">
    </p>
    <p>
      <label for="password">비밀번호 : </label>
      <input id="password" v-model="password" type="password">
    </p>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import {useArticleStore} from '@/stores/articles'

const store = useArticleStore()
const username = ref(null)
const password = ref(null)

// 사용자의 입력을 하나의 객체로 싸서 보내주는 것
const login = function(){
  const payload = {
    username: username.value,
    password: password.value,
  
  }
  store.login(payload)
}
</script>

<style scoped>

</style>