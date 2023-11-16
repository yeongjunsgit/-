<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <p>
      <label for="username">아이디 : </label>
      <input id="username" v-model.trim="username" type="text" name="" >
    </p>
    <p>
      <label for="password1">비밀번호 : </label>
      <input id="password1" v-model.trim="password1" type="password" name="" >
    </p>
    <p>
      <label for="password2">비밀번호 확인 : </label>
      <input id="password2" v-model.trim="password2" type="password" name="" >
    </p>
      <input type="submit" name="" id="">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import {useArticleStore} from '@/stores/articles'

const store = useArticleStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
// 사용자의 입력을 하나의 객체로 싸서 보내주는 것
const signUp = function(){
  const payload = {
    username:username.value,
    password1:password1.value,
    password2:password2.value
  }
  store.signUp(payload)
}
</script>

<style scoped>

</style>