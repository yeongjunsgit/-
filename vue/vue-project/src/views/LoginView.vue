<template>
  <div class="login-container">
    <h1>로그인</h1>
    <form @submit.prevent="login" class="login-form">
      <div class="mb-3">
        <input
          id="username"
          v-model.trim="username"
          type="text"
          class="form-control"
          placeholder="Username"
        />
      </div>
      <div class="mb-3">
        <input
          id="password"
          v-model="password"
          type="password"
          class="form-control"
          placeholder="Password"
        />
      </div>
      <button type="submit" class="btn btn-primary w-100">로그인</button>
    </form>
    <p @click="gotoSignup" class="mt-5">아직 회원이 아닌가요? <span class="text-primary">회원가입</span>
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/articles';
import { useRouter } from 'vue-router'
const store = useArticleStore();
const username = ref(null);
const password = ref(null);

const login = function() {
  // console.log('로그인 뷰')
  // console.log(username.value)
  // console.log(password.value)
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.login(payload);
};

const router = useRouter()
const gotoSignup = function(){
  router.push({name:'SignUpView'})
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  height: 100vh;
}

.login-form {
  width: 300px;
}
</style>
