<template>
  <div class="card">
    <p>옵션</p>
    {{ option }}
    <hr>
    <p>상품</p>
    {{ product }}
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()

const props = defineProps({
    option: Object,
})

const product = ref(null)


axios({
    method:"get",
    url: `${store.API_URL}/fin_prct/list-depositloan-products/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
})
.then ((res)=>{
    console.log("상품",res.data)
    console.log('옵션',props.option)
    product.value = res.data.filter((product)=>product.fin_prdt_cd === props.option.product)
    console.log(res.data[0].fin_prdt_cd)
})
.catch ((err) => {
    console.log(err)
})

</script>

<style scoped>

</style>