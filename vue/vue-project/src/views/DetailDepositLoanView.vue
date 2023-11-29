<template>
    <div>
        <br>
        <div v-if="product" class="border">
            <h1 class="fw-bold mt-3 ms-2">{{ product.fin_prdt_nm }}</h1>
            <hr>
            <h5 class="fw-bold ms-2"><strong>금융회사 : </strong> {{ product.kor_co_nm }}</h5>
            <p class="ms-2"><strong>중도상환 수수료 : </strong>{{ product.erly_rpay_fee }}</p>
            <p class="ms-2"><strong>연체 이자율 : </strong>{{ product.dly_rate }}</p>
            <p class="ms-2"><strong>대출 한도 : </strong>{{ product.loan_lmt }}</p>
            <p class="ms-2"><strong>대출 부대비용 : </strong>{{ product.loan_inci_expn }}</p>
            <p class="ms-2"><strong>가입 방법 : </strong>{{ product.join_way }}</p>
        </div>
        <br>
        <h2 class="fw-bold">옵션들</h2>
        <div v-if="options">
            <div class="card my-3" v-for="option in options">
                <br>
                <p class="ms-2"><strong>대출 상환 유형명 : </strong>{{ option.rpay_type_nm }}</p>
                <br>
                <p class="ms-2"><strong>대출 금리 유형명 : </strong>{{ option.lend_rate_type_nm }}</p>
                <br>
                <p class="ms-2"><strong>최저 대출 금리 [소수점 2자리] : </strong>{{ option.lend_rate_min }}</p>
                <br>
                <p class="ms-2"><strong>대출금리_최고 [소수점 2자리] : </strong>{{ option.lend_rate_max }}</p>
                <br>
                <p class="ms-2"><strong>전월 취급 평균금리 [소수점 2자리] : </strong>{{ option.lend_rate_avg }}</p>
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
    url: `${store.API_URL}/fin_prct/object_depositloan_products/${fin_prdt_cd.value}`,
    headers: {
    Authorization: `Token ${store.token}`
    }
})
.then((res)=>{
    console.log(res.data)
    product.value = res.data
    axios({
    method: 'get',
    url: `${store.API_URL}/fin_prct/object_depositloan_options/${fin_prdt_cd.value}`,
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