<template>
  <div class="my-3">
    <!-- <h1>DepositeSaving</h1> -->
    <h3 class="mb-3"><strong>고금리 예금 추천</strong></h3>
    <div v-if="products">
    <div v-for="product in products">
      <div class="title_over" @click="gotoDetail(product.fin_prdt_cd)">{{ product.fin_prdt_nm }}</div>
      <!-- <FinanPrdtOption
      :option="option"/> -->
    </div>
  </div>
  </div>
</template>

<script setup>

import FinanPrdtOption from '@/components/FinanPrdtOption.vue'
import {useArticleStore} from '@/stores/articles'
import { ref, onMounted } from "vue"
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useArticleStore()
const products = ref(null)

const gotoDetail = function(fin_prdt_cd){
  router.push(`/finan_prdt/${fin_prdt_cd}`)
}


onMounted(() => {
  const store = useArticleStore()

  axios({
    method: 'get',
    url: `${store.API_URL}/fin_prct/list-financial-products/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res)=>{
    // console.log(res.data)
    products.value = res.data

  })
  .catch((err) => {
    console.log(err)
    // axios({
    //   method: 'get',
    //   url: `${store.API_URL}/fin_prct/save-financial-products/`,
    //   headers: {
    //     Authorization: `Token ${store.token}`
    //   }
    // })
    // .then((res)=>{
    //   console.log('저장')
     

    // })
    // .catch((err)=>{
    //   console.log(err)
    // })
  })
})
</script>

<style scoped>



</style>