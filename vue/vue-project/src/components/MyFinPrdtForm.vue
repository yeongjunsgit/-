<template>
  <div>
  
    <div class="btn-group dropup">
    <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
      상품 종류
    </button>
    <ul class="dropdown-menu">
      <li><a @click="selectPrdt(1)" class="dropdown-item" href="#">정기예금</a></li>
      <li><a @click="selectPrdt(2)" class="dropdown-item" href="#">연금저축</a></li>
      <li><a @click="selectPrdt(3)" class="dropdown-item" href="#">적금</a></li>
      <li><a @click="selectPrdt(4)" class="dropdown-item" href="#">주택담보대출</a></li>
      <li><a @click="selectPrdt(5)" class="dropdown-item" href="#">전세자금대출</a></li>
    </ul>
  </div>
  
      <form v-if="select" @submit.prevent="searchPrdt" class="mb-3">
        <div class="input-group">
          <input
            id="prdts"
            v-model.trim="prdts"
            type="text"
            class="form-control"
            name=""
            placeholder="소장한 금융상품"
          />
          <input type="submit" class="form-control" value="검색하기" name="" id="">
        </div>
      </form>


      <span>검색결과</span>
        <div v-if="filteredprdt">
          
            <div v-for="prdt in filteredprdt">
              <div  @click="addPrdt(prdt)">{{ prdt.fin_prdt_nm }}</div>
          
          </div>
        </div>
        <span v-else>
          없음
        </span>
      <div class="card" v-for="prdt in prdtsList">
        {{ prdt.fin_prdt_nm }} <button @click="deletePrdt(prdt)">x</button>
      </div>
    <form @submit.prevent="donePrdt">
      <input  type="submit" value="완료">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import {useArticleStore} from '@/stores/articles'
import { useRouter,useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
const store = useArticleStore()
const prdtsList = ref([])
const prdts = ref(null)
const select = ref(null)
const filteredprdt = ref(null)
const type = ref(null)

const selectPrdt = function(id){
  select.value = id
  // console.log(select.value)
}

const searchPrdt = function(){
  // console.log('검색하기')
  const tmpUrl = ref(null)
  if (select.value == 1) {
    tmpUrl.value = 'list-financial-products'
    type.value = 'financial'
  } 
  else if (select.value === 2){
    tmpUrl.value = 'list-yearsaving-products'
    type.value = 'yearsaving'
  }
  else if (select.value === 3){
    tmpUrl.value = 'list-saving-products'
    type.value = 'saving'
  }
  else if (select.value === 4){
    tmpUrl.value = 'list-homeloan-products'
    type.value = 'homeloan'
  }
  else if (select.value === 5){
    tmpUrl.value = 'list-depositloan-products'
    type.value = 'depositloan'
  }
  console.log(tmpUrl.value)
  axios ({
    method: 'get',
    url: `${store.API_URL}/fin_prct/${tmpUrl.value}/`,


  })
  .then((res) => {
    // console.log('검색어',prdts.value)
    // console.log('반환 데이터',res.data)
    filteredprdt.value  = res.data.filter((item) => item.fin_prdt_nm.includes(prdts.value))
    // console.log(filteredprdt.value)
  })
  .catch((err)=> {
    console.log(err)
  })

}

const addPrdt = function(cd){
  const index = prdtsList.value.findIndex((item)=> item.fin_prdt_cd===cd.fin_prdt_cd)

  if(index != -1){
    window.alert('이미 있는 상품입니다.')
  } else {
    prdtsList.value.push(
      {
        fin_prdt_cd:cd.fin_prdt_cd,
        fin_prdt_nm:cd.fin_prdt_nm,
        type:type.value,
      }
    
    )
  }
  // console.log(prdtsList.value)
}


const deletePrdt = function (prdt){
  // console.log(prdt)
  const index = prdtsList.value.findIndex((item)=> item.fin_prdt_cd===prdt.fin_prdt_cd)

  prdtsList.value.splice(index,1)

}

const emit = defineEmits(['emitPrdts',])


const donePrdt = function (){
  console.log('상품을 보냅니다.')
  console.log(prdtsList.value)
  emit('emitPrdts',prdtsList.value)
  router.push(`/profile`)
}

</script>

<style scoped>

</style>