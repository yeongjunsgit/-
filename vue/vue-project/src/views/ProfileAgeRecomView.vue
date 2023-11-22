<template>
  <div>
    <!-- {{ ageRecommend }} -->
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

const store = useArticleStore()

const ageData = defineProps({
  age: Object,
})
console.log('ageData',ageData)
const ageRecommend = ref([])

onMounted (() => {
  console.log(ageData.age.age)
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/age-filter/${ageData.age.age}/`,
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