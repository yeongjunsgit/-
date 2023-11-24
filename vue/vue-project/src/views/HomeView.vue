
<template>
  <main>

    <div class="">
    <HomeEvent/>
    </div>
    <div class="d-flex justify-content-evenly">
      <div class="homeviewbtn btn btn-outline-primary" @click="gotoCom">
        <strong>커뮤니티</strong>
      </div>
      <div class="homeviewbtn btn btn-outline-primary" @click="gotoFin">
        <strong>금융상품</strong>
      </div>
      <div class="homeviewbtn btn btn-outline-primary" @click="gotoProfile">
        <strong>프로필</strong>
      </div>
      <div class="homeviewbtn btn btn-outline-primary" @click="gotoExcalcul">
        <strong>환율</strong>
      </div>
      <div class="homeviewbtn btn btn-outline-primary" @click="gotoMap">
        <strong>근처 은행</strong>
      </div>
    </div>
    <div class="d-flex">
    <div class="w-50 p-5">
    <HomeArticle/>
    </div>
    <div class="w-30 p-5">
    <HomeExchange/>
    </div>
  </div>
  </main>
</template>
<script setup>
import HomeArticle from '@/components/HomeArticle.vue';
import HomeEvent from '@/components/HomeEvent.vue';
import HomeExchange from '@/components/HomeExchange.vue';
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
  margin:30px 10px;
  width: 15%;
  height:100px;
  padding: 15px;
  border-radius: 15%;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>