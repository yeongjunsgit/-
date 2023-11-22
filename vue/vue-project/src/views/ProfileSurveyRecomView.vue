<template>
  <div>
    {{   mySurvey }}
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useArticleStore } from '@/stores/articles'
import ProfileRecommendPrdt from '@/components/ProfileRecommendPrdt.vue'
import axios from 'axios'

const mySurvey = ref(null)

onMounted (() => {
  const store = useArticleStore()
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/get-survey/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res) => {
    console.log(res.data)
    mySurvey.value = res.data
    
  })
  .catch((err) => {
    console.log(err)
  })
})

</script>

<style scoped>

</style>