
<template>
  <main>

    <div class="">
    <HomeEvent/>
    </div>
    <div class="d-flex justify-content-evenly">
      <div class="homeviewbtn" @click="gotoCom">
        커뮤니티
      </div>
      <div class="homeviewbtn" @click="gotoFin">
        금융상품
      </div>
      <div class="homeviewbtn" @click="gotoProfile">
        프로필
      </div>
      <div class="homeviewbtn" @click="gotoExcalcul">
        환율
      </div>
      <div class="homeviewbtn" @click="gotoMap">
        근처 은행
      </div>
    </div>
    <div class="border inblock">
    <HomeArticle/>
    </div>
    <div class="border inblock">
    
  </div>
  </main>
</template>
<script setup>
import HomeArticle from '@/components/HomeArticle.vue';
import HomeEvent from '@/components/HomeEvent.vue';
// import ExCalculView from '@/views/ExCalculView.vue';
import { useRouter } from 'vue-router';
import ExCalculView from './ExCalculView.vue';

const router = useRouter()
const gotoCom = function(){
  router.push({name:'CommunityView'})
}
const gotoFin = function(){
  router.push({name:'recommendView'})
  
}
const gotoProfile = function(){
  router.push({name:'ProfileView'})
  
}
const gotoMap = function(){
  router.push({name:'NearBankView'})

}
const gotoExcalcul = function(){
  router.push({name:'ExCalculView'})

}
</script>

<style scoped>
.homeviewbtn {
  margin:10px;
  width: 15%;
  padding: 15px;
  border-radius: 12%;
  text-align: center;
  color: rgb(53, 169, 204); /* 글자 색상 설정 */
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid rgb(53, 169, 204);
}

</style>