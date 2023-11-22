<template>
  <div>
    <div v-if="product">
    <h1>{{ product.fin_prdt_nm }}</h1>
    <h3>금융회사 : {{ product.kor_co_nm }}</h3>
    <p>중도상환 수수료 : {{ product.erly_rpay_fee }}</p>
    <p>연체 이자율 : {{ product.dly_rate }}</p>
    <p>대출 한도 : {{ product.loan_lmt }}</p>
    <p>대출 인지비용 : {{ product.loan_inci_expn }}</p>
    <p>가입 방법 : {{ product.join_way }}</p>
    </div>
    <h2>옵션들</h2>
    <div v-if="options">
      <div class="card" v-for="option in options">
          <p>대출 상환 유형명 : {{ option.rpay_type_nm }}</p>
          <p>대출 금리 유형명 : {{ option.lend_rate_type_nm }}</p>
          <p>최저 대출 금리 [소수점 2자리] : {{ option.lend_rate_min }}</p>
          <p>대출금리_최고 [소수점 2자리] : {{ option.lend_rate_max }}</p>
          <p>전월 취급 평균금리 [소수점 2자리] {{ option.lend_rate_avg }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import {useArticleStore} from '@/stores/articles'
import { ref, onMounted } from "vue"
import axios from 'axios'

const route = useRoute()
const fin_prdt_cd = ref(route.params.fin_prdt_cd)
const product = ref(null)
const options = ref(null)

onMounted(() => {
const store = useArticleStore()
// object_financial_products
// object_financial_options
axios({
    method: 'get',
    url: `${store.API_URL}/fin_prct/object_depositloan_products/${fin_prdt_cd.value}`,
    headers: {
    Authorization: `Token ${store.token}`
    }
})
.then((res)=>{
    console.log(res.data)
    product.value = res.data
    axios({
    method: 'get',
    url: `${store.API_URL}/fin_prct/object_depositloan_options/${fin_prdt_cd.value}`,
    headers: {
    Authorization: `Token ${store.token}`
        }
    })
    .then((res)=>{
        console.log(res.data)
        options.value = res.data
    })
    .catch((err) => {
        console.log(err)
    })
})
.catch((err) => {
    console.log(err)
})
})

</script>

<style scoped>

</style>