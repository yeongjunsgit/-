<!-- CommunityView.vue -->
<template>
  <div>
    <h1 class="text-center mt-5">커뮤니티</h1>
    <RouterLink class="d-block text-end m-3" :to="{name:'create'}">
      <i class="fa-solid fa-pen" style="color: #3d3d3d;"></i></RouterLink>
    <div>
    <div class="border d-flex"> 
    <div class="p-2">번호</div>
    <div class="p-2 flex-grow-1"> 내용</div>
    
    <div class="p-2 ">글쓴이</div>
    </div>
    <CommunityItem
    v-for="article in store.articles"
    :article="article"/>
    </div>
  </div>
</template>

<script setup>

import CommunityItem from '@/components/CommunityItem.vue';
import {useArticleStore} from '@/stores/articles'
import { ref, onMounted } from "vue";
import { RouterLink } from 'vue-router'

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style scoped>

</style>