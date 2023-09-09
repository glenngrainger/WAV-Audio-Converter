<script setup>
const { files, isTransferring } = defineProps([
  "files",
  "isConverting",
  "convertionComplete",
]);

function downloadFile(fileDetails) {
  if (fileDetails.download) {
    let link = document.createElement("a");
    link.href = URL.createObjectURL(fileDetails.download.blob);
    link.download = fileDetails.download.fileName;

    document.body.append(link);

    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(link.href), 7000);
  }
}
</script>

<template>
  <div>
    <ul>
      <li v-for="file in files">
        <div class="file-wrap">
          <div class="file-name-wrap">
            <div class="name">{{ file.file.name }}</div>
            <div class="size">{{ file.fileSizeMb }} mb</div>
          </div>
          <div class="details-wrap">
            <div v-if="file.currentlyTransfering">
              <div class="loader"></div>
            </div>
            <div v-else-if="file.converted">
              <font-awesome-icon
                icon="fa-solid fa-download"
                @click="downloadFile(file)"
              />
            </div>
            <div v-else-if="file.error">
              <div class="convert-error">
                {{ file.errorMessage ? file.errorMessage : "Error" }}
              </div>
            </div>
            <div v-else>
              <font-awesome-icon icon="fa-solid fa-close" />
            </div>
          </div>
        </div>
      </li>
    </ul>
    <div class="btn-wrap" v-if="isConverting">
      <button class="action-btn currently-converting">Converting...</button>
    </div>
    <div
      class="btn-wrap"
      v-else-if="
        convertionComplete ||
        files.every((file) => file.error || file.converted)
      "
    >
      <button class="action-btn back" @click="$emit('finishHandler')">
        Finish
      </button>
    </div>
    <div class="btn-wrap" v-else>
      <button class="action-btn" @click="(e) => $emit('initConvert', e)">
        Convert
      </button>
    </div>
  </div>
</template>

<style scoped lang="scss">
ul {
  margin: 0;
  padding: 0;

  li,
  .file-wrap {
    border-radius: 12px;
  }

  li {
    border: 1px solid $primaryVeryLight;
    margin: 1rem 0;
    list-style-type: none;

    .file-wrap {
      padding: 1.5rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;

      .file-name-wrap {
        > div {
          display: inline;
        }
        .name {
          color: $primary;
          font-weight: 600;
        }

        .size {
          margin-left: 1.5rem;
          color: $primaryLight;
        }
      }

      .details-wrap {
        height: 20px;
        svg {
          cursor: pointer;
        }

        .convert-error {
          font-weight: 500;
          color: $danger;
        }
      }
    }

    transition: background-color 0.25s ease-in-out;
    :hover {
      background-color: $primaryExtraLight;
    }
  }
}

.btn-wrap {
  display: flex;
  align-items: center;
  .action-btn {
    cursor: pointer;

    font-size: 1.5rem;
    font-weight: 500;
    background-color: $secondary;
    color: $white;
    padding: 0.5rem 1rem;
    border: none;
    outline: none;
    border-radius: 6px;
    margin-left: auto;

    transition: background-color 0.25s ease-in-out;

    &:hover {
      background-color: $secondaryLight;
    }

    &.currently-converting {
      color: $primaryLight;
      background-color: $primaryVeryLight;

      &:hover {
        background-color: $primaryExtraLight;
      }
    }

    &.back {
      color: $primary;
      background-color: $primaryVeryLight;

      &:hover {
        background-color: $primaryExtraLight;
      }
    }
  }
}

.loader {
  border: 2px solid $primaryVeryLight; /* Light grey */
  border-top: 2px solid $secondary; /* Blue */
  border-radius: 50%;
  width: 16px;
  height: 16px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
