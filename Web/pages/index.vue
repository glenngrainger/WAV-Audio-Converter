<script setup>
import PageSummary from "~/components/textContent/pageSummary.vue";
import FileDrop from "~/components/fileDrop/fileDrop.vue";
import axios from "axios";
axios.defaults.baseURL = "http://127.0.0.1:8000";
</script>
<template>
  <PageSummary
    title="WAV Converter"
    summary="Audio Converter converts WAV to mp3 format, helping decrease the size of large audio files. To convert files drop them in the area below or click the area to select files."
  />
  <FileDrop />
</template>
<style lang="scss" scoped></style>
