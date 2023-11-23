<template>
  <div>
    <h3>설문조사</h3>
    <form @submit.prevent="submitSurvey">
      <div style="height: 300px;" id="carouselExample" class="carousel slide text-bg-light d-flex  text-center align-items-center">
        <div class="carousel-indicators bg-primary-subtle text-emphasis-primary">
          <button class="active" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="3" aria-label="Slide 4"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="4" aria-label="Slide 5"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="5" aria-label="Slide 6"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="6" aria-label="Slide 7"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="7" aria-label="Slide 8"></button>
        </div>



        <div class="carousel-inner">
          <div class="carousel-item active">
            <div class="m-3 form-check">
              <p>1. 손해를 보더라도 높은 수익률을 기대하십니까?</p>
              <div class="d-flex justify-content-evenly">
                <a @click="yesRisk" class="btn btn-primary">예</a>
                <a @click="noRisk" class="btn btn-outline-primary">아니요</a>
              </div>
            </div>
          </div>


          <div class="carousel-item">
            <div class="m-3 form-check">
              <p for="like_deposit">2. 예금 상품 추천을 원하십니까?</p>
              <div class="d-flex justify-content-evenly">
                <a @click="yesdeposit" class="btn btn-primary">예</a>
                <a @click="nodeposit" class="btn btn-outline-primary">아니요</a>
              </div>
            </div>
          </div>
          
          <div class="carousel-item">
            <div class="m-3 form-check">
              <p for="like_save">3. 적금 상품 추천을 원하십니까?</p>
              <div class="d-flex justify-content-evenly">
                <a @click="yessave" class="btn btn-primary">예</a>
                <a @click="nosave" class="btn btn-outline-primary">아니요</a>
              </div>
            </div>
          </div>
          
          <div class="carousel-item">
            <div class="m-3">
              <p for="period">4. 원하는 기간 유형을 선택해주세요</p>
              <div class="d-flex justify-content-evenly">
                <a @click="yesperiod" class="btn btn-primary">단기</a>
                <a @click="noperiod" class="btn btn-outline-primary">장기</a>
              </div>
            </div>
          </div>
          
          
          
          <div class="carousel-item">
            <div class="m-3 form-check">
              <p for="need_loan">5. 대출 상품 추천을 원하십니까?</p>
              
              <div class="d-flex justify-content-evenly">
                <a @click="yesloan" class="btn btn-primary">예</a>
                <a @click="noloan" class="btn btn-outline-primary">아니요</a>
              </div>
            </div>
          </div>
          
          <div class="carousel-item">
            <div class="m-3">
              <p for="need_loantype">6. 원하시는 대출 옵션을 골라주세요</p>
              <div class="d-flex justify-content-evenly">
                <a @click="houseoption" class="btn btn-primary">주택담보</a>
                <a @click="depositoption" class="btn btn-outline-primary">전세자금</a>
              </div>
              
            </div>
          </div>
          <div class="carousel-item">
            <div class="m-3">
              <input class="btn btn-primary" value="제출하기" type="submit" name="" id="">
              
            </div>
          </div>
          
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden bs-primary">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden bs-primary">Next</span>
        </button>
      </div>

    </form>
    <!-- {{ like_yearsaving }}
    {{ like_deposit }}
    {{ like_save }}
    {{ period }}
    {{ need_loan }}
    {{ need_loantype }}
    {{ like_high_limit }} -->
  </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/articles'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()

const store = useArticleStore()
const like_yearsaving = ref(false)
const like_deposit = ref(false)
const like_save = ref(false)
const period = ref('단기')
const need_loan = ref(false)
const need_loantype = ref('주택담보')
const like_high_limit = ref('높은 한도')



const yesRisk = function (){
  like_yearsaving.value = true
}
const noRisk = function (){
  like_yearsaving.value = false
}
const yesdeposit = function (){
  like_deposit.value = true
}
const nodeposit = function (){
  like_deposit.value = false
}
const yessave = function (){
  like_save.value = true
}
const nosave = function (){
  like_save.value = false
}
const yesperiod = function (){
  period.value = '단기'
}
const noperiod = function (){
  period.value = '장기'
}
const yesloan = function (){
  need_loan.value = true
}
const noloan = function (){
  need_loan.value = false
}

const houseoption = function (){
  need_loantype.value = "주택담보"
}
const depositoption = function (){
  need_loantype.value = "전세자금"
}




const submitSurvey = function(){
  if (like_high_limit.value == '높은 한도'){
    like_high_limit.value = true
  } else {
    like_high_limit.value = false
  }
  
  const surveyInfo = {
    user:store.mypk,
    like_yearsaving : like_yearsaving.value,
    like_deposit : like_deposit.value,
    like_save : like_save.value,
    period : period.value,
    need_loan : need_loan.value,
    need_loantype : need_loantype.value,
    like_high_limit : like_high_limit.value,
  }
  console.log(surveyInfo)

  axios({
    method:'post',
    url:`${store.API_URL}/accounts/survey/`,
    data:surveyInfo,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res)=>{
    console.log(res.data)
    store.doSurvey = true
    router.push('/profile')
    
  })
  .catch((err)=>{
    console.log(err)
  })

}
// data: {  
//       user:store.mypk,
//       user_age:store.myage,
//       financial_products:prdt_cd_list.value.join(','),
//       product_type:type_list.value.join(',')
//     },

// class User form-checkSurvey(models.Model):
    // # 연금저축
    // like_yearsaving = models.BooleanField(null=True)
    // # 적금
    // like_save = models.BooleanField(null=True)
    // # 예금
    // like_deposit = models.BooleanField(null=True)
    // # 장기추구, 단기 추구
    // period = models.CharField(max_length=30,null=True)
    // # 대출필요?
    // need_loan = models.BooleanField(null=True)
    // # 대출 필요할때 주택담보/ 개인신용/ 전세자금
    // need_loantype = models.CharField(max_length=30,null=True)
    // # 한도? vs 최저금리
    // like_high_limit = models.BooleanField(null=True)

    
</script>

<style scoped>

</style>