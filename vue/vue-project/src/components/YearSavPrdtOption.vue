<template>
  <div v-if="product">
    <h4>{{ product[0].fin_prdt_nm }}</h4>
    
    <p>가입 제한 : 제한없음 </p>
    <p>전년도 수익률 : {{ product[0].btrm_prft_rate_1 }}</p>
    <hr>
  </div>
</template>

<script setup>
import { ref,onMounted } from 'vue'
import axios from 'axios'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()

const props = defineProps({
  option: Object,
})

const product = ref(null)


onMounted (()=>{
axios({
    method:"get",
    url: `${store.API_URL}/fin_prct/list-yearsaving-products/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
})
.then ((res)=>{
    // console.log(res.data)
    // console.log(props.option)
    product.value = res.data.filter((product)=>product.fin_prdt_cd === props.option.product)
})
.catch ((err) => {
    console.log(err)
})
})

</script>

<style scoped>

</style>