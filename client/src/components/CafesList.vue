<script setup>
import { reactive, ref } from "vue";

const msg = ref({ text: 'This is a test of the msg text system. Is this thing on?'})

function changeMsg() {
  msg.text = 'And now this.'
}

</script>

<template>
Cafes this is a test.
  <p>{{ msg.text }}</p>
  <button @click="changeMsg">Change Text</button>
</template>



<style scoped>

</style>