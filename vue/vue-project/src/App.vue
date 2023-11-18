<template>
  <header class="">
    <div class="wrapper">
      <nav class="navbar navbar-expand-lg bg-body-tertiary ">
        <div class="container-fluid ">
          <ul class="navbar-nav gap-3 me-auto mb-2 mb-lg-0 flex-row">
            <li class="nav-item">
              <RouterLink :to="{name:'HomeView'}" class="nav-link">홈</RouterLink>  
            </li>
            <li class="nav-item">
              <RouterLink :to="{name:'CommunityView'}" class="nav-link">커뮤니티</RouterLink>  
            </li>
            <li class="nav-item">
              <RouterLink :to="{name:'ExCalculView'}" class="nav-link">환율계산기</RouterLink>  
            </li>
            <li class="nav-item">
              <RouterLink to="/rate" class="nav-link">예적금 금리 비교 전체</RouterLink>  
            </li>
            <li class="nav-item">
              <RouterLink :to="{name:'ProfileView'}" class="nav-link">프로필</RouterLink>  
            </li>
            
            <li class="nav-item">
              <RouterLink :to="{name:'NearBankView'}" class="nav-link">근처은행</RouterLink> 
            </li>
            <li class="nav-item">
              <RouterLink :to="{name:'LoginView'}" class="nav-link">회원가입/로그인</RouterLink>
            </li>
          </ul>
        </div>
      </nav>
      <RouterView />
    </div>
  </header>
</template>

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
