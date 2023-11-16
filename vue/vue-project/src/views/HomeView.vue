
<template>
  <main>
    <h1>홈</h1>
    <div class="border carosal">
    <HomeEvent/>
    </div>
    <div class="border inblock">
    <HomeArticle/>
    </div>
    <div class="border inblock">
    <HomeExchange/>
  </div>
  </main>
</template>
<script setup>
import HomeArticle from '@/components/HomeArticle.vue';
import HomeEvent from '@/components/HomeEvent.vue';
import HomeExchange from '@/components/HomeExchange.vue';
</script>
<style scoped>
.border {
  border: 1px solid black;
}
.carosal {
  height: 300px;
}
.inblock {
  display: inline-block;
  width: 300px;
  height: 300px;
}
</style>