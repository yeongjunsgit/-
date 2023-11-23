<template>
  <div class="my-3">
    <!-- <h1>YearSaving</h1> -->
    <div v-if="filteredData">
      <div v-for="option in filteredData">
        <YearSavPrdtOptionVue
        :option="option"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import YearSavPrdtOptionVue from '@/components/YearSavPrdtOption.vue'
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
  url: `${store.API_URL}/fin_prct/list-yearsaving-options/`,
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
      products.value = res.data
      const loopCount = Math.min(res.data.length, 10); // 배열의 길이와 10 중 작은 값을 사용
      for (let i = 0; i < loopCount; i++) {
        filteredData.value.push(res.data[i])
      }
      console.log(filteredData)
    })
    .catch((err) => {
      console.log(err)
    })
  })
  


})


</script>

<style scoped>

</style>