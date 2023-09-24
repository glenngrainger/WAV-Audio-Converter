<script setup>
import { ref } from "vue";
const isDragOver = ref(false);

function dragOverHandler(e) {
  e.preventDefault();
  isDragOver.value = true;
  $emit("dragOverHandler", e);
}
</script>

<template>
  <div
    class="file-drop-area"
    :class="{ dragover: isDragOver }"
    @drop="(e) => $emit('dropFileHandler', e)"
    @dragover="(e) => dragOverHandler(e)"
    @dragleave="(e) => (isDragOver = false)"
  >
    <div class="drop-text-wrap">
      <div class="icon-wrap">
        <font-awesome-icon icon="fa-solid fa-cloud-arrow-up" />
      </div>
      <p>Drop your files here</p>
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
    font-weight: 500;
    color: $secondary;
    .icon-wrap {
      text-align: center;
      .fa-cloud-arrow-up {
        font-size: 3rem;
        transition: font-size 0.25s ease-in-out;
      }
    }

    p {
      font-size: 1.25rem;
      margin-top: 1.5rem;
      transition: font-size 0.25s ease-in-out;
    }
  }

  &:hover,
  &.dragover {
    background-color: $primaryVeryLight;

    .drop-text-wrap {
      .fa-cloud-arrow-up {
        font-size: 4rem;
      }

      p {
        font-size: 1.6rem;
      }
    }
  }
}
</style>
