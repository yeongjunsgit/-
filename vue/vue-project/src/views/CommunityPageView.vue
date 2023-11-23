<template>
  <div>
    <h1 class="text-center mt-5">커뮤니티</h1>
    <RouterLink class="d-block text-end m-3" :to="{name:'create'}">
      <i class="fa-solid fa-pen" style="color: #3d3d3d;"></i>
    </RouterLink>
    <div class="border d-flex">
      <div class="p-2">번호</div>
      <div class="p-2 flex-grow-1"> 내용</div>
      <div class="p-2 ">글쓴이</div>
    </div>
    <CommunityItem
      v-for="article in store.paginatedArticles"
      :article="article"
      :key="article.id"
    />
    <div class="pagination">
      <button v-for="pageNumber in store.pageNumbers" :key="pageNumber" @click="changePage(pageNumber)">
        {{ pageNumber }}
      </button>
    </div>
  </div>
</template>

<script setup>
import CommunityItem from '@/components/CommunityItem.vue';
import { useArticleStore } from '@/stores/articles';
import { onMounted } from "vue";
import { RouterLink } from 'vue-router';

const store = useArticleStore();

onMounted(() => {
  store.getArticles(); // 최초에 첫 페이지의 데이터를 가져옵니다.
});

const changePage = (pageNumber) => {
  store.getArticles(pageNumber); // 페이지 버튼을 클릭할 때 해당 페이지의 데이터를 가져옵니다.
};
</script>

<style scoped>
/* 스타일 추가 */
</style>
