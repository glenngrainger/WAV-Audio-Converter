<script setup>
defineProps(["title", "summary"]);
</script>

<template>
  <h1>{{ title }}</h1>
  <p class="summary">{{ summary }}</p>
</template>

<style scoped lang="scss">
h1 {
  color: $primary;
  font-size: 2.5rem;
  font-weight: 500;
  text-align: center;
}
.summary {
  text-align: center;
  color: $primaryLight;
  padding: 0 20rem;
  line-height: 1.5;
}
</style>
