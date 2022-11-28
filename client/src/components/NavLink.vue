<template>
<AppLink
  v-bind="$attrs"
  class="nav-link"
  active-class="dark active"
  inactive-class="light"
  >
  <slot />
</AppLink>
</template>

<script setup>
import AppLink from "@/components/AppLink.vue";


</script>

<style scoped>

</style>