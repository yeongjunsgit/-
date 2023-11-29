<template>
  <div class="my-3">
    <h3 class="mb-3"><strong>낮은 금리순</strong></h3>
    <div v-if="products">
      <div v-for="product in products">
        <div @click="gotoDetail([product.fin_prdt_cd])">상품 이름 :{{  product.fin_prdt_nm }}</div>
        <!-- <DepositLoanOptionVue
        :product="product"
        /> -->
      </div>
    </div>
  </div>
</template>

<script setup>
import DepositLoanOptionVue from '@/components/DepositLoanOption.vue'
import { useArticleStore } from '@/stores/articles'
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useArticleStore()
const products = ref(null)

const gotoDetail = function(fin_prdt_cd){
  router.push(`/depositloan_prdt/${fin_prdt_cd}`)
}

onMounted(() => {
  const store = useArticleStore()
  
  axios({
    method: 'get',
    url: `${store.API_URL}/fin_prct/list-depositloan-products/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res)=>{
    console.log(res.data)
    products.value = res.data
    
  })
  .catch((err) => {
    console.log(err)
    // axios({
    //   method: 'get',
    //   url: `${store.API_URL}/fin_prct/save-deposiloan-products/`,
    //   headers: {
    //     Authorization: `Token ${store.token}`
    //   }
    //   })
    //     .then((res)=>{
    //       console.log('저장')
      
    //     })
    //     .catch((err)=>{
    //       console.log(err)
    // }
    // )
  })
})

</script>

<style scoped>

</style>