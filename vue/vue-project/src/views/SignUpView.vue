<template>
  <div class="signup-container">
    <h1>회원가입</h1>
    <form @submit.prevent="signUp" class="signup-form">
      <div class="mb-3">
        
        <input
          id="username"
          v-model.trim="username"
          type="text"
          class="form-control"
          name=""
          placeholder="아이디 *"
        />
      </div>
      <div class="mb-3">
        
        <input
          id="password1"
          v-model.trim="password1"
          type="password"
          class="form-control"
          name=""
          placeholder="비밀번호 *"
        />
      </div>
      <div class="mb-3">
        
        <input
          id="password2"
          v-model.trim="password2"
          type="password"
          class="form-control"
          name=""
          placeholder="비밀번호 확인 *"
        />
      </div>
      <div class="mb-3">
        <p>{{ typeof(age) }}</p>
        <!-- <label for="password2" class="form-label">나이 :</label> -->
        <input
          id="age"
          v-model.trim="age"
          type="text"
          class="form-control"
          name=""
          placeholder="나이 *"
        />
      </div>

      
      <div class="mb-3">
        <!-- <label for="salary" class="form-label">연봉 :</label> -->
        <input
          id="salary"
          v-model.trim="salary"
          type="text"
          class="form-control"
          name=""
          placeholder="연봉"
        />
      </div>
      <div class="mb-3">
        <!-- <label for="password2" class="form-label">자금 :</label> -->
        <input
          id="money"
          v-model.trim="money"
          type="text"
          class="form-control"
          name=""
          placeholder="자금"
        />
      </div>
      <div class="mb-3">
        <!-- <label for="password2" class="form-label">닉네임 :</label> -->
        <input
          id="nickname"
          v-model.trim="nickname"
          type="text"
          class="form-control"
          name=""
          placeholder="닉네임"
        />
      </div>
      <div class="mb-3">
        <!-- <label for="password2" class="form-label">소장한 금융상품 :</label> -->
        <input
          id="prdts"
          v-model.trim="prdts"
          type="text"
          class="form-control"
          name=""
          placeholder="소장한 금융상품"
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
const age = ref(null);
const salary = ref(null);
const money = ref(null);
const nickname = ref(null);
const prdts = ref(null);


const signUp = function() {
  console.log(Number(age.value))
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    age: Number(age.value),
    salary: Number(salary.value),
    money: Number(money.value),
    nickname: nickname.value,
    prdts: prdts.value,
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
