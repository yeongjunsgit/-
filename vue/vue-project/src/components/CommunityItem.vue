<!-- CommnityItemView.vue -->
<template>
  <div class="border d-flex"> 
    <!-- {{ article }} -->
    <div class="p-2 px-3" @click="goDetail">{{ article.id }}</div>
    <div class="p-2 flex-grow-1" @click="goDetail">{{ article.title }}</div>
    
    <div class="p-2 ">{{ article.user.username }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'

const props = defineProps({
  article: Object,
})
// console.log(props.article.id)
const router = useRouter()
const goDetail = function(){
  router.push(`/community/${props.article.id}`)
  
}
</script>

<style scoped>
</style>