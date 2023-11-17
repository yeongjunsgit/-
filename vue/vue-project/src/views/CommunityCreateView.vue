<template>
  <div>
    <h1 class="fw-bold mt-3">게시글 생성 페이지</h1>
    <form @submit.prevent="createArticle">
      <div class="mb-3">
        <label for="exampleFormControlInput1" class="form-label">제목</label>
        <input v-model="title" type="text" class="form-control" id="exampleFormControlInput1">
      </div>
      <div class="mb-3">
        <label for="exampleFormControlTextarea1" class="form-label">내용</label>
        <textarea v-model="content" class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
      </div>
      <input type="submit" name="" id="">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import {useArticleStore} from '@/stores/articles'
import { RouterLink } from 'vue-router'

const store = useArticleStore()

const title = ref(null)
const content = ref(null)

const createArticle = function () {
  const payload = {
    title: title.value,
    content: content.value,
  }
  console.log(payload)
  store.createArticles(payload)
}

</script>

<style scoped>

</style>