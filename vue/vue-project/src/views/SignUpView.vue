<template>
  <div class="signup-container">
    <h1>회원가입</h1>
    <form @submit.prevent="signUp" class="signup-form">
      <div class="mb-3">
        <label for="username" class="form-label">아이디 :</label>
        <input
          id="username"
          v-model.trim="username"
          type="text"
          class="form-control"
          name=""
          placeholder="Username"
        />
      </div>
      <div class="mb-3">
        <label for="password1" class="form-label">비밀번호 :</label>
        <input
          id="password1"
          v-model.trim="password1"
          type="password"
          class="form-control"
          name=""
          placeholder="Password"
        />
      </div>
      <div class="mb-3">
        <label for="password2" class="form-label">비밀번호 확인 :</label>
        <input
          id="password2"
          v-model.trim="password2"
          type="password"
          class="form-control"
          name=""
          placeholder="Confirm Password"
        />
      </div>
      <button type="submit" class="btn btn-primary w-100 mt-3">회원가입</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/articles';

const store = useArticleStore();
const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);

const signUp = function() {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };
  store.signUp(payload);
};
</script>

<style scoped>
.signup-container {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  height: 100vh;
}

.signup-form {
  width: 300px;
}
</style>
