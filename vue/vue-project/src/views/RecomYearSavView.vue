<template>
  <div class="my-3">
    <!-- <h1>YearSaving</h1> -->
    <h3 class="mb-3"><strong>전년도 수익률 순</strong></h3>
    <div v-if="products">
      <div v-for="product in products">
        <div @click="gotoDetail(product.fin_prdt_cd)">
          
          <div class="title_over">{{product.fin_prdt_nm }}
          </div>

          <div>{{product.kor_co_nm }}
          </div>

        </div>
        <!-- <YearSavPrdtOptionVue
        :option="option"/> -->
      </div>
    </div>
  </div>
</template>

<script setup>
import YearSavPrdtOptionVue from '@/components/YearSavPrdtOption.vue'
import { useArticleStore } from '@/stores/articles'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const store = useArticleStore()
const products = ref(null)
const router = useRouter()

const gotoDetail = function(cd){
  router.push(`/yearsaving_prdt/${cd}`)
}
onMounted(() => {
  const store = useArticleStore()
  axios({
  method: 'get',
  url: `${store.API_URL}/fin_prct/list-yearsaving-products/`,
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
    axios({
      method: 'get',
      url: `${store.API_URL}/fin_prct/save-yearsaving-products/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then((res)=>{
      console.log(res.data)
      
    })
    .catch((err) => {
      console.log(err)
    })
  })
  


})


</script>

<style scoped>

</style>