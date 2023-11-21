<template>
  <div>
    <h1>예적금</h1>
    <div>
      <nav>
        <RouterLink to="/finanprdt">정기예금</RouterLink>
        <RouterLink to="/yearsave">연금저축</RouterLink>
        <RouterLink to="/save">적금</RouterLink>
        <RouterLink to="/homeloan">주택담보</RouterLink>
        <RouterLink to="/depositloan">전세자금</RouterLink>
      </nav>
      <RouterView/>
    </div>
  </div>

</template>

<script setup>

</script>

<style scoped>

</style>