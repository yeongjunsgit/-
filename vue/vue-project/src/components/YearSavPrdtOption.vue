<template>
  <div v-if="product">

    <div class="d-flex">
    <div class="first">
        {{ product.fin_prdt_nm }}
    </div>
    <div class="others">
        <div v-if="product.prdt_type_nm">
          {{product.prdt_type_nm}}
        </div>
        <div v-else>
            -
        </div>
    </div>
    <div class="others">
        <div v-if="product.btrm_prft_rate_1">
          {{product.btrm_prft_rate_1}}%
        </div>
        <div v-else>
            -
        </div>
    </div>
    <div class="others">
        <div v-if="product.btrm_prft_rate_2">
          {{product.btrm_prft_rate_2}}%
        </div>
        <div v-else>
            -
        </div>
    </div>
    <div class="others">
        <div v-if="product.btrm_prft_rate_3">
          {{product.btrm_prft_rate_3}}%
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
  const type = 'yearsaving'
  // console.log(props.product.fin_prdt_cd)
  options.value = await store.tmp_options(type, props.product.fin_prdt_cd)
  // console.log(options)
})
</script>

<style scoped>

</style>