<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink :to="{name:'HomeView'}">홈</RouterLink> | 
        <RouterLink :to="{name:'CommunityView'}">커뮤니티</RouterLink> | 
        <RouterLink :to="{name:'ExCalculView'}">환율계산기</RouterLink> | 
        <RouterLink to="/rate">예적금 금리 비교 전체</RouterLink> | 
        <RouterLink :to="{name:'ProfileView'}">프로필</RouterLink> | 
        <RouterLink :to="{name:'SignUpView'}">회원가입</RouterLink> | 
        <RouterLink :to="{name:'NearBankView'}">근처은행</RouterLink>
      
      </nav>
      <RouterView />
    </div>
  </header>

</template>

<style scoped>
</style>