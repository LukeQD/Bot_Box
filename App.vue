<template>
  <div>
    <button @click="addGraph">Add Graph</button>
    <div class="grid">
      <iframe
        v-for="(frame, index) in iframes"
        :key="index"
        src="/graph.html"
        class="iframe-tile"
      ></iframe>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const iframes = ref([])

function addGraph() {
  iframes.value.push({})
}
</script>

<style scoped>
.grid {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.iframe-tile {
  width: 640px;
  height: 360px;
  border: none;
}
</style>
