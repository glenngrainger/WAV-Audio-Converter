<script setup>
import axios from "axios";
import { ref } from "vue";
import NoFilesDropZone from "./noFilesDropZone.vue";
import FilesList from "./filesList/filesList.vue";

const files = ref([]);
const isConverting = ref(false);
const convertionComplete = ref(false);

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

  let tooLarge = !validateFileSize(tempFilesArray);

  tempFilesArray.forEach((file) =>
    files.value.push({
      file,
      converted: false,
      currentlyTransfering: false,
      error: tooLarge,
      errorMessage: tooLarge ? "Too large" : "",
      download: undefined,
      fileSizeMb: Math.round(getFileSize(file) / 1000),
    })
  );
}

function validateFileSize(files) {
  return files.every((file) => {
    return getFileSize(file) <= 50000;
  });
}

async function initConvert(e) {
  e.preventDefault();
  isConverting.value = true;

  let promises = [];

  files.value.forEach(async (file) => {
    promises.push(
      new Promise(async (resolve, reject) => {
        if (!file.converted && !file.error) {
          file.currentlyTransfering = true;
          try {
            let formData = new FormData();
            formData.append("file", file.file);

            let resp = await axios.post("/", formData, {
              headers: { "Content-Type": "multipart/form-data" },
              responseType: "blob",
            });

            file.download = {
              blob: await resp.data,
              fileName: file.file.name.replace(".wav", ".mp3"),
            };

            if (resp.status === 200) {
              file.converted = true;
            } else {
              file.error = true;
            }
          } catch (err) {
            file.error = true;
          }

          file.currentlyTransfering = false;
        }
        resolve();
      })
    );
  });

  Promise.all(promises).then(() => {
    isConverting.value = false;
    convertionComplete.value = true;
  });
}

function getFileSize(file) {
  return file.size / 1024;
}

function dragOverHandler(e) {
  e.preventDefault();
}

function removeFileHandler(fileToRemove) {
  files.value = files.value.filter((file) => file.file !== fileToRemove.file);
}

function finishHandler() {
  convertionComplete.value = false;
  isConverting.value = false;
  files.value = [];
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
        @initConvert="initConvert"
        @finishHandler="finishHandler"
        @removeFileHandler="removeFileHandler"
        :files="files"
        :isConverting="isConverting"
        :convertionComplete="convertionComplete"
      />
    </div>
  </Transition>
  <p class="wav-message">Only WAV files currently supported. Max 50mb.</p>
</template>

<style scoped lang="scss">
.wav-message {
  color: $primaryLight;
}

.fade-enter-active {
  transition: opacity 0.5s ease;
}
.fade-leave-active {
  display: none;
}

.fade-enter-from {
  opacity: 0;
}
.fade-leave-to {
  opacity: 0;
}
</style>
