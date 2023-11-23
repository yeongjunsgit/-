<template>
  <div>
    <div ref="BankMap" style="width: 100%; height: 400px;"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

onMounted(() => {
  const script = document.createElement('script');
  script.async = true;
  script.src = 'https://dapi.kakao.com/v2/maps/sdk.js?appkey=515518f4fc322125ee5a59b92e14d7b6&autoload=false';
  document.head.appendChild(script);

  script.onload = () => {
    window.kakao.maps.load(() => {
      const container = document.getElementById('kakao-map');
      const options = {
        center: new window.kakao.maps.LatLng(37.5665, 126.9780), // 서울의 좌표
        level: 8,
      };
      const map = new window.kakao.maps.Map(container, options);
    });
  };
});
</script>