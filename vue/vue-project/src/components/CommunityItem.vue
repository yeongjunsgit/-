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
console.log(props.article.id)
const router = useRouter()
const goDetail = function(){
  console.log('디테일 뷰로 가기')
  router.push(`/community/${props.article.id}`)
  
}
</script>

<style lang="scss" scoped>

</style>