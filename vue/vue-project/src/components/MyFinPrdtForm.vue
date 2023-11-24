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


      <div class="my-5" v-if="isSearch">
      <span >검색결과</span>
      <div class="mt-3" v-if="filteredprdt">
          
          <ul>
            <li class="dropdown-item" v-for="prdt in filteredprdt" :key="prdt.fin_prdt_cd">
   
              <div  style="height: 40px;" @click="addPrdt(prdt)">
              {{ prdt.fin_prdt_nm }}
              </div>
              
            </li>
          </ul>
          
        </div>
        <span v-else>
          없음
        </span>

      </div>
      <h5 class="my-3"><strong>선택한 금융상품</strong></h5>


      
      <div class="mb-3 d-flex flex-wrap">
        <div v-for="prdt in prdtsList" :key="prdt.id" class="col-3 mb-3">
          <div style="height: 130px;" class="card">
            <div class="card-body">
              <p class="card-text">{{ prdt.fin_prdt_nm }}</p>
              <a href="#" class="btn btn-danger" @click="deletePrdt(prdt)">삭제하기</a>
            </div>
          </div>
        </div>
      </div>
    <form @submit.prevent="donePrdt">
      <input class="btn btn-success" type="submit" value="금융상품 변경하기">
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
const isSearch = ref(false)

const selectPrdt = function(id){
  select.value = id

}

const searchPrdt = function(){
  isSearch.value = true
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

    filteredprdt.value  = res.data.filter((item) => item.fin_prdt_nm.includes(prdts.value))

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
  // console.log('상품을 보냅니다.')
  // console.log(prdtsList.value)
  emit('emitPrdts',prdtsList.value)
  router.push(`/profile`)
}

</script>

<style scoped>

</style>