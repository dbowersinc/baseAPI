<template>
<div>
  <div>
    <img :src="img_url" :alt="name" class="w-full aspect-video">
    <h1>{{ name }}</h1>
  </div>
  <div>
    <p>{{ location }}</p>
    <a :href="map_url"><p>Map it</p></a>
  </div>
  <div>
    <p>Coffee is priced at {{ coffee_price }}.</p>
    <ul>
      <li v-if="has_sockets">Sockets</li>
      <li v-if="has_wifi">WiFi</li>
      <li v-if="has_toilets">Toilets</li>
    </ul>
    <p>Has {{ seats }} seats.</p>
  </div>

</div>
</template>

<script setup>
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
    'seats'
])
</script>
