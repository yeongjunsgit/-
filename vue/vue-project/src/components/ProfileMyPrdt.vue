<template>
    <div v-if="product">
      {{ product }}
      
    </div>
  </template>
  
  <script setup>
  
  import {useArticleStore} from '@/stores/articles'
  import { ref, onMounted } from "vue";

  
  const props = defineProps(
    {findata:Object,}
    )
  const product = ref(null)
  onMounted(()=>{
      const product_type = props.findata.split('|')[0]
      const code = props.findata.split('|')[1]
      const store = useArticleStore()
      const url = null
      product.value = store.findPrdt(product_type,code)
  })
  </script>
  
  <style scoped>
  
  </style>