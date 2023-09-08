<script setup>
import { ref } from "vue";
import NoFilesDropZone from "./noFilesDropZone.vue";
import FilesList from "./filesList/filesList.vue";

const files = ref([]);

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

  if (validateFileSize(tempFilesArray)) {
    files.value.push(tempFilesArray);
    console.log(files);
  } else {
    console.log("File too large");
  }
}

function validateFileSize(files) {
  return files.every((file) => {
    return file.size / 1024 <= 50000;
  });
}

function dragOverHandler(e) {
  e.preventDefault();
}
</script>

<template>
  <div v-if="files.length == 0">
    <NoFilesDropZone
      @dragOverHandler="dragOverHandler"
      @dropFileHandler="dropFileHandler"
    />
  </div>
  <div v-else>
    <FilesList :files="files" />
  </div>
  <p class="wav-message">Only WAV file currently supported. Max 50mb.</p>
</template>

<style scoped lang="scss">
.wav-message {
  color: $primaryLight;
}
</style>
