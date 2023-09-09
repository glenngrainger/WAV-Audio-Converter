<script setup>
import axios from "axios";
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
      currentlyTransfering: false,
      error: false,
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
  isTransferring.value = true;

  files.value.forEach(async (file) => {
    if (!file.converted) {
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
          fileName: file.file.name,
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
  });

  isTransferring.value = false;
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
        @initConvert="initConvert"
        :files="files"
        :isTransferring="isTransferring"
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
