<template>
  <header>
    <div class="wrapper">
      <nav class="navbar navbar-expand-lg" style="background-color: #e3f2fd;">
        <!--  -->
      <div class="container-fluid shrink">
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0 d-flex align-item-center">

            <li class="nav-item d-flex align-items-center">
              <RouterLink :to="{name:'HomeView'}" class="nav-link boldnav">홈</RouterLink> 
            </li>
            <li class="nav-item d-flex align-items-center">
              <RouterLink :to="{name:'CommunityView'}" class="nav-link boldnav">커뮤니티</RouterLink>  
            </li>
            <li class="nav-item d-flex align-items-center">
              <RouterLink :to="{name:'ExCalculView'}" class="nav-link boldnav">환율계산기</RouterLink>  
            </li>
            <li class="nav-item d-flex align-items-center">
              <RouterLink to="/rate" class="nav-link boldnav">금융 상품</RouterLink>  
            </li>
            <li class="nav-item d-flex align-items-center">
              <RouterLink :to="{name:'ProfileView'}" class="nav-link boldnav">프로필</RouterLink>  
            </li>
            
            <li class="nav-item d-flex align-items-center">
              <RouterLink :to="{name:'NearBankView'}" class="nav-link boldnav">근처은행</RouterLink> 
            </li>
            <li v-if="!store.isLogin" class="nav-item d-flex align-items-center">
              <RouterLink :to="{name:'LoginView'}" class="nav-link boldnav">회원가입/로그인</RouterLink>
            </li>
            <li v-else class="nav-item d-flex align-items-center">
              <a class="nav-link boldnav" @click="logout">로그아웃</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
      <RouterView class="shrink"/>
    </div>
    <footer class="p-2 mt-5">
                                      
    </footer>
    <footer class="text-center text-bg-light p-2 mt-5 fixed-bottom">
      footer
    </footer>
  </header>
</template>
<script setup>

import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()

const logout = function(){
  store.logout()
  router.push(`/`)
}
</script>
<style>

@import url('https://fonts.googleapis.com/css2?family=Dongle:wght@300;400;700&display=swap');


/* 기존 스타일 유지 */
.border {
  border: 1px solid black;
}
.carosal {
  height: 300px;
}
.inblock {
  display: inline-block;
  width: 300px;
  height: 300px;
}
.shrink{
  width: 50%;
  margin-left: auto;
  margin-right: auto;
}
/* 추가된 스타일 */
.nav-link {
  text-decoration: none; /* 밑줄 제거 */
  
}
.boldnav {
  font-weight:bold;
}

.v-application {
  font-family: 'Dongle', sans-serif;
}

</style>
