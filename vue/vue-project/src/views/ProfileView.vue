<template>
  <div>
    <div>
      <h1>ProfileView</h1>
      키 {{ store.token }}
      <div v-if="mydata">
        <h3>{{mydata[0].nickname}}님의 페이지</h3>
        <p>아이디 : {{mydata[0].username}}</p>
        <p>내 나이 : {{ mydata[0].age }}세</p>
        <p v-if="mydata[0].money">내 자산 : {{ mydata[0].money }}원</p>
        <p v-if="mydata[0].financial_products">내 금융 상품 : {{ mydata[0].financial_products }}</p>
        <div>
          <!-- <ProfileAgeRecomViewVue
          :age="mydata[0]"
          /> -->
        </div>
        
      </div>
      <p @click="gotoDetail"> 금융상품 추가하기 > </p>
      <p @click="gotoSurvey"> 금융상품 취향 설문조사  > </p>
    </div>
  </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/articles'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import ProfileAgeRecomViewVue from '@/views/ProfileAgeRecomView.vue'
// import { useArticleStore } from '@/stores/articles'
const store = useArticleStore()
// 0. 나의 데이터 가져오기
const mydata = ref(null)
const router = useRouter()
const gotoDetail = function(){
  router.push(`/profile/${store.mypk}`)
}

const gotoSurvey = function(){
  router.push(`/profile/survey`)
}

onMounted(() => {
  const store = useArticleStore()
  // console.log('토큰',store.token)
  // console.log('이름',store.myname)
  
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/user-detail/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res)=>{
    console.log(res.data)
    console.log('저장한 내 이름',store.myname)
    mydata.value = res.data.filter((user) => user.username === store.myname)
    console.log(mydata.value[0].financial_products)
    
    
  })
  .catch((err) => {
    // console.log(store.token)
        console.log(err)
 
      })


})
// 1. 나이대에 맞는 추천상품 -> 글쓴이의 나이대를 어린이, 청년, 중장년, 노년으로 나누어서 추천 상품을 알려줌




// 1-1. 예금, 적금(단기, 장기 나눠서), 연금저축, 주택담보, 전세자금, 개인신용 탭 고르기
// 1-2. 일단 사용자의 나이 데이터 가져옴
// 1-3. 해당 상품 모델에 있는 데이터 모두 가져옴
// 1-4. 반복문을 통해서 가입조건에 해당하는 상품 추천
</script>

<style scoped>

</style>