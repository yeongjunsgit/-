<template>
  <div>
    <h1>예적금</h1>
    <div>

          <ul class="nav nav-tabs" id="myTab" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true"><RouterLink to="/finanprdt">정기예금</RouterLink></button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false"><RouterLink to="/yearsave">연금저축</RouterLink></button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact-tab-pane" type="button" role="tab" aria-controls="contact-tab-pane" aria-selected="false"><RouterLink to="/save">적금</RouterLink></button>
            </li>
   
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact-tab-pane" type="button" role="tab" aria-controls="contact-tab-pane" aria-selected="false"><RouterLink to="/save"><RouterLink to="/homeloan">주택담보</RouterLink></RouterLink></button>
            </li>
   
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact-tab-pane" type="button" role="tab" aria-controls="contact-tab-pane" aria-selected="false"><RouterLink to="/save"><RouterLink to="/depositloan">전세자금</RouterLink></RouterLink></button>
            </li>
    
          </ul>
        
      <RouterView/>
    </div>
  </div>

</template>

<script setup>
import HomeLoanOptionVue from '@/components/HomeLoanOption.vue'
import { useArticleStore } from '@/stores/articles'
import { ref, onMounted } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const products = ref(null)
const filteredData = ref(null)

onMounted(() => {
  const store = useArticleStore()
  // axios({
  //   method: 'get',
  //   url: `${store.API_URL}/fin_prct/save-financial-products/`,
  //   headers: {
  //     Authorization: `Token ${store.token}`
  //   }
  // })
  // .then((res)=>{
  //   console.log(res.data)
  //   products.value = res.data
  //   const loopCount = Math.min(res.data.length, 10); // 배열의 길이와 10 중 작은 값을 사용
  //   for (let i = 0; i < loopCount; i++) {
  //     filteredData.value.push(res.data[i])
  //   }
  //   console.log(filteredData)
  // })
  // .catch((err) => {
  //       console.log(err)
  //     })

  router.push({name: 'RecomFinanPrdtView'})
})


</script>

<style scoped>

</style>