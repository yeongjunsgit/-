<template>
  <div class="signup-container">
    <h1>수정</h1>
    <form @submit.prevent="changePassword" class="signup-form">
      <div class="my-3">
        
       
        
        <input
          id="password1"
          v-model.trim="new_password1"
          type="password"
          class="form-control"
          name=""
          placeholder="새 비밀번호 *"
        />
   
        
        <input
          id="password2"
          v-model.trim="new_password2"
          type="password"
          class="form-control"
          name=""
          placeholder="새 비밀번호 확인*"
        />
      </div>
        
      
      <button type="submit" class="btn btn-primary w-100 mt-3">회원가입</button>
    </form>
    
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/articles';
import { useRouter } from 'vue-router'

const router = useRouter()

const store = useArticleStore();

const new_password1 = ref(null);
const new_password2 = ref(null);

const changePassword = function(){
  const payload = {
    new_password1:new_password1.value,
    new_password2:new_password2.value,
  }
  console.log('비밀번호 변경 뷰에서 보냄')
  store.changePassword(payload)
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
