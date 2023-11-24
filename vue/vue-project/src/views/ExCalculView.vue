<template>
  <div>
    <h1 class="my-3">환율계산기</h1>
    <!-- {{ country }} -->
    <select class="form-select" v-model="country">
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
    
    <div  v-if="filteredData.length">
      <h3 class="my-3">현재 환율 : {{   filteredData[0].kftc_bkpr }}</h3>
      <div class="input-group">
        
        <input class="form-control" v-model="koreaMoney" type="text" name="" id="" placeholder="한국">
        <span class="input-group-text"> 원</span>
      </div>
      <p>
        <div class="input-group mt-3">
          
          <input class="form-control" v-model="otherMoney" type="text" name="" id="" :placeholder="country.split(' ')[0]">
          <span class="input-group-text">{{ country.split(' ')[1] }}</span>
        </div>
      </p>
      
      <div>
        <h3 class="my-3"> 
        최종 금액 : {{ koreaMoney}}원
        </h3>
        <h3 class="my-3"> 
        최종 금액 : {{ otherMoney}}{{ country.split(' ')[1] }}
        </h3>
      <div class="d-flex gap-3">

        <button style="width: 130px;" class="btn btn-primary" @click="changemoney(1000)">1,000원  </button>
        <button style="width: 130px;" class="btn btn-primary" @click="changemoney(5000)">5,000원  </button>
        <button style="width: 130px;" class="btn btn-outline-primary" @click="changemoney(10000)">10,000원  </button>
        <button style="width: 130px;" class="btn btn-outline-primary" @click="changemoney(50000)">50,000원  </button>
        <button style="width: 130px;" class="btn btn-outline-secondary" @click="changemoney(100000)">100,000원  </button>
        <button style="width: 130px;" class="btn btn-outline-secondary" @click="changemoney(500000)">500,000원  </button>
      </div>
      <div class="d-flex gap-3 mt-3">
        <button style="width: 130px;" class="btn btn-primary" @click="changeforeignmoney(1)">1 {{ country.split(' ')[1] }} </button>
        <button style="width: 130px;" class="btn btn-primary" @click="changeforeignmoney(5)">5 {{ country.split(' ')[1] }}</button>
        <button style="width: 130px;" class="btn btn-outline-primary" @click="changeforeignmoney(10)">10 {{ country.split(' ')[1] }}</button>
        <button style="width: 130px;" class="btn btn-outline-primary" @click="changeforeignmoney(50)">50 {{ country.split(' ')[1] }}</button>
        <button style="width: 130px;" class="btn btn-outline-secondary" @click="changeforeignmoney(100)">100  {{ country.split(' ')[1] }}</button>
        <button style="width: 130px;" class="btn btn-outline-secondary" @click="changeforeignmoney(500)">500  {{ country.split(' ')[1] }}</button>
      </div>
        
      </div>

    </div>
    
  


  </div>
</template>

<script setup>

import {useArticleStore} from '@/stores/articles'
import { ref,computed,onMounted, watch } from 'vue';

const country = ref('')
const datas = ref(null)
const koreaMoney = ref(null)
const otherMoney = ref(null)


const koreaToForeign = computed(() => {
  // console.log(filteredData.value[0])
  return koreaMoney.value / Number(filteredData.value[0].kftc_bkpr.replace(',',''));
})

const foreignToKorea = computed(() => {
  // console.log(filteredData.value[0])
  return otherMoney.value * Number(filteredData.value[0].kftc_bkpr.replace(',',''))
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


const changeforeignmoney = function(money){
  otherMoney.value = money
}

onMounted(()=>{
  const store = useArticleStore()
  console.log('여기는 뷰')
  store.getExchangeData()  

})
const store = useArticleStore()
datas.value = store.exchangedata


const filteredData = computed(() => {
  if(datas.value === null){
    console.log('dajs')
    return []
  } else{

    return datas.value.filter((item) => item.cur_nm === country.value);
  }
})



</script>

<style scoped>

</style>