<template>
  <div>
    <h1>Community Detail</h1>
  
    <div v-if="article">
      <!-- {{ article }}
      {{ mypk }} -->
      <!-- {{ article[0] }}s -->
    <!-- <p>글쓴이 : {{ article[0].user }}</p> -->
    <p>제목 : {{ article[0].title }}</p>
    <p>내용 : {{ article[0].content }}</p>
    <div v-if="mypk === article[0].user">
      <button @click="gotoUpdate">수정</button>
      <button @click="deleteArticle">삭제</button>
    </div>
  </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useArticleStore } from '@/stores/articles'
import axios from 'axios'
import { useRoute,useRouter } from 'vue-router'



const route = useRoute()
const article = ref(null)
const mypk = ref(null)
const store = useArticleStore()

onMounted(() => {
  const store = useArticleStore()
  mypk.value = store.mypk
  
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/lists/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {

    article.value = res.data.filter((data) => data.id === Number(route.params.id))
    // console.log(article.value)
    // console.log(route.params.id)
    })
    .catch((err) => {
      console.log(err)
    })
})
const router = useRouter()

const gotoUpdate = function(){
  console.log('업데이트하러가기')

  router.push({name:'update',params:route.params.id})
}

const deleteArticle = function () {
  const payload = {
    article_id: article.value[0].id,
    article_user:article.value[0].user,
    user: mypk.value
  }
  store.deleteArticle(payload)
}
</script>

<style scoped>

</style>