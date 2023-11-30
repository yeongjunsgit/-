<template>
  <div class="my-3">
    <!-- <h1>HomeLoan</h1> -->
    <h3 class="mb-3"><strong>낮은 금리순</strong></h3>
    <div v-if="products">
      <div v-for="product in products">
        <div class="title_over" @click="gotoDetail(product.fin_prdt_cd)">{{   product.fin_prdt_nm }}</div>
        <!-- <HomeLoanOptionVue
        :product="product"
        /> -->
      </div>
    </div>
  </div>
</template>

<script setup>
import HomeLoanOptionVue from '@/components/HomeLoanOption.vue'
import { useArticleStore } from '@/stores/articles'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()

const store = useArticleStore()
const products = ref(null)

const gotoDetail = function(fin_prdt_cd){
    router.push(`/homeloan_prdt/${fin_prdt_cd}`)
}

onMounted(() => {
  const store = useArticleStore()
  axios({
    method: 'get',
    url: `${store.API_URL}/fin_prct/list-homeloan-products/`,
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
          url: `${store.API_URL}/fin_prct/save-homeloan-products/`,
          headers: {
            Authorization: `Token ${store.token}`
          }})
        .then((res)=>{
          console.log('저장')
         
        })
        .catch((err)=>{
          console.log(err)
        }
        )
      })
})

</script>

<style scoped>

</style>