<template>
  <div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useArticleStore } from '@/stores/articles'
import axios from 'axios';

defineProps({
  userinfo: Object,
})

const ageRecommend = ref([])

onMounted (() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/fin_prct/입력해주세요./`,
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