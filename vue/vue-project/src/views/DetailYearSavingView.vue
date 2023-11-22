<template>
<div>
    <div v-if="product">
        <h1>{{ product.fin_prdt_nm }}</h1>
        <h3>금융회사 : {{ product.kor_co_nm }}</h3>
        <p>판매사 : {{ product.sale_co }}</p>
        <p>가입 방법 : {{ product.join_way }}</p>
        <p>연금종류명 : {{ product.pnsn_kind_nm }}</p>
        <p>상품유형명 : {{ product.prdt_type_nm }}</p>
        <p>공시 이율 : {{ product.dcls_rate }}</p>
        <p>최저 보증 이율 : {{ product.guar_rate }}</p>
        <p>과거 수익률1 (전년도) : {{ product.btrm_prft_rate_1 }}</p>
        <p>과거 수익률2 (전전년도) : {{ product.btrm_prft_rate_2 }}</p>
        <p>과거 수익률3 (전전전년도) : {{ product.btrm_prft_rate_3 }}</p>
        <p>기타 사항 : {{ product.etc }}</p>
    </div>
    <h3>옵션들</h3>
    <div v-if="options">
        <div class="card" v-for="option in options">
           <p>최소 기간 : {{ option.pnsn_recp_trm_nm }}</p>
           <p>최대 기간 : {{ option.paym_prd_nm }}</p>
           <p>가입 가능 최소 나이: {{ option.pnsn_entr_age_nm }}</p>
           <p>가입 가능 최대 나이: {{ option.pnsn_strt_age_nm }}</p>
           <p>매달 저축 금액 : {{ option.mon_paym_atm_nm }}</p>
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
    url: `${store.API_URL}/fin_prct/object_yearsaving_products/${fin_prdt_cd.value}`,
    headers: {
    Authorization: `Token ${store.token}`
    }
})
.then((res)=>{
    console.log(res.data)
    product.value = res.data
    axios({
    method: 'get',
    url: `${store.API_URL}/fin_prct/object_yearsaving_options/${fin_prdt_cd.value}`,
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