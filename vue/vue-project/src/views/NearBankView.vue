<template>
  <div>
    <h1>지도</h1>
    <div ref="map" style="width: 100%; height: 400px;"></div>
  </div>
</template>

<script setup>
// 브라우저에서 직접 실행할 때는 Vue 컴포넌트를 전역 스코프에 등록
const MapView = {
  template: '<div ref="map" style="width: 100%; height: 400px;"></div>',
  mounted() {
    const container = this.$refs.map;
    const options = {
      center: new kakao.maps.LatLng(37.566826, 126.9786567),
      level: 3,
    };
    const map = new kakao.maps.Map(container, options);
    // 기타 맵에 필요한 작업 수행...
  },
};

// 등록된 컴포넌트를 전역 스코프에 할당
window.MapView = MapView;
</script>

<style scoped>

</style>