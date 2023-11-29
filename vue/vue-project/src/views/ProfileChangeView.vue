<template>
  <div class="signup-container">
    <h1>수정</h1>
    <form @submit.prevent="changeInfo" class="signup-form">
      <div class="my-3">
        
        <input
          id="nickname"
          v-model.trim="nickname"
          type="text"
          class="form-control"
          name=""
          placeholder="닉네임 *"
        />
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

        <input
          id="salary"
          v-model.trim="salary"
          type="text"
          class="form-control"
          name=""
          placeholder="연봉"
        />

        
        <input
          id="money"
          v-model.trim="money"
          type="text"
          class="form-control"
          name=""
          placeholder="자금"
        />


      </div>
      
      <button type="submit" class="btn btn-primary w-100 mt-3">수정하기</button>
    </form>
    <br>
    <button @click="gotochangePassword" class="btn btn-info w-50 mt-3">비밀번호 수정</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/articles';
import { useRouter } from 'vue-router'

const router = useRouter()
// import MyFinPrdtForm from '../components/MyFinPrdtForm.vue';
const store = useArticleStore();
const age = ref(null);
const salary = ref(null);
const money = ref(null);
const nickname = ref(null);
// const prdts = ref(null)

const gotochangePassword = function(){
  router.push(`/profile/${store.myname}/change/password`)
}
const changeInfo = function() {

  const payload = {
    age: Number(age.value),
    salary: Number(salary.value),
    money: Number(money.value),
    nickname: nickname.value,

  }
  console.log('뷰에서 수정 보내기')
  store.changeInfo(payload)
}

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
