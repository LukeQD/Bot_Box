<template>
  <div ref="chartContainer" class="chart"></div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import uPlot from 'uplot'
import 'uplot/dist/uPlot.min.css'

const chartContainer = ref(null)
let uplot = null
let intervalId = null

const NUM_SERIES = 10
const MAX_POINTS = 1000  // keep the buffer small for performance
const UPDATE_RATE_MS = 1 // ~1000 Hz

const data = ref({
  x: [],
  ySeries: Array.from({ length: NUM_SERIES }, () => []),
})

// Function to simulate new data
function generateNewData() {
  const now = Date.now() / 1000
  const newX = now
  const newY = Array.from({ length: NUM_SERIES }, (_, i) => Math.sin(now * 2 * Math.PI * (i + 1) * 0.1) + Math.random() * 0.1)
  return { newX, newY }
}

function updateData() {
  const { newX, newY } = generateNewData()
  data.value.x.push(newX)
  if (data.value.x.length > MAX_POINTS) data.value.x.shift()

  newY.forEach((val, i) => {
    data.value.ySeries[i].push(val)
    if (data.value.ySeries[i].length > MAX_POINTS) data.value.ySeries[i].shift()
  })

  uplot.setData([
    data.value.x,
    ...data.value.ySeries,
  ])
}

onMounted(() => {
  const opts = {
    width: 600,
    height: 300,
    title: "Real-Time 10-Series Plot @ 1000Hz",
    scales: {
      x: { time: true },
      y: { auto: true },
    },
    series: [
      { label: "Time" },
      ...Array.from({ length: NUM_SERIES }, (_, i) => ({
        label: `Y${i + 1}`,
      }))
    ],
  }

  uplot = new uPlot(opts, [
    data.value.x,
    ...data.value.ySeries,
  ], chartContainer.value)

  // Start update loop
  intervalId = setInterval(updateData, UPDATE_RATE_MS)
})

onBeforeUnmount(() => {
  clearInterval(intervalId)
  uplot?.destroy()
})
</script>

<style scoped>
.chart {
  width: 100%;
  height: 100%;
}
</style>
