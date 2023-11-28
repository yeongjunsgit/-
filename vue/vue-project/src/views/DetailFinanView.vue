<template>
    <div>
        <br>
        <div v-if="product" class="border">
            <h1 class="fw-bold mt-3 ms-2">{{ product.fin_prdt_nm }}</h1>
            <hr>
            <h5 class="fw-bold ms-2"><strong>은행 : </strong>
                <span @click="gotoCompany(product.fin_co_no)">{{ product.kor_co_nm }}</span></h5>
            
            <p class="ms-2"><strong>가입 방법 : </strong>{{ product.join_way }}</p>
            <p class="ms-2"><strong>만기 후 이자율 : </strong>{{ product.mtrt_int }}</p>
            <p class="ms-2"><strong>우대조건 : </strong>{{ product.spcl_cnd }}</p>
            <p class="ms-2"><strong>가입제한 : </strong>
                <span v-if="product.join_deny == 1">제한 없음</span>
                <span v-else-if="product.join_deny == 2">서민전용</span>
                <span v-else>일부제한</span>
            </p>
            <p class="ms-2"><strong>가입 대상 : </strong>{{ product.join_member }}</p>
            <p class="ms-2"><strong>기타 유의 사항 : </strong>{{ product.etc_note }}</p>
            <p class="ms-2"><strong>최대한도 : </strong>
                <span v-if="product.max_limit">{{ product.max_limit }}원</span>
                <span v-else>없음</span>
            </p>
            
            <p class="ms-2"><strong>공시 종료일 : </strong>
                <span v-if="product.dcls_end_dat">{{ product.dcls_end_dat }}</span>
                <span v-else>미정</span>
            </p>
        </div>
        <br>
        <h2 class="fw-bold">옵션들</h2>
        <div v-if="options">
            <div class="card my-3" v-for="option in options">
                <br>
                <p class="ms-2"><strong>저축 금리 유형 : </strong>{{ option.intr_rate_type }}</p>
                <br>
                <p class="ms-2"><strong>저축 금리 유형명 : </strong>{{ option.intr_rate_type_nm }}</p>
                <br>
                <p class="ms-2"><strong>저축 금리 [소수점 2자리] : </strong>
                    <span v-if="option.intr_rate">{{ option.intr_rate }}</span>
                    <span v-else>없음</span>
                </p>
                <br>
                <p class="ms-2"><strong>저축 기간 [단위: 개월] : </strong>{{ option.save_trm }}</p>
                <br>
                <p class="ms-2"><strong>최고 우대금리 [소수점 2자리] </strong>{{ option.intr_rate2 }}</p>
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

const gotoCompany = function(code){
    console.log('회사 이동')
}
onMounted(() => {
const store = useArticleStore()
// object_financial_products
// object_financial_options
axios({
    method: 'get',
    url: `${store.API_URL}/fin_prct/object_financial_products/${fin_prdt_cd.value}`,
    headers: {
    Authorization: `Token ${store.token}`
    }
})
.then((res)=>{
    console.log(res.data)
    product.value = res.data
    axios({
    method: 'get',
    url: `${store.API_URL}/fin_prct/object_financial_options/${fin_prdt_cd.value}`,
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