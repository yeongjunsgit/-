<template>
  <div class="my-3">
    <!-- <h1>DepositeSaving</h1> -->
    <h3 class="mb-3"><strong>고금리 적금 추천</strong></h3>
    <div v-if="products">
    <div v-for="product in products">
      <p class="title_over"  @click="gotoDetail(product.fin_prdt_cd)">{{ product.fin_prdt_nm }}</p>
      
    </div>
  </div>
  </div>
</template>

<script setup>

import SavingPrdtOption from '@/components/SavingPrdtOption.vue'
import {useArticleStore} from '@/stores/articles'
import { ref, onMounted } from "vue"
import { useRouter} from 'vue-router'
import axios from 'axios'

const store = useArticleStore()
const products = ref(null)
const router = useRouter()

const gotoDetail = function(cd){
  router.push(`/saving_prdt/${cd}`)
}


onMounted(() => {
  const store = useArticleStore()

  axios({
    method: 'get',
    url: `${store.API_URL}/fin_prct/list-saving-products/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res)=>{
    
    products.value = res.data  
  })
  .catch((err) => {
      console.log(err)
      axios({
        method: 'get',
        url: `${store.API_URL}/fin_prct/save-saving-products/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      .then((res)=>{
          console.log('저장')
    
        })
      })
      .catch((err)=>{
        console.log(err)
      }
      )
    })

</script>

<style scoped>

</style>