<template>
  <header class="">
    <div class="wrapper">
      <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid mx-5">
        <RouterLink :to="{name:'HomeView'}" class="nav-link">홈</RouterLink> 
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0 ">

            <li class="nav-item">
              <RouterLink :to="{name:'CommunityView'}" class="nav-link">커뮤니티</RouterLink>  
            </li>
            <li class="nav-item">
              <RouterLink :to="{name:'ExCalculView'}" class="nav-link">환율계산기</RouterLink>  
            </li>
            <li class="nav-item">
              <RouterLink to="/rate" class="nav-link">금융 상품</RouterLink>  
            </li>
            <li class="nav-item">
              <RouterLink :to="{name:'ProfileView'}" class="nav-link">프로필</RouterLink>  
            </li>
            
            <li class="nav-item">
              <RouterLink :to="{name:'NearBankView'}" class="nav-link">근처은행</RouterLink> 
            </li>
            <li v-if="!store.mypk" class="nav-item">
              <RouterLink :to="{name:'LoginView'}" class="nav-link">회원가입/로그인</RouterLink>
            </li>
            <li v-else class="nav-item">
              <p class="nav-link" @click="logout">로그아웃</p>
            </li>
          </ul>
          <!-- <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form> -->
        </div>
      </div>
    </nav>
      <RouterView class="mx-5"/>
    </div>
    <footer class="text-center text-bg-light p-2 mt-5">
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

/* 추가된 스타일 */
.nav-link {
  text-decoration: none; /* 밑줄 제거 */
}

</style>
