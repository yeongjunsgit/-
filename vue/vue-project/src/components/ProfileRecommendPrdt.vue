<template>
  <div>
    <div class="card">
      <h5>상품 이름 : {{ data.fin_prdt_nm }}</h5>
      <p>은행명 : {{  data.kor_co_nm  }}</p>
      <p>가입자 수: {{ data.count }} </p>
      <div v-if="data.product_type === 'financial'">
        
        <p v-if="data.max_limit != null">최고 한도 : {{ data.max_limit }}</p>
        <p v-else>최고 한도 : 없음</p>
      </div>

      <div v-else-if="data.product_type === 'yearsaving'">
        <p>상품 유형명 : {{ data.prdt_type_nm }}</p>
        <p>전년도 수익률 : {{ data.btrm_prft_rate_1 }}</p>
      </div>
      <div v-else-if="data.product_type === 'saving'">
        <p v-if="data.max_limit != null">최고 한도 : {{ data.max_limit }}</p>
        <p v-else>최고 한도 : 없음</p>
      </div>
      <div v-else-if="data.product_type === 'depositloan'">
        <p>최저 금리 : {{ data.max_option }}</p>
      </div>
      <div v-else-if="data.product_type === 'homeloan'">
        <p>최저 금리 : {{ data.max_option }}</p>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  data: Object,
})

</script>

<style scoped>

</style>