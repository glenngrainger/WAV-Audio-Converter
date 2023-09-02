<template>
  <navbar>
    <h2>Audio Converter</h2>
    <ul>
      <li>
        <a class="selected">WAV Converter</a>
      </li>
      <li>
        <a>Trim</a>
      </li>
    </ul>
  </navbar>
  <div class="main-content">
    <NuxtPage />
  </div>
</template>

<style scoped lang="scss">
navbar {
  display: flex;
  justify-content: space-between;
  padding: 0 4rem;

  h2 {
    color: $secondary;
    cursor: pointer;
  }

  ul {
    color: $primary;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 1.5rem;

    list-style-type: none;

    a {
      color: $primary;
      padding: 0.5rem 1rem;
      border-radius: 6px;
      cursor: pointer;
      transition: background-color 0.25s ease-in-out;

      &:hover {
        background-color: $primaryVeryLight;
      }

      &.selected {
        background-color: $primaryVeryLight;
      }
    }
  }
}
.main-content {
  padding: 0 6rem;
}
</style>
