<template>
  <div class="card m-3 p-3">{{findata.split('|')[0]}}</div>

  </template>
  
  <script setup>
  
  import { useRouter } from 'vue-router';
  const router = useRouter
  const props = defineProps(
    {findata:String,}
    
    )

  </script>
  
  <style scoped>
  
  </style>