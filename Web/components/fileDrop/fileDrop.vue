<script setup></script>

<template>
  <div class="file-drop-area">
    <div class="drop-text-wrap">
      <h3>img</h3>
      <p>Click or drop your files</p>
    </div>
  </div>
</template>

<style scoped lang="scss">
.file-drop-area {
  margin-top: 2rem;
  background-color: $primaryExtraLight;
  width: 100%;
  height: 400px;
  border-radius: 12px;
  border: 2px dashed $primaryLight;
  border-spacing: 20px;
  transition: background-color 0.25s ease-in-out;

  display: flex;
  justify-content: center;
  align-items: center;

  cursor: pointer;

  .drop-text-wrap {
    color: $secondary;
    h3 {
      text-align: center;
    }

    p {
      transition: font-size 0.25s ease-in-out;
      font-weight: 600;
    }
  }

  &:hover {
    background-color: $primaryVeryLight;

    .drop-text-wrap > p {
      font-size: 1.25rem;
    }
  }
}
</style>
