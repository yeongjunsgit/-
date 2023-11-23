<template>
  <div>
    <h1 class="text-center mt-5">커뮤니티</h1>
    <RouterLink class="d-block text-end m-3" :to="{ name: 'create' }">
      <i class="fa-solid fa-pen" style="color: #3d3d3d;"></i>
    </RouterLink>
    <div>
      <div class="border d-flex">
        <div class="p-2">번호</div>
        <div class="p-2 flex-grow-1"> 내용</div>
        <div class="p-2">글쓴이</div>
      </div>
      <div v-for="(article, index) in paginatedArticles" :key="index">
        <CommunityItem :article="article" :number="index + 1" />
      </div>
    </div>
    <div class="d-flex justify-content-center mt-4">
      <ul class="pagination">
        <li class="page-item" @click="prevPage" :disabled="currentPage === 1"><a class="page-link" href="#">이전</a></li>
        <li class="page-item"><a class="page-link" href="#">{{ currentPage }}</a></li>
        <li class="page-item" @click="nextPage" :disabled="currentPage === totalPages"><a class="page-link" href="#">다음</a></li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import CommunityItem from "@/components/CommunityItem.vue";
import { useArticleStore } from "@/stores/articles";
import { ref, onMounted, computed } from "vue";
import { RouterLink } from "vue-router";

const store = useArticleStore();
let number = 0;
const articlesPerPage = 10;
const currentPage = ref(1);

onMounted(() => {
  store.getArticles();
});

const paginatedArticles = computed(() => {
  const startIndex = (currentPage.value - 1) * articlesPerPage;
  const endIndex = startIndex + articlesPerPage;
  return store.articles.slice(startIndex, endIndex);
});

const totalPages = computed(() => Math.ceil(store.articles.length / articlesPerPage));

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};
</script>

<style scoped>
/* 필요한 스타일링 추가 */
/* .pagination {
  display: flex;
  justify-content: center;
  margin-top: 10px;
} */
</style>
