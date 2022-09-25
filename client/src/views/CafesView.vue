<script setup>
import CafesList from "../components/CafesList.vue";
import { useFetch } from "@/components/fetch"


const { data, error } = useFetch( 'http://127.0.0.1:5000/random')
</script>

<template>
<main>
  <div v-if="error">Damn It!!: {{ error.message }}</div>
  <div v-else-if="data">
    <h1>Data</h1>
    <pre>{{ data }}</pre>
  </div>
  <div v-else>Loading...</div>

 <CafesList />
</main>
</template>

<style scoped>

</style>