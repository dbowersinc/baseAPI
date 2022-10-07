<script setup>

import { useFetch } from "@/components/fetch"
import CafesPreview from "../components/CafesPreview.vue";


const { data, error } = useFetch( 'http://127.0.0.1:5000/')

</script>

<template>
  <div>
    <div class="hidden lg:block w-60">
      <div class="w-60 bg-white px-1 absolute">
        <ul class="">
          <li class="relative">
            <a class="flex items-center text-sm py-4 px-6 h-12 overflow-hidden text-gray-700 text-ellipsis whitespace-nowrap rounded hover:text-gray-900 hover:bg-gray-100 transition duration-300 ease-in-out" href="#!" data-mdb-ripple="true" data-mdb-ripple-color="dark">Sidenav link 1</a>
          </li>
          <li class="relative">
            <a class="flex items-center text-sm py-4 px-6 h-12 overflow-hidden text-gray-700 text-ellipsis whitespace-nowrap rounded hover:text-gray-900 hover:bg-gray-100 transition duration-300 ease-in-out" href="#!" data-mdb-ripple="true" data-mdb-ripple-color="dark">Sidenav link 2</a>
          </li>
          <li class="relative">
            <a class="flex items-center text-sm py-4 px-6 h-12 overflow-hidden text-gray-700 text-ellipsis whitespace-nowrap rounded hover:text-gray-900 hover:bg-gray-100 transition duration-300 ease-in-out" href="#!" data-mdb-ripple="true" data-mdb-ripple-color="dark">Sidenav link 2</a>
          </li>
        </ul>
      </div>
    </div>
    <main class="lg:pl-56">
      <div v-if="error">Damn It!!: {{ error.message }}</div>
      <div v-else-if="data" class="flex-auto">
        <div class="bg-white">
          <div class="mx-auto max-w-2xl px-4 sm:py-4 sm:px-6 lg:max-w-7xl lg:px-8">
            <h2 class="text-2xl font-bold text-gray-900">Cafes</h2>
            <div class="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-3 xl:gap-x-6">
              <CafesPreview
                  v-for="cafe in data"
                  v-bind="cafe"
                  :key="cafe.id"
              />
            </div>
          </div>
        </div>
      </div>
      <div v-else>Loading...</div>

    </main>
  </div>

</template>

<style scoped>

</style>


