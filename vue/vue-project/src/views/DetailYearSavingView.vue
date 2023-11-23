<template>
    <div>
        <br>
        <div v-if="product" class="border">
            <h1 class="fw-bold mt-3 ms-2">{{ product.fin_prdt_nm }}</h1>
            <hr>
            <h5 class="fw-bold ms-2">금융회사 : {{ product.kor_co_nm }}</h5>
            <p class="ms-2"><strong>판매사 : </strong>{{ product.sale_co }}</p>
            <p class="ms-2"><strong>가입 방법 : </strong>{{ product.join_way }}</p>
            <p class="ms-2"><strong>연금종류명 : </strong>{{ product.pnsn_kind_nm }}</p>
            <p class="ms-2"><strong>상품유형명 : </strong>{{ product.prdt_type_nm }}</p>
            <p class="ms-2"><strong>공시 이율 : </strong>{{ product.dcls_rate }}</p>
            <p class="ms-2"><strong>최저 보증 이율 : </strong>{{ product.guar_rate }}</p>
            <p class="ms-2"><strong>과거 수익률1 (전년도) : </strong>{{ product.btrm_prft_rate_1 }}</p>
            <p class="ms-2"><strong>과거 수익률2 (전전년도) : </strong>{{ product.btrm_prft_rate_2 }}</p>
            <p class="ms-2"><strong>과거 수익률3 (전전전년도) : </strong>{{ product.btrm_prft_rate_3 }}</p>
            <p class="ms-2"><strong>기타 사항 : </strong>{{ product.etc }}</p>
        </div>
        <br>
        <h2 class="fw-bold">옵션들</h2>
        <div v-if="options">
            <div class="card my-3" v-for="option in options">
                <br>
                <p class="ms-2"><strong>최소 기간 : </strong>{{ option.pnsn_recp_trm_nm }}</p>
                <br>
                <p class="ms-2"><strong>최대 기간 : </strong>{{ option.paym_prd_nm }}</p>
                <br>
                <p class="ms-2"><strong>가입 가능 최소 나이: </strong>{{ option.pnsn_entr_age_nm }}</p>
                <br>
                <p class="ms-2"><strong>가입 가능 최대 나이: </strong>{{ option.pnsn_strt_age_nm }}</p>
                <br>
                <p class="ms-2"><strong>매달 저축 금액 : </strong>{{ option.mon_paym_atm_nm }}</p>
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