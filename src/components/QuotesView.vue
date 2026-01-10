<script setup lang="ts">
import { ref, onMounted } from 'vue'

const quote = ref<Quote | null>(null)
const isLoading = ref(true)
const error = ref<Error | null>(null)

interface Quote {
  content: string
  author: string
}

const fetchQuote = async () => {
  isLoading.value = true
  error.value = null
  try {
    const response = await fetch('/api/random')
    console.log('response.ok:', response.ok)
    console.log('status:', response.status)
    console.log('statusText:', response.statusText)

    if (!response.ok) {
      throw new Error('Failed to fetch a quote.')
    }
    const data = await response.json()
    quote.value = {
      content: data[0].q,
      author: data[0].a,
    }
  } catch (err: unknown) {
    if (err instanceof Error) {
      error.value = err
      console.error(err)
    } else {
      error.value = new Error(String(err))
    }
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchQuote()
})
</script>

<template>
  <div class="logic-container">
    <div class="quote-container">
      <div v-if="isLoading">Hang tight!<br />Getting you an awesome quote...</div>
      <div v-else-if="error">
        <p>Error: {{ error.message }}</p>
      </div>
      <div v-else-if="quote && quote.content">
        <p>{{ quote.content }}</p>
        <p class="quote-author">{{ quote.author }}</p>
      </div>
      <button @click="fetchQuote">Get a quote</button>
    </div>
  </div>
</template>

<style scoped>
.logic-container {
  display: flex;
  position: relative;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100%;
  justify-content: center;
  align-items: center;
}
.quote-container {
  border: 1px solid rgb(154, 207, 225);
  border-radius: 5px;
  position: absolute;
  min-height: 10rem;
  width: 50rem;
  font-size: 1.5rem;
  padding: 20px;
  box-shadow: 5px 5px 7px 0.3px black;
}
button {
  position: absolute;
  top: 14rem;
  left: 20rem;
  width: 8rem;
  height: 3rem;
  border-radius: 1000px;
  border: none;
  box-shadow: 5px 5px 7px 0.3px black;
}
button:hover {
  cursor: pointer;
}
</style>
