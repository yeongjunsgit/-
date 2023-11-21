<template>
  <div>
    <h1>ProfileView</h1>
    <div v-if="mydata">
      {{ mydata }}
    </div>
    <p @click="gotoDetail"> 금융상품 추가하기 > </p>
  </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/articles'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router';
const store = useArticleStore()
// 0. 나의 데이터 가져오기
const mydata = ref(null)
const router = useRouter()
const gotoDetail = function(){
  console.log(store.mypk)
  router.push(`/profile/${store.mypk}`)
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
    // console.log(store.myname)
    mydata.value = res.data.filter((user) => user.username === store.myname)
    // console.log(mydata.value)
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