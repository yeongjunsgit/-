<template>
  <div>
    <h1>Community Detail</h1>
    <div v-if="article">
    <p>제목 : {{ article[0].title }}</p>
    <p>내용 : {{ article[0].content }}</p>
  </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useArticleStore } from '@/stores/articles'
import axios from 'axios'
import { useRoute } from 'vue-router'
const route = useRoute()
const article = ref(null)

onMounted(() => {
  const store = useArticleStore()
  
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/lists/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
    // console.log(res.data)
    article.value = res.data.filter((data) => data.id === Number(route.params.id))
    console.log(typeof(article.value))
    // console.log(route.params.id)
    })
    .catch((err) => {
      console.log(err)
    })
})



</script>

<style scoped>

</style>