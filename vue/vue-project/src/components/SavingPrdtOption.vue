<template>
    <div v-if="product">

    <div class="d-flex">
    <div class="first">
        {{ product.fin_prdt_nm }}
    </div>
    <div class="others">
        <div v-if=six_month_option>
            {{six_month_option.intr_rate2}}
        </div>
        <div v-else>
            -
        </div>
    </div>
    <div class="others">
        <div v-if=one_year_option>
            {{one_year_option.intr_rate2}}
        </div>
        <div v-else>
            -
        </div>
        
    </div>
    <div class="others">
        <div v-if=two_year_option>
            {{two_year_option.intr_rate2}}
        </div>
        <div v-else>
            -
        </div>
    </div>
    <div class="others">
        <div v-if=three_year_option>
            {{three_year_option.intr_rate2}}
        </div>
        <div v-else>
            -
        </div>
    </div>
    </div>
    <hr>
    </div>
</template>

<script setup>
import { ref,onMounted } from 'vue'
import axios from 'axios'
import { useArticleStore } from '@/stores/articles'
import { useRouter } from 'vue-router';
const router = useRouter()
const store = useArticleStore()

const six_month_option = ref(null)
const one_year_option = ref(null)
const two_year_option = ref(null)
const three_year_option = ref(null)
const options = ref(null)
const props = defineProps({
    product:Object,
})

onMounted(async  ()=>{
    const store = useArticleStore()
    const type = 'saving'
    options.value = await store.tmp_options(type, props.product.fin_prdt_cd)
    
    six_month_option.value = options.value.find(option => option.save_trm === 6)
    one_year_option.value = options.value.find(option => option.save_trm === 12)
    two_year_option.value = options.value.find(option => option.save_trm === 24)
    three_year_option.value = options.value.find(option => option.save_trm === 36)
})
</script>

<style >
.first {
  flex-basis: 60%;
}

.others {
  flex-basis: 10%;
}
</style>