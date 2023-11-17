<template>
  <div>
    <h1 class="fw-bold mt-3">게시글 수정 페이지</h1>

    <form v-if="article" @submit.prevent="updateArticles">
      <div class="mb-3">
        <label for="title" class="form-label">제목</label>
        <input v-model="title" type="text" class="form-control" id="title">
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">내용</label>
        <textarea v-model="content" class="form-control" id="content" rows="3"></textarea>
      </div>
      <input type="submit" name="" id="">
    </form>
  </div>
</template>

<script setup>
import { ref,onMounted } from 'vue'
import {useArticleStore} from '@/stores/articles'
import axios from 'axios';
import { RouterLink, routeLocationKey } from 'vue-router'
import { useRoute } from 'vue-router';
const store = useArticleStore()
const article = ref(null)

const route = useRoute()
const title = ref(null)
const content = ref(null)

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

    article.value = res.data.filter((data) => data.id === Number(route.params.id))
    title.value=article.value[0].title
    content.value=article.value[0].content
    // console.log(article.value)
    // console.log(route.params.id)
    })
    .catch((err) => {
      console.log(err)
    })
  
})


const updateArticles = function () {
  console.log(article.value[0].user)
  const payload = {
    title: title.value,
    content: content.value,
    article_id:route.params.id,
    user: store.mypk,
    article_user: article.value[0].user.id,
  }
  store.updateArticle(payload)
}

</script>

<style scoped>

</style>