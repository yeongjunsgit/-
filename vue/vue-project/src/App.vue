<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink :to="{name:'HomeView'}">Home</RouterLink> | 
        <RouterLink :to="{name:'CommunityView'}">CommunityView</RouterLink> | 
        <RouterLink :to="{name:'ExCalculView'}">ExCalculView</RouterLink> | 
        <RouterLink to="/rate">DepositeSavingRateView</RouterLink> | 
        <RouterLink :to="{name:'ProfileView'}">ProfileView</RouterLink> | 
        <RouterLink :to="{name:'SignInView'}">SignInView</RouterLink> | 
        <RouterLink :to="{name:'NearBankView'}">NearBankView</RouterLink>
      
      </nav>
      <RouterView />
    </div>
  </header>

</template>

<style scoped>
</style>