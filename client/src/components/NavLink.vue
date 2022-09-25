<template>
<AppLink
  v-bind="$attrs"
  class="nav-link"
  active-class="bg-yellow-300 active"
  inactive-class="bg-green-300"
  >
  <slot />
</AppLink>
</template>

<script setup>
import AppLink from "@/components/AppLink.vue";


</script>

<style scoped>

</style>