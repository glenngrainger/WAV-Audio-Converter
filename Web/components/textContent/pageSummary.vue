<script setup>
defineProps(["title", "summary"]);
</script>

<template>
  <div class="summary-container">
    <div class="summary-wrap">
      <h1>{{ title }}</h1>
      <p class="summary">{{ summary }}</p>
    </div>
  </div>
</template>

<style scoped lang="scss">
.summary-container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;

  .summary-wrap {
    width: 80%;
  }
}

h1 {
  color: $primary;
  font-size: 2.5rem;
  font-weight: 500;
  text-align: center;
}
.summary {
  text-align: center;
  color: $primaryLight;
  line-height: 1.5;
}
</style>
