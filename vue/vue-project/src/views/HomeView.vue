
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
<style>

</style>