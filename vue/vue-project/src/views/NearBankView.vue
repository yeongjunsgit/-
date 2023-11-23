<template>
  <div id="app">
    <h1 class="mt-4 text-center">근처 은행 찾기</h1>
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