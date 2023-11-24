<template>
  <div>
    <h5 class="text-center my-5"><strong>나와 비슷한 나이대의 이용자들이 가입한 상품</strong></h5>
    <ProfileRecommendPrdt
    v-for="recom in ageRecommend.data"
    :data="recom"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useArticleStore } from '@/stores/articles'
import ProfileRecommendPrdt from '@/components/ProfileRecommendPrdt.vue'
import axios from 'axios';
import { useRoute } from 'vue-router';
const store = useArticleStore()
const route = useRoute()
const ageRecommend = ref([])

onMounted (() => {
  
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/age-filter/${route.params.age}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res.data)
      ageRecommend.value = res.data
      
    })
    .catch((err) => {
      console.log(err)
    })


})



</script>

<style scoped>

</style>