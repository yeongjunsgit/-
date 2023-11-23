<template>
  <div class="my-3">
    <!-- <h1>DepositeSaving</h1> -->
    <h3 class="mb-3"><strong>고금리 적금 추천</strong></h3>
    <div v-if="filteredOption">
    <div v-for="option in filteredOption">
      <SavingPrdtOption
      :option="option"/>
    </div>
  </div>
  </div>
</template>

<script setup>

import SavingPrdtOption from '@/components/SavingPrdtOption.vue'
import {useArticleStore} from '@/stores/articles'
import { ref, onMounted } from "vue"
import { RouterLink } from 'vue-router'
import axios from 'axios'

const store = useArticleStore()
const options = ref(null)
const filteredOption = ref([])
const products = ref(null)


onMounted(() => {
  const store = useArticleStore()

  axios({
    method: 'get',
    url: `${store.API_URL}/fin_prct/list-saving-options/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res)=>{
    console.log(res.data)
    options.value = res.data
    const loopCount = Math.min(res.data.length, 10); // 배열의 길이와 10 중 작은 값을 사용
    for (let i = 0; i < loopCount; i++) {
      filteredOption.value.push(res.data[i])
    }
    console.log(filteredOption)

    
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