<template>
  <div v-if="product" @click="gotoDetail([options[0].product])">
    
    <h4>{{ product.fin_prdt_nm }}</h4>
    <p>대출 한도 : {{ product.loan_lmt }}</p>
    <p>연체 이자율 : {{product.dly_rate}} </p>

    <p v-if="options">최저 금리 : {{   options[0].lend_rate_min }}</p>
    <hr>
  </div>
</template>

<script setup>
import { ref,onMounted } from 'vue'
import axios from 'axios'
import { useArticleStore } from '@/stores/articles'
import { useRouter } from 'vue-router'

const router = useRouter()

const store = useArticleStore()

const props = defineProps({
  product: Object,
})

const gotoDetail = function(fin_prdt_cd){
  console.log(options)
  router.push(`/depositloan_prdt/${fin_prdt_cd}`)
}

const options = ref(null)

onMounted (()=>{

axios({
    method:"get",
    url: `${store.API_URL}/fin_prct/list-depositloan-options/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
})
.then ((res)=>{

    options.value = res.data.filter((option)=>option.product === props.product.fin_prdt_cd)
    
})
.catch ((err) => {
    console.log(err)
})
})

</script>

<style scoped>

</style>