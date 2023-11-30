<template>
  <div>
    <div>상품 : {{ product.fin_prdt_nm }}</div>
    <div>옵션 왜 안나와 : {{ options }}</div>
  </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/articles'
import { useRouter } from 'vue-router';

const router = useRouter()
const store = useArticleStore()

const gotoDetail = function(fin_prdt_cd){
  console.log(fin_prdt_cd)
  router.push(`/yearsaving_prdt/${fin_prdt_cd}`)
}
const props = defineProps({
  product: Object,
})

const options = store.options
</script>

<style scoped>

</style>