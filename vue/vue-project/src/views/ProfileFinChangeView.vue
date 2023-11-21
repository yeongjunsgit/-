<template>
  <div>
    <h1>ProfileFinChangeView</h1>
    <MyFinPrdtForm
    @emit-prdts="gerPrdts"
    />
  </div>
</template>

<script setup>
import MyFinPrdtForm from '@/components/MyFinPrdtForm.vue'
import { ref } from 'vue'
import axios from 'axios'
import { useArticleStore } from '@/stores/articles'


const store = useArticleStore()

const prdt_cd_list = ref([])
const type_list = ref([])

const gerPrdts = function(ps){
  console.log('이벤트를 받았습니다')
  console.log(ps)

  ps.forEach(prdt => {
    prdt_cd_list.value.push(prdt.fin_prdt_cd)
    type_list.value.push(prdt.type)
  })

  axios ({
    method: 'put',
    url: `${store.API_URL}/accounts/add-data/`,
    data: {  
      user:store.mypk,
      financial_products:prdt_cd_list.value.join(','),
      product_type:type_list.value.join(',')
    },
    headers: {
            Authorization: `Token ${store.token}`
          }
  })
  .then((res) => {
   console.log(res) 
  })
  .catch((err)=>console.log(err))
  
}
</script>

<style scoped>

</style>