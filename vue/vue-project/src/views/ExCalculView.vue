<template>
  <div>
    <h1>환율계산기</h1>
    <p v-if="datas">
    <select v-model="country">
      <option disabled value="">Please select one</option>
      <option>미국 달러</option>
      <option>유로</option>
      <option>위안화</option>
    </select>
    <input v-model="koreaMoney" type="text" name="" id="">
  </p>
  <div v-if="country=='미국 달러'">
  <div v-if="USAData">{{USAData}}
  <!-- <p>전신환(송금) 받으실때	: {{ Number(koreaMoney) }}</p>
  <p>전신환(송금) 보내실때	: {{ Number(koreaMoney) }}</p>
  <p>매매 기준율	: {{ Number(koreaMoney) }}</p>
  <p>10일환가료율	: {{ Number(koreaMoney) }}</p>
  <p>서울외국환중개매매기준율	: {{ Number(koreaMoney) }}</p> -->
  <p>서울외국환중개장부가격	: {{ Number(koreaMoney)*USAData.kftc_bkpr }}</p>
  </div>

  </div>
  <div v-else-if="country=='위안화'">
  <div v-if="ChinaData">{{ChinaData}}</div>
  </div>
  <div v-else-if="country=='유로'">
  <div v-if="EuroData">{{EuroData}}</div>
  </div>


  </div>
</template>

<script setup>
import axios from 'axios';
import {useArticleStore} from '@/stores/articles'
import { ref,computed,onMounted } from 'vue';
const koreaMoney = ref(null)
const country = ref('미국 달러')
const datas = ref(null)
const USAData = ref(null)
const ChinaData = ref(null)
const KoreaData = ref(null)
const EuroData = ref(null)
onMounted(()=>{
  const store = useArticleStore()
  axios({
    method:'get',
    url:`${store.API_URL}/exchangerate/get_data/`
  })
  .then((res)=>{
    datas.value=res.data.data
    console.log(datas.value)
    datas.value.forEach(data => {
      // console.log(data)
      if (data.cur_nm =='미국 달러'){
        USAData.value = data
        console.log(USAData.value.kftc_bkpr)
        USAData.value.kftc_bkpr = Number(USAData.value.kftc_bkpr.split(',').join(""))
        console.log(USAData.value.kftc_bkpr)
      } else if (data.cur_nm =='위안화'){
        ChinaData.value = data
      } else if (data.cur_nm =='유로'){
        EuroData.value = data
      }
       else if (data.cur_nm =='한국 원'){
        KoreaData.value = data
      }
    });
    
  })
  .catch((err)=>{
    console.log(err)
  })
  
})

// watch(()=>{

// })
// const exchangerateData = computed(()=>{
//     return data.value.data.filter((item)=>item.CUR_NM=country.value)
// })


