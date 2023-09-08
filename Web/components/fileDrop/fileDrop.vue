<script setup>
import { ref } from "vue";
import NoFilesDropZone from "./noFilesDropZone.vue";
import FilesList from "./filesList/filesList.vue";

const files = ref([]);
const isTransferring = ref(false);

function dropFileHandler(e) {
  e.preventDefault();

  let tempFilesArray = [];
  if (e.dataTransfer.items) {
    [...e.dataTransfer.items].forEach((item) => {
      if (item.kind === "file") {
        tempFilesArray.push(item.getAsFile());
      }
    });
  } else {
    tempFilesArray.push([...e.dataTransfer.files]);
  }

  if (!validateFileSize(tempFilesArray)) {
    console.log("File too large");
  }

  tempFilesArray.forEach((file) =>
    files.value.push({
      file,
      converted: false,
      fileSizeMb: Math.round(getFileSize(file) / 1000),
    })
  );
}

function validateFileSize(files) {
  return files.every((file) => {
    return getFileSize(file) <= 50000;
  });
}

function initConvert(e) {
  e.preventDefault();
  isTransferring.value = true;

  setTimeout(() => (isTransferring.value = false), 2000);
}

function getFileSize(file) {
  return file.size / 1024;
}

function dragOverHandler(e) {
  e.preventDefault();
}
</script>

<template>
  <Transition name="fade">
    <div v-if="files.length == 0">
      <NoFilesDropZone
        @dragOverHandler="dragOverHandler"
        @dropFileHandler="dropFileHandler"
      />
    </div>
    <div v-else>
      <FilesList
        :files="files"
        :isTransferring="isTransferring"
        @initConvert="initConvert"
      />
    </div>
  </Transition>
  <p class="wav-message">Only WAV files currently supported. Max 50mb.</p>
</template>

<style scoped lang="scss">
.wav-message {
  color: $primaryLight;
}

// TODO
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
