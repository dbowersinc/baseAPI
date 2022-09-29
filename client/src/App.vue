<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
import AppLink from "./components/AppLink.vue";
import NavLink from "./components/NavLink.vue";
</script>

<template>
  <div>
    <div class="w-full">
      <div class="max-w-7xl mx-auto">
        <div class="relative flex">
        <div class="relative flex ml-auto">
          <nav class="text-sm leading-6">
            <ul class="flex space-x-8">
              <li>
                <NavLink to="/" class="hover:bg-sky-700">Home </NavLink>
              </li>
              <li>
                <NavLink to="/about" class="hover:bg-sky-700">About </NavLink>
              </li>
              <li>
                <NavLink to="/cafes" class="hover:bg-sky-700">Cafes </NavLink>
              </li>
            </ul>
          </nav>
        </div>
        </div>
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