// [{'result': 1, 'cur_unit': 'AED', 'ttb': '347.07', 'tts': '354.08', 'deal_bas_r': '350.58', 'bkpr': '350', 'yy_efee_r': '0', 'ten_dd
// _efee_r': '0', 'kftc_bkpr': '350', 'kftc_deal_bas_r': '350.58', 'cur_nm': '아랍에미리트 디르함'}, {'result': 1, 'cur_unit': 'AUD', '
// ttb': '835.96', 'tts': '852.85', 'deal_bas_r': '844.41', 'bkpr': '844', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '844', 
// 'kftc_deal_bas_r': '844.41', 'cur_nm': '호주 달러'}, {'result': 1, 'cur_unit': 'BHD', 'ttb': '3,385.08', 'tts': '3,453.47', 'deal_ba
// s_r': '3,419.28', 'bkpr': '3,419', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '3,419', 'kftc_deal_bas_r': '3,419.28', 'cur
// _nm': '바레인 디나르'}, {'result': 1, 'cur_unit': 'BND', 'ttb': '952.85', 'tts': '972.1', 'deal_bas_r': '962.48', 'bkpr': '962', 'yy
// _efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '962', 'kftc_deal_bas_r': '962.48', 'cur_nm': '브루나이 달러'}, {'result': 1, 'cur
// _unit': 'CAD', 'ttb': '930.6', 'tts': '949.4', 'deal_bas_r': '940', 'bkpr': '940', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkp
// r': '940', 'kftc_deal_bas_r': '940', 'cur_nm': '캐나다 달러'}, {'result': 1, 'cur_unit': 'CHF', 'ttb': '1,443.08', 'tts': '1,472.23'
// , 'deal_bas_r': '1,457.66', 'bkpr': '1,457', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '1,457', 'kftc_deal_bas_r': '1,457
// .66', 'cur_nm': '스위스 프랑'}, {'result': 1, 'cur_unit': 'CNH', 'ttb': '178.41', 'tts': '182.02', 'deal_bas_r': '180.22', 'bkpr': '
// 180', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '180', 'kftc_deal_bas_r': '180.22', 'cur_nm': '위안화'}, {'result': 1, 'c
// ur_unit': 'DKK', 'ttb': '186.64', 'tts': '190.41', 'deal_bas_r': '188.53', 'bkpr': '188', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'k
// ftc_bkpr': '188', 'kftc_deal_bas_r': '188.53', 'cur_nm': '덴마아크 크로네'}, {'result': 1, 'cur_unit': 'EUR', 'ttb': '1,391.4', 'tts
// ': '1,419.51', 'deal_bas_r': '1,405.46', 'bkpr': '1,405', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '1,405', 'kftc_deal_b
// as_r': '1,405.46', 'cur_nm': '유로'}, {'result': 1, 'cur_unit': 'GBP', 'ttb': '1,598.82', 'tts': '1,631.11', 'deal_bas_r': '1,614.97
// ', 'bkpr': '1,614', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '1,614', 'kftc_deal_bas_r': '1,614.97', 'cur_nm': '영국 파 
// 운드'}, {'result': 1, 'cur_unit': 'HKD', 'ttb': '163.52', 'tts': '166.83', 'deal_bas_r': '165.18', 'bkpr': '165', 'yy_efee_r': '0', 
// 'ten_dd_efee_r': '0', 'kftc_bkpr': '165', 'kftc_deal_bas_r': '165.18', 'cur_nm': '홍콩 달러'}, {'result': 1, 'cur_unit': 'IDR(100)',
//  'ttb': '8.25', 'tts': '8.42', 'deal_bas_r': '8.34', 'bkpr': '8', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '8', 'kftc_de
// al_bas_r': '8.34', 'cur_nm': '인도네시아 루피아'}, {'result': 1, 'cur_unit': 'JPY(100)', 'ttb': '860.87', 'tts': '878.26', 'deal_bas
// _r': '869.57', 'bkpr': '869', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '869', 'kftc_deal_bas_r': '869.57', 'cur_nm': '일
// 본 옌'}, {'result': 1, 'cur_unit': 'KRW', 'ttb': '0', 'tts': '0', 'deal_bas_r': '1', 'bkpr': '1', 'yy_efee_r': '0', 'ten_dd_efee_r':
//  '0', 'kftc_bkpr': '1', 'kftc_deal_bas_r': '1', 'cur_nm': '한국 원'}, {'result': 1, 'cur_unit': 'KWD', 'ttb': '4,138.22', 'tts': '4,
// 221.83', 'deal_bas_r': '4,180.03', 'bkpr': '4,180', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '4,180', 'kftc_deal_bas_r':
//  '4,180.03', 'cur_nm': '쿠웨이트 디나르'}, {'result': 1, 'cur_unit': 'MYR', 'ttb': '273.98', 'tts': '279.51', 'deal_bas_r': '276.75'
// , 'bkpr': '276', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '276', 'kftc_deal_bas_r': '276.75', 'cur_nm': '말레이지아 링기
// 트'}, {'result': 1, 'cur_unit': 'NOK', 'ttb': '119.42', 'tts': '121.83', 'deal_bas_r': '120.63', 'bkpr': '120', 'yy_efee_r': '0', 't
// en_dd_efee_r': '0', 'kftc_bkpr': '120', 'kftc_deal_bas_r': '120.63', 'cur_nm': '노르웨이 크로네'}, {'result': 1, 'cur_unit': 'NZD', 
// 'ttb': '771.52', 'tts': '787.11', 'deal_bas_r': '779.32', 'bkpr': '779', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '779',
//  'kftc_deal_bas_r': '779.32', 'cur_nm': '뉴질랜드 달러'}, {'result': 1, 'cur_unit': 'SAR', 'ttb': '339.89', 'tts': '346.76', 'deal_b
// as_r': '343.33', 'bkpr': '343', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '343', 'kftc_deal_bas_r': '343.33', 'cur_nm': '
// 사우디 리얄'}, {'result': 1, 'cur_unit': 'SEK', 'ttb': '121.89', 'tts': '124.36', 'deal_bas_r': '123.13', 'bkpr': '123', 'yy_efee_r'
// : '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '123', 'kftc_deal_bas_r': '123.13', 'cur_nm': '스웨덴 크로나'}, {'result': 1, 'cur_unit': 
// 'SGD', 'ttb': '952.85', 'tts': '972.1', 'deal_bas_r': '962.48', 'bkpr': '962', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': 
// '962', 'kftc_deal_bas_r': '962.48', 'cur_nm': '싱가포르 달러'}, {'result': 1, 'cur_unit': 'THB', 'ttb': '36.24', 'tts': '36.97', 'de
// al_bas_r': '36.61', 'bkpr': '36', 'yy_efee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '36', 'kftc_deal_bas_r': '36.61', 'cur_nm': '
// 태국 바트'}, {'result': 1, 'cur_unit': 'USD', 'ttb': '1,274.82', 'tts': '1,300.57', 'deal_bas_r': '1,287.7', 'bkpr': '1,287', 'yy_ef
// ee_r': '0', 'ten_dd_efee_r': '0', 'kftc_bkpr': '1,287', 'kftc_deal_bas_r': '1,287.7', 'cur_nm': '미국 달러'}]


</script>

<style scoped>

</style>