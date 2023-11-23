<template>
  <div>
    <div class="card my-3">
      <div class="card-body">
        <h5 class="card-title">{{ data.count }}명이 가입한 상품</h5>
        <h5 class="card-title">상품 이름 : {{ data.fin_prdt_nm }}</h5>
        <h6 class="card-subtitle mb-2 text-body-secondary">은행명 : {{  data.kor_co_nm  }}</h6>
        <div v-if="data.product_type == 'financial'">
          <p>상품 유형명 : 예금</p>
          <p v-if="data.max_limit != null">최고 한도 : {{ data.max_limit }}</p>
          <p v-else>최고 한도 : 없음</p>
          <a href="#" @click="gotoDetailFin(data.fin_prdt_cd)" class="card-link">세부정보 보러가기 ></a>
        </div>

        <div v-else-if="data.product_type == 'yearsaving'">
          <p>상품 유형명 : 연금 저축</p>
          <p>전년도 수익률 : {{ data.btrm_prft_rate_1 }}</p>
          <a href="#" @click="gotoDetailyearSave(data.fin_prdt_cd)" class="card-link">세부정보 보러가기 ></a>
        </div>
        <div v-else-if="data.product_type == 'saving'">
          <p>상품 유형명 : 적금</p>
          <p v-if="data.max_limit != null">최고 한도 : {{ data.max_limit }}</p>
          <p v-else>최고 한도 : 없음</p>
          <a href="#" @click="gotoDetailSave(data.fin_prdt_cd)" class="card-link">세부정보 보러가기 ></a>
        </div>
        <div v-else-if="data.product_type == 'depositloan'">
          <p>상품 유형명 : 전세 자금 대출</p>
          <p>최저 금리 : {{ data.max_option }}</p>
          <a href="#" @click="gotoDetailloan('depositloan',data.fin_prdt_cd)" class="card-link">세부정보 보러가기 ></a>
        </div>
        <div v-else-if="data.product_type == 'homeloan'">
          <p>상품 유형명 : 주택 담보 대출</p>
          <p>최저 금리 : {{ data.max_option }}</p>
          <a href="#" @click="gotoDetailloan('homeloan',data.fin_prdt_cd)" class="card-link">세부정보 보러가기 ></a>

        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  data: Object,
})

const router = useRouter()


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
</script>

<style scoped>

</style>