<template>
<AppLink
  v-bind="$attrs"
  class="nav-link"
  active-class="nav-link active"
  inactive-class="nav-link"
  >
  <slot />
</AppLink>
</template>

<script setup>
import AppLink from "@/components/AppLink";


</script>

<style scoped>

</style>