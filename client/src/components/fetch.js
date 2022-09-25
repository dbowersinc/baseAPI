// fetch.js
// composable to fetch data

import { ref } from 'vue'
import axios from 'axios'

export function useFetch(url) {
  const data = ref(null)
  const error = ref(null)

  axios.get(url)
    .then((res) => (data.value = res.data))
    .catch((err) => (error.value = err))

  return { data, error }
}