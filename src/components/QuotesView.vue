<script setup>
import { ref, onMounted } from 'vue'

const quote = ref({})
const isLoading = ref(true)
const error = ref(null)

const fetchQuote = async () => {
  isLoading.value = true
  error.value = null
  try {
    const response = await fetch('https://api.quotable.io')
    if (!response.ok) {
      throw new Error('Failed to fetch a quote.')
    }
    const data = await response.json()
    quote.value = data // API returns a single quote object here.
  } catch (err) {
    error.value = err
    console.error(err)
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchQuote()
})
</script>

<template>
  <div class="quote-container">
    <div v-if="isLoading">Hang tight!<br />Getting you an awesome quote...</div>
    <div v-else-if="error">
      <p>Error: {{ error.message }}</p>
    </div>
    <div v-else-if="quote.content">
      <p>{{ quote.content }}</p>
      <p class="quote-author">{{ quote.author }}</p>
    </div>
    <button @click="fetchQuote">Get a quote</button>
  </div>
</template>
<style scoped>
.quote-container {
  border: 2px solid red;
  position: absolute;
  top: 5rem;
  left: 5rem;
  height: 5rem;
  width: 5rem;
}
</style>
