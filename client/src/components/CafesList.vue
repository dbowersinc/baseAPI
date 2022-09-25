<script setup>
import { reactive, ref } from "vue";

const cafe = ref({ text: 'This is a test of the msg text system. Is this thing on?'})
const count = ref(0)

function increment() {
  count.value++
}
function changeMsg() {
  cafe.value.text = 'Testing.'
  count.value++
}

</script>

<template>
Cafes this is a test.
  <p>{{ cafe.text }}</p>
  <button @click="changeMsg">Change Text</button>

  <p>{{ count }}</p>
  <button @click="increment">Inc</button>
</template>



<style scoped>

</style>