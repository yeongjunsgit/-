<template>
  <div>
    
    <div id="carouselExample" class="carousel slide mt-5">
      <div class="carousel-inner">
        
        <div class="carousel-item active">
          <img src="@/assets/kakao.png" class="d-block w-100" alt="카카오" @click="goToExternalLink('https://www.kakaobank.com/bank-story/195')">
        </div>
        <div class="carousel-item">
          <img src="@/assets/toss.png" class="d-block w-100" alt="토스" @click="goToExternalLink('https://www.tossbank.com/product-service/savings/savings-freedom')">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>  
    <div id="carouselExample2" class="carousel slide mt-5">
      <div class="carousel-inner">
        
        <div class="carousel-item active">
          <img src="@/assets/hana.png" class="d-block w-100" alt="하나은행" @click="goToExternalLink('https://www.kebhana.com/cont/mall/mall08/mall0801/mall080102/1461831_115157.jsp')">
          
        </div>
        <div class="carousel-item">
          <img src="@/assets/loan.png" class="d-block w-100" alt="하나은행" @click="goToExternalLink('https://www.kakaobank.com/products/creditLoan')">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample2" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExample2" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>  
    
  </div>
</template>

<script setup>

</script>
<script>
export default {
  methods: {
    goToExternalLink(url) {
      // 외부 링크로 이동
      window.location.href = url;
    }
  }
}
</script>
<style scoped>

</style>