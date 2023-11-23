<template>
  <div class="m-3" v-if="mySurvey">
    <!-- {{   mySurvey }} -->

    <h3 v-if="mySurvey.data.YearSavingPrdt">연금저축 상품</h3>
    <div class="card my-3" v-for="yearsave in mySurvey.data.YearSavingPrdt" >
  
      <div class="card-body">
        <h5 class="card-title">{{yearsave.fin_prdt_nm}}</h5>
        <h6 class="card-subtitle mb-2 text-body-secondary">은행 : {{yearsave.kor_co_nm}}</h6>
        <p class="card-text">전년도 수익률 : {{yearsave.btrm_prft_rate_1}}</p>
        <p class="card-text">2년전 수익률 : {{yearsave.btrm_prft_rate_2}}</p>
        <p class="card-text">3년전 수익률 : {{yearsave.btrm_prft_rate_3}}</p>
        
        <a href="#" @click="gotoDetailyearSave(yearsave.fin_prdt_cd)" class="card-link">세부정보 보러가기 ></a>
      </div>

    </div>
    
    <h3 v-if="mySurvey.data.saving_data">적금 상품</h3>
    <div class="card my-3" v-for="save in mySurvey.data.saving_data">
      <div class="card-body">
        <h5 class="card-title">{{save.fin_prdt_nm}}</h5>
        <h6 class="card-subtitle mb-2 text-body-secondary">은행 : {{save.kor_co_nm}}</h6>
        <p class="card-text">최대 금리 : {{save.intr_rate2}}</p>
        <p class="card-text">기간 : {{ save.save_rrm }}개월</p>
        <a href="#" @click="gotoDetailSave(gotoDetailloan.fin_prdt_cd)" class="card-link">세부정보 보러가기 ></a>
      </div>
    </div>
    <h3 v-if="mySurvey.data.deposit_data">예금 상품</h3>
    <div class="card" v-for="deposit in mySurvey.data.deposit_data">
      <div class="card-body">
        <h5 class="card-title">상품 이름 : {{deposit.fin_prdt_nm}}</h5>
        <h6 class="card-subtitle mb-2 text-body-secondary">은행 : {{deposit.kor_co_nm}}</h6>
        <p class="card-text">최대 금리 : {{deposit.intr_rate2}}</p>
        <p class="card-text">기간 : {{ deposit.save_rrm }}개월</p>
        <a href="#" @click="gotoDetailFin(deposit.fin_prdt_cd)" class="card-link">세부정보 보러가기 ></a>
      </div>
    </div>
    <div v-if="mySurvey.data.deposit_data"></div>
    <h3 v-if="mySurvey.data.loan_data">대출 상품</h3>
    <div class="card my-3" v-for="loan in mySurvey.data.loan_data">
      <div class="card-body">
        <h5 class="card-title">상품 이름 : {{loan.fin_prdt_nm}}</h5>
        <h6 class="card-subtitle mb-2 text-body-secondary">은행 : {{loan.kor_co_nm}}</h6>
        <p class="card-text">최저 금리 : {{loan.lend_rate_min}}</p>
        <p class="card-text">최대 금리 : {{ loan.lend_rate_max }}</p>
        <a href="#" @click="gotoDetailloan(loan.fin_prdt_cd)" class="card-link">세부정보 보러가기 ></a>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useArticleStore } from '@/stores/articles'
import ProfileRecommendPrdt from '@/components/ProfileRecommendPrdt.vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const mySurvey = ref(null)

const gotoDetailyearSave = function(fin_prdt_cd){
  router.push(`/yearsaving_prdt/${fin_prdt_cd}`)
}
const gotoDetailSave = function(fin_prdt_cd){
  router.push(`/saving_prdt/${fin_prdt_cd}`)
}

const gotoDetailFin = function(fin_prdt_cd){
  router.push(`/finan_prdt/${fin_prdt_cd}`)
}
const gotoDetailloan = function(type,fin_prdt_cd){
  if (type='house_loan'){
  router.push(`/homeloan_prdt/${fin_prdt_cd}`)
} else {
    router.push(`/depositloan_prdt/${fin_prdt_cd}`)
    
  }
}
onMounted (() => {
  const store = useArticleStore()
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/get-survey/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res) => {
    console.log(res.data)
    mySurvey.value = res.data
    
  })
  .catch((err) => {
    console.log(err)
  })
})

</script>

<style scoped>

</style>