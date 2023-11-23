<template>
  <div class="my-3">
    <!-- <h1>HomeLoan</h1> -->
    <div v-if="filteredData">
      <div v-for="product in filteredData">
        <HomeLoanOptionVue
        :product="product"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import HomeLoanOptionVue from '@/components/HomeLoanOption.vue'
import { useArticleStore } from '@/stores/articles'
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import axios from 'axios'

const store = useArticleStore()
const options = ref(null)
const filteredData = ref([])
const products = ref(null)

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
    console.log(res.data)
    options.value = res.data
    const loopCount = Math.min(res.data.length, 10); // 배열의 길이와 10 중 작은 값을 사용
    for (let i = 0; i < loopCount; i++) {
      filteredData.value.push(res.data[i])
    }
    console.log(filteredData)
  })
  .catch((err) => {
        console.log(err)
        axios({
          method: 'get',
          url: `${store.API_URL}/fin_prct/save-houseloan-products/`,
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