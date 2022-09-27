<script setup>
import { reactive, ref } from "vue";

defineProps([
    'id',
    'name',
    'location',
    'img_url',
    'map_url',
    'has_sockets',
    'has_wifi',
    'has_toilets',
    'coffee_price',
])

</script>

<template>
  <div class="group relative">
    <h3 class="text-md text-gray-800">
          {{ name }}
        </h3>
    <div class="min-h-80 aspect-w-1 aspect-h-1 w-full overflow-hidden rounded-md bg-gray-200 group-hover:opacity-75 lg:aspect-none lg:h-80">
        <img :src="img_url" :alt="name" class="h-full w-full object-cover object-center lg:h-full lg:w-full" />
    </div>
    <div class="mt-4 flex justify-between">
      <div>
        <p class="text-sm font-medium text-gray-900">{{ location }}</p>
        <p v-if="has_wifi" class="mt-1 text-sm text-gray-500">WiFi</p>
        <p v-if="has_sockets" class="mt-1 text-sm text-gray-500">Sockets</p>
        <p v-if="has_toilets" class="mt-1 text-sm text-gray-500">Toilets</p>

      </div>
      <p class="text-sm font-medium text-gray-900">{{ coffee_price }} coffee</p>
    </div>
  </div>
</template>



<style scoped>

</style>