<script setup>

import { useFetch } from "@/components/fetch"
import CafesPreview from "../components/CafesPreview.vue";


const { data, error } = useFetch( 'http://127.0.0.1:5000/')

</script>

<template>
  <main>
    <div v-if="error">Damn It!!: {{ error.message }}</div>
    <div v-else-if="data">
      <div class="bg-white">
        <div class="mx-auto max-w-2xl py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8">
          <h2 class="text-2xl font-bold tracking-tight text-gray-900">Cafes</h2>
          <div class="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
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
</template>

<style scoped>

</style>


