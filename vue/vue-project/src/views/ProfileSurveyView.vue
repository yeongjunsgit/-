<template>
  <div>
    <h3>설문조사</h3>
    <form>
      <div>
      <label for="like_yearsaving">손해를 보더라도 높은 수익률을 기대하십니까?</label>
      <input type="checkbox" id="like_yearsaving" v-model="like_yearsaving">
      </div>
      <div>
      <label for="save_type">원하는 예적금 상품을 골라주세요.</label>
      <select v-model="save_type">
        <option disabled value="">Please select one</option>
        <option>적금</option>
        <option>예금</option>
      </select>
      </div>
      <div>
      <label for="period">원하는 기간 유형을 선택해주세요</label>
      <select v-model="period">
        <option disabled value="">Please select one</option>
        <option>단기</option>
        <option>장기</option>
      </select>
    </div>
    <div>
      <label for="need_loan">대출 상품 추천을 원하십니까?</label>
      <input type="checkbox" id="need_loan" v-model="need_loan">
    </div>
      <label for="need_loantype">원하시는 대출 옵션을 골라주세요</label>
      <select v-model="need_loantype">
        <option disabled value="">Please select one</option>
        <option>주택담보</option>
        <option>개인신용</option>
        <option>전세자금</option>
      </select>
    </form>
    {{ like_yearsaving }}
    {{save_type}}
    {{period}}
    {{need_loan}}
    {{need_loantype }}
  </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/articles'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router';
const store = useArticleStore()
const like_yearsaving = ref(null)
const save_type = ref(null)
const period = ref(null)
const need_loan = ref(null)
const need_loantype = ref(null)

// class UserSurvey(models.Model):
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