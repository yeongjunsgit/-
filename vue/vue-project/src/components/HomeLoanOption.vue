<template>
  <div v-if="product">
    <!-- {{   product }} -->
    <h4>{{ product.fin_prdt_nm }}</h4>
    <p>대출 한도 : {{ product.loan_lmt }}</p>
    <p>연체 이자율 : {{product.dly_rate}} </p>
    <p v-if="options">최저 금리 : {{ options[0].lend_rate_min }}</p>
    <hr>
  </div>
</template>

<script setup>
import { ref,onMounted } from 'vue'
import axios from 'axios'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()

const props = defineProps({
  product: Object,
})

const options = ref(null)

onMounted (()=>{
  axios({
      method:"get",
      url: `${store.API_URL}/fin_prct/list-homeloan-options/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
  })
  .then ((res)=>{
      console.log(res.data)
      console.log(props.option)
      options.value = res.data.filter((option)=>option.product === props.product.fin_prdt_cd)
  })
  .catch ((err) => {
      console.log(err)
  })
})
</script>

<style scoped>

</style>