<template>
  <h1>근처 은행 찾기</h1>
  <div id="app">
    <KakaoMap />
  </div>
</template>

<script>
import KakaoMap from "@/components/KakaoMap.vue";

export default {
  name: "App",
  components: {
    KakaoMap,
  },
};
</script>