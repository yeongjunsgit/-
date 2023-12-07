<template>
  <div class="my-3">
    <div class="input-group mb-3">
      <input v-model="search_prdt" type="text" class="form-control" placeholder="상품이름" aria-label="Recipient's username" aria-describedby="button-addon2">
      <button @click="searchPrdt" class="btn btn-outline-primary" type="button" id="button-addon2">검색하기</button>
    </div>
    <br>
    <div class="d-flex">
      <div class="first">상품이름</div>
      <div class="others">6M</div>
      <div class="others">12M</div>
      <div class="others">24M</div>
      <div class="others">36M</div>

    </div>
    <hr>
    <div v-if="search">
      <div v-for="product in result_prdt">
        <div class="title_over" @click="gotoDetail(product.fin_prdt_cd)">
        <FinanPrdtOption
        :product="product"/>
        </div>
      </div>
    </div>
    <div v-else>
      <div v-if="products">
        <div v-for="product in products">
          <div class="title_over" @click="gotoDetail(product.fin_prdt_cd)">
            <FinanPrdtOption
            :product="product"/>
          </div>
        </div>
      </div>
    </div>

    
  </div>
</template>

<script setup>

import FinanPrdtOption from '@/components/FinanPrdtOption.vue'
import {useArticleStore} from '@/stores/articles'
import { ref, onMounted } from "vue"
import { useRouter } from 'vue-router'

const router = useRouter()

const gotoDetail = function(fin_prdt_cd) {
  router.push(`/finan_prdt/${fin_prdt_cd}`)
}
const store = useArticleStore()
const products = ref(null)
const search_prdt = ref(null)
const result_prdt = ref(null)
const search = ref(false)
const searchPrdt = function () {
  result_prdt.value = products.value.filter((item) => item.fin_prdt_nm.includes(search_prdt.value))
  search.value = true
}

onMounted(async () => {
  const type = 'financial'
  products.value = await store.tmp_products(type)
})


</script>

<style scoped>

.first {
  flex-basis: 60%;
}

.others {
  flex-basis: 10%;
}

</style>