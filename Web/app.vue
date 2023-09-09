<template>
  <nav>
    <a class="logo"><font-awesome-icon icon="fa-solid fa-play" /></a>
    <ul>
      <li>
        <a class="selected">WAV Converter</a>
      </li>
    </ul>
  </nav>
  <div class="main-content">
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
  <!-- <div class="terms-conditions-wrap">
    <a>About</a>
    <div>|</div>
    <a>Terms and Conditions</a>
  </div> -->
</template>

<style lang="scss" scoped>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 4rem;

  .logo {
    color: $secondary;
    font-size: 2.5rem;
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
      cursor: pointer;

      &:hover {
        border-bottom: 2px solid $secondary;
      }

      &.selected {
        border-bottom: 2px solid $secondary;
      }
    }
  }
}
.main-content {
  padding: 0 6rem 4rem 6rem;
}

.terms-conditions-wrap {
  position: fixed;
  bottom: 1rem;
  right: 4rem;

  display: flex;
  align-items: center;
  gap: 1rem;

  font-size: 0.75rem;
  font-weight: 500;

  color: $primaryLight;

  a {
    padding: 0.5rem;
    border-radius: 6px;
    cursor: pointer;

    &:hover {
      background-color: $primaryExtraLight;
    }
  }
}
</style>
