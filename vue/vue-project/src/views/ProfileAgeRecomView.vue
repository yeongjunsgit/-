<template>
  <div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useArticleStore } from '@/stores/articles'
import axios from 'axios';

const store = useArticleStore()

const ageData = defineProps({
  age: Object,
})

const ageRecommend = ref([])

onMounted (() => {
  console.log(ageData.age.age)
  // 1. 모든 유저 정보를 가져와 나이가 위아래로 10인 사람들의 정보를 추려냄
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/age-filter/${ageData.age.age}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res.data)
      ageRecommend.value = res.data.filter((item) =>  Math.max(0, props.age - 10) <= item.user.age <= props.age + 10)
      
    })
    .catch((err) => {
      console.log(err)
    })


})



</script>

<style scoped>

</style>