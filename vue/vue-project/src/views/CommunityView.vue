<template>
  <div>
    <h1>Community</h1>
    <RouterLink :to="{name:'create'}">[Create]</RouterLink>
    <CommunityItem
    v-for="article in store.articles"
    :article="article"/>
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