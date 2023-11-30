<template>
  <div class="my-3">
    <!-- <h1>DepositeSaving</h1> -->
    <h3 class="mb-3"><strong>고금리 예금 추천 왜안나와</strong></h3>
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

// import FinanPrdtOption from '@/components/FinanPrdtOption.vue'
import {useArticleStore} from '@/stores/articles'
import { ref, onMounted } from "vue"
import { useRouter } from 'vue-router'

const router = useRouter()
const products = ref(null)
const gotoDetail = function(fin_prdt_cd){
  router.push(`/finan_prdt/${fin_prdt_cd}`)
}


onMounted(() => {
  const type = 'financial'
  const store = useArticleStore()
  products.value = store.list_products(type)
  
})


</script>

<style scoped>



</style>