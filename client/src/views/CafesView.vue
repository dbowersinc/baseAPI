<script setup>
import { ref } from 'vue'
import { useFetch } from "@/components/fetch"
import CafesPreview from "../components/CafesPreview.vue";
import LeftSidebar from "@/components/LeftSidebar.vue";

const baseurl = 'http://127.0.0.1:5000/'
const url = ref(baseurl)
const { data, error } = useFetch(url)

// refactor to filter the data object based on the search term.
function onSearch(term) {
  url.value = baseurl + 'search?loc=' + term + '&has_toilet=1'
}

</script>

<template>
  <div>
    <div class="hidden lg:block w-60">
      <div class="w-60 bg-white px-1 absolute">
        <LeftSidebar @search-url="onSearch"/>
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


