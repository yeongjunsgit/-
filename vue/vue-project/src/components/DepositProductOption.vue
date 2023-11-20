<template>
    <div>
        {{ option|length }}
        <hr>
        {{ product }}
        <hr>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()

const props = defineProps({
    option:Object,
})

const product = ref(null)


axios({
    method:"get",
    url: `${store.API_URL}/fin_prct/list-financial-products/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
})
.then ((res)=>{
    console.log(res.data)
    console.log(props.option)
    product.value = res.data.filter((product)=>product.fin_prdt_cd === props.option.product.fin_prdt_cd)
})
.catch ((err) => {
    console.log(err)
})

</script>

<style  scoped>

</style>