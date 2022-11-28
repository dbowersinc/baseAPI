<script setup>
import { RouterLink, RouterView } from "vue-router";
import NavLink from "./components/NavLink.vue";
import Header from "./components/Header.vue";
</script>

<template>
  <div>
    <div class="w-full">
      <div class="max-w-7xl mx-auto my-2">
        <Header></Header>
        </div>
    </div>
    <div class="max-w-7xl mx-auto">
    <RouterView></RouterView>
    </div>
    <footer class="max-w-7xl mx-auto">
      This is a footer
    </footer>
  </div>
</template>

<style scoped>

</style>
