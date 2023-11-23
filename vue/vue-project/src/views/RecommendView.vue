<template>
  <div>
    <h1>금융 상품 추천 탭</h1>
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


const router = useRouter()

onMounted(() => {

  router.push({name: 'RecomFinanPrdtView'})
})


</script>

<style scoped>

</style>