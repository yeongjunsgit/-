<template>
  <div>
    <h1>환율계산기</h1>
    <!-- {{ country }} -->
    <select v-model="country">
      <option disabled value="">Please select one</option>
      <option>미국 달러</option>
      <option>유로</option>
      <option>위안화</option>
      <option>아랍에미리트 디르함</option>
      <option>호주 달러</option>
      <option>바레인 디나르</option>
      <option>브루나이 달러</option>
      <option>캐나다 달러</option>
      <option>스위스 프랑</option>
      <option>덴마아크 크로네</option>
      <option>영국 파운드</option>
      <option>홍콩 달러</option>
      <option>인도네시아 루피아</option>
      <option>일본 옌</option>
      <option>한국 원</option>
      <option>쿠웨이트 디나르</option>
      <option>말레이지아 링기트</option>
      <option>노르웨이 크로네</option>
      <option>뉴질랜드 달러</option>
      <option>사우디 리얄</option>
      <option>스웨덴 크로나</option>
      <option>싱가포르 달러</option>
      <option>태국 바트</option>
    </select>
    <!-- <p>{{koreaMoney}}</p> -->
    <p v-if="filteredData.length">
      <h3>현재 환율 : {{   filteredData[0].kftc_bkpr }}</h3>
      <input v-model="koreaMoney" type="text" name="" id="">
      <span> 원</span>
      <p>
        <input v-model="otherMoney" type="text" name="" id="">
        {{ country.split(' ')[1] }}
      </p>
      
      <p>{{ (koreaMoney / Number(filteredData[0].kftc_bkpr.replace(',',''))).toFixed(2)}}
        
      </p>

      <span @click="changemoney(1000)">1,000원  </span>
      <span @click="changemoney(10000)">10,000원  </span>
      <span @click="changemoney(100000)">100,000원  </span>
      <span @click="changemoney(1000000)">1,000,000원  </span>
      <!-- {{ data }} -->
    </p>
  


  </div>
</template>

<script setup>
import axios from 'axios';
import {useArticleStore} from '@/stores/articles'
import { ref,computed,onMounted, watch } from 'vue';

const country = ref('')
const datas = ref(null)
const koreaMoney = ref(null)
const otherMoney = ref(null)


const koreaToForeign = computed(() => {
  // console.log(filteredData.value[0])
  return koreaMoney.value * (Number(filteredData.value[0].kftc_bkpr.replace(',',''))).toFixed(2);
})

const foreignToKorea = computed(() => {
  // console.log(filteredData.value[0])
  return otherMoney.value / (Number(filteredData.value[0].kftc_bkpr.replace(',',''))).toFixed(2)
})

watch(koreaMoney, (newValue) => {
  otherMoney.value = koreaToForeign.value
})

watch(otherMoney, (newValue) => {
  koreaMoney.value = foreignToKorea.value
})


const changemoney = function(money){
  koreaMoney.value = money
}
onMounted(()=>{
  const store = useArticleStore()
  store.getExchangeData()  
})
const store = useArticleStore()
datas.value = store.exchangedata


const filteredData = computed(() => {
  return datas.value.filter((item) => item.cur_nm === country.value);
})



</script>

<style scoped>

</style>