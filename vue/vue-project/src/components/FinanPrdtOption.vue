<template>
    <div v-if="product">

    <h4>{{ product[0].fin_prdt_nm }}</h4>
    <p>우대 조건 : {{ product[0].spcl_cnd }}</p>
    <p>가입 제한 : 
        <span v-if="product[0].join_deny===1">
            제한없음
        </span>
        <span v-else-if="product[0].join_deny===2">
            서민전용
        </span>
        <span v-else>
            일부제한
        </span>
    </p>
    <p>가입 대상 : {{ product[0].join_member }}</p>

    <p>최고 금리 옵션 : {{  option.intr_rate2 }}</p>
    


    
    <hr>
    </div>
</template>

<script setup>
import { ref,onMounted } from 'vue'
import axios from 'axios'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()

const props = defineProps({
    option:Object,
})

const product = ref(null)

onMounted (()=>{
axios({
    method:"get",
    url: `${store.API_URL}/fin_prct/list-financial-products/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
})
.then ((res)=>{
    // console.log(res.data)
    // console.log(props.option)
    product.value = res.data.filter((product)=>product.fin_prdt_cd === props.option.product)
})
.catch ((err) => {
    console.log(err)
})
})
</script>

<style  scoped>

</style>