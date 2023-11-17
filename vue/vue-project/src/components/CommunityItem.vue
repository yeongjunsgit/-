<template>
  <div class="border"> 
    <p @click="goDetail">제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
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

<style lang="scss" scoped>

</style>