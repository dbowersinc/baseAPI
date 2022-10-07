<script setup>
import { useFetch } from "@/components/fetch"
import CafesPreview from "../components/CafesPreview.vue";
import NavLink from "../components/NavLink.vue";

const { data, error } = useFetch( 'http://127.0.0.1:5000/')

</script>

<template>
  <div>
    <div class="hidden lg:block w-60">
      <div class="w-60 bg-white px-1 absolute">
        <h2 class="text-2xl text-gray-900">All Cafes</h2>
        <div class="flex justify-center">
          <div class="mb-3 py-3 xl:w-96">
            <div class="input-group relative flex flex-wrap items-stretch w-full mb-4">
              <input type="search" class="form-control relative flex-auto min-w-0 block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" placeholder="Search" aria-label="Search" aria-describedby="button-addon2">
              <button class="btn inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700  focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out flex items-center" type="button" id="button-addon2">
                <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="search" class="w-4" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                  <path fill="currentColor" d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z"></path>
                </svg>
              </button>
            </div>
          </div>
        </div>
        <ul class="">
          <li class="relative">
            <a class="flex items-center text-sm py-4 px-6 h-12 overflow-hidden text-gray-700 text-ellipsis whitespace-nowrap rounded hover:text-gray-900 hover:bg-gray-100 transition duration-300 ease-in-out" href="#!" data-mdb-ripple="true" data-mdb-ripple-color="dark">Sidenav link 1</a>
          </li>
          <li class="relative">
            <NavLink to="/" class="hover:bg-sky-700">Home </NavLink>
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
          <div class="mx-auto max-w-2xl px-4  sm:py-4 sm:px-6 lg:max-w-7xl lg:px-8">
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


