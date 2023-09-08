<script setup>
const { files, isTransferring } = defineProps(["files", "isTransferring"]);
</script>

<template>
  <ul>
    <li v-for="file in files">
      <div class="file-wrap">
        <div class="file-name-wrap">
          <div class="name">{{ file.file.name }}</div>
          <div class="size">{{ file.fileSizeMb }} mb</div>
        </div>
        <font-awesome-icon icon="fa-solid fa-close" />
      </div>
    </li>
  </ul>
  <div class="btn-wrap" v-if="isTransferring">
    <button class="convert-btn currently-converting">Converting...</button>
  </div>
  <div class="btn-wrap" v-else>
    <button class="convert-btn" @click="(e) => $emit('initConvert', e)">
      Convert
    </button>
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
      padding: 2rem;
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

      svg {
        cursor: pointer;
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
  .convert-btn {
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
  }
}
</style>
