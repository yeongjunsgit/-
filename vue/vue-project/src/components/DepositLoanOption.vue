<template>
  <div v-if="product">

    <div class="d-flex">
    <div class="first">
        <h5><strong>{{ product.fin_prdt_nm }}</strong></h5>
        <div v-if="product.dly_rate">
          {{product.dly_rate}}
        </div>
        <div v-if="product.loan_lmt">
          {{product.loan_lmt}}
        </div>
    </div>
    <div class="others">
      <div v-if="options">
        {{options[0].lend_rate_min}}%
      </div>
      <div v-else>
        -
      </div>
    </div>
    <div class="others">
      <div v-if="options">
        {{options[0].lend_rate_max}}%
      </div>
      <div v-else>
        -
      </div>
    </div>
    
  </div>
  </div>
  <hr>

    
</template>

<script setup>
import { useArticleStore } from '@/stores/articles'
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue'

const router = useRouter()
const store = useArticleStore()
const props = defineProps({
  product: Object,
})
const options = ref(null)

onMounted(async () => {
  const type = 'depositloan'
  // console.log(props.product.fin_prdt_cd)
  options.value = await store.tmp_options(type, props.product.fin_prdt_cd)
  // console.log(options)
})
</script>

<style scoped>
.first {
  flex-basis: 80%;
}

.others {
  flex-basis: 10%;
}
</style>