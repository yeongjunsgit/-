<template>
  <div>
    <h3>설문조사</h3>
    <form @submit.prevent="submitSurvey">
        <div class="m-3 form-check">
        <label for="like_yearsaving">1. 손해를 보더라도 높은 수익률을 기대하십니까?</label>
        <input  class="form-check-input" type="checkbox" id="like_yearsaving" v-model="like_yearsaving">
        </div>
        <div class="m-3 form-check">
        <label for="like_deposit">2. 예금 상품 추천을 원하십니까?</label>
        <input  class="form-check-input" type="checkbox" id="like_deposit" v-model="like_deposit">
        </div>
        <div class="m-3 form-check">
        <label for="like_save">3. 적금 상품 추천을 원하십니까?</label>
        <input  class="form-check-input" type="checkbox" id="like_save" v-model="like_save">
        </div>
        <div class="m-3">
        <label for="period">4. 원하는 기간 유형을 선택해주세요</label>
        <select v-model="period">
          <option disabled value="">Please select one</option>
          <option>단기</option>
          <option>장기</option>
        </select>
      </div>
      <div class="m-3 form-check">
        <label for="need_loan">5. 대출 상품 추천을 원하십니까?</label>
        <input  class="form-check-input" type="checkbox" id="need_loan" v-model="need_loan">
      </div>
      <div class="m-3">
      <label for="need_loantype">6. 원하시는 대출 옵션을 골라주세요</label>
      <select v-model="need_loantype">
        <option disabled value="">Please select one</option>
        <option>주택담보</option>
        <!-- <option>개인신용</option> -->
        <option>전세자금</option>
      </select>
      </div>
      <div class="m-3">
        <label for="like_high_limit">7. 원하는 대출 방향이 어떤것인가요?</label >
          <select v-model="like_high_limit">
          <option disabled value="">Please select one</option>
          <option>높은 한도</option>
          <option>낮은 금리</option>
        </select>
      </div>
      <input type="submit" name="" id="">
    </form>
    {{ like_yearsaving }}
    {{ like_deposit }}
    {{ like_save }}
    {{ period }}
    {{ need_loan }}
    {{ need_loantype }}
    {{ like_high_limit }}
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