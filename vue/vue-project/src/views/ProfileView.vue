<template>
  <div>
    <div class="m-3" v-if="mydata">
      <div class="d-flex justify-content-between">
        <h3 class="mb-4"><strong>{{mydata.nickname}}</strong>님의 페이지</h3>
        <button class="btn btn-primary" @click="gotoProfileChange"> 내 정보 변경하기 > </button>
      </div>
      <div class="d-flex">
      <img class="round" src="@/assets/myimage.png" alt="">
      <div>
      
      <p>아이디 : {{mydata.username}}</p>
      <p>내 나이 : {{ mydata.age }}세</p>
      <p v-if="mydata.money">내 자산 : {{ mydata.money }}원</p>
      </div>
    </div>

      <div v-if="mydata.financial_products">
        <h4><strong>내 금융 상품  </strong></h4>
        <div v-for="findata in mydata.financial_products.split(',')">
          <!-- {{ findata }} -->
        <ProfileMyPrdt
        :findata="findata"
        />
      </div>
    </div>
      
    <div>

        <div class="d-flex justify-content-evenly">
        <button class="btn btn-primary" @click="gotoFinDetail"> 금융상품 변경하기 > </button>
        <button class="btn btn-info text-white" @click="gotoSurvey"> 금융상품 취향 설문조사  > </button>
        </div>  


        <ul class="nav nav-tabs my-3" id="myTab" role="tablist">
          <li class="nav-item" role="presentation">
            <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">
              
              <RouterLink class="deco" :to="{name:'ProfileAgeRecomView',params:{ age: mydata.age }}">나이별 추천상품</RouterLink>
            </button>
            
          </li>
          <li class="nav-item" role="presentation">
            <button class="nav-link" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">
              <RouterLink class="deco" v-if="store.doSurvey" :to="{name:'ProfileSurveyRecomView'}">설문조사별 추천상품</RouterLink> 
            </button>
            </li>
        </ul>
        <nav>

          
          
        </nav>
        <RouterView/>
        
        
      </div>
    </div>

  </div>
</template>

<script setup>
import ProfileMyPrdt from '@/components/ProfileMyPrdt.vue'
// /agerecommend
import { useArticleStore } from '@/stores/articles'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'


const store = useArticleStore()




// 0. 나의 데이터 가져오기
const mydata = ref(null)
const router = useRouter()
const gotoFinDetail = function(){
  router.push(`/profile/${store.myname}/${store.mypk}`)
}

const gotoSurvey = function(){
  router.push(`/profile/${store.myname}/survey`)
}

const gotoProfileChange = function () {
  router.push(`/profile/${store.myname}/change`)
}

onMounted(() => {
  const store = useArticleStore()
  // console.log('토큰',store.token)
  // console.log('이름',store.myname)
  
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/user-detail/${store.myname}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res)=>{
    console.log(res.data)
    mydata.value = res.data
    console.log(mydata.value)
    // console.log('저장한 내 이름',store.myname)
    // mydata.value = res.data.filter((user) => user.username === store.myname)
    // console.log(mydata.value[0].financial_products)
    
    
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

.round{
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-left: 20px;
  margin-right: 20px;
}
.deco {
  text-decoration: none;
  color: black;
}
</style>