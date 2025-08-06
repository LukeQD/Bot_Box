<template>
  <button @click="addGraph">Add Graph</button>
  <div class="grid">
    <iframe
      v-for="src in frames"
      :key="src"
      :src="src"
      frameborder="0"
    ></iframe>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const frames = ref<string[]>([])

function addGraph() {
  // timestamp to bust cache & give each iframe a unique key
  frames.value.push(`/graph.html?ts=${Date.now()}`)
}
</script>

<style scoped>
button {
  padding: .5rem 1rem;
  font-size: 1rem;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}
iframe {
  width: 100%;
  height: 250px;
  border: 1px solid #ccc;
}
</style>
