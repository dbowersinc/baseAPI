<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
import AppLink from "./components/AppLink.vue";
import NavLink from "./components/NavLink.vue";
</script>

<template>
  <nav class="navbar navbar-expand-sm navbar-dark bg-dark" aria-label="Third navbar example">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Expand at sm</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample03" aria-controls="navbarsExample03" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarsExample03">
        <NavLink to="/" class="hover:bg-sky-700">Home </NavLink>
        <NavLink to="/about" class="hover:bg-sky-700">About </NavLink>
        <NavLink to="/cafes" class="hover:bg-sky-700">Cafes </NavLink>
        <form role="search">
          <input class="form-control" type="search" placeholder="Search" aria-label="Search">
        </form>
      </div>
    </div>
  </nav>



  <RouterView></RouterView>

  <footer>
    This is a footer
  </footer>
</template>

<style scoped>

</style>
