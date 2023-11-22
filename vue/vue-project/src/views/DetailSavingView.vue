<template>
<div>
    <div v-if="product">
        <h1>{{ product.fin_prdt_nm }}</h1>
        <h3>은행 : {{ product.kor_co_nm }}</h3>
        <p>가입 방법 : {{ product.join_way }}</p>
        <p>만기 후 이자율 : {{ product.mtrt_int }}</p>
        <p>가입 대상 : {{ product.join_member }}</p>
        <p>기타 유의 사항 : {{ product.etc_note }}</p>
        <p>최대한도 : 
            <span v-if="product.max_limit">{{ product.max_limit }}원</span>
            <span v-else>없음</span>
        </p>
        <p>가입 방법 : {{ product.join_way }}</p>

        </div>
        <h3>옵션들</h3>
        <div v-if="options">
        <div class="card" v-for="option in options">
           <p>저축 금리 유형 : {{ option.intr_rate_type }}</p>
           <p>저축 금리 유형명 : {{ option.intr_rate_type_nm }}</p>
           <p>저축 금리 [소수점 2자리] : {{ option.intr_rate }}</p>
           <p>저축 기간 [단위: 개월] : {{ option.save_trm }}</p>
           <p>최고 우대금리 [소수점 2자리] {{ option.intr_rate2 }}</p>
        </div>
    </div>
</div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import {useArticleStore} from '@/stores/articles'
import { ref, onMounted } from "vue"
import axios from 'axios'

const route = useRoute()
const fin_prdt_cd = ref(route.params.fin_prdt_cd)
const product = ref(null)
const options = ref(null)

onMounted(() => {
const store = useArticleStore()
// object_financial_products
// object_financial_options
axios({
    method: 'get',
    url: `${store.API_URL}/fin_prct/object_saving_products/${fin_prdt_cd.value}`,
    headers: {
    Authorization: `Token ${store.token}`
    }
})
.then((res)=>{
    console.log(res.data)
    product.value = res.data
    axios({
    method: 'get',
    url: `${store.API_URL}/fin_prct/object_saving_options/${fin_prdt_cd.value}`,
    headers: {
    Authorization: `Token ${store.token}`
        }
    })
    .then((res)=>{
        console.log(res.data)
        options.value = res.data
    })
    .catch((err) => {
        console.log(err)
    })
})
.catch((err) => {
    console.log(err)
})
})
</script>

<style scoped>

</style>