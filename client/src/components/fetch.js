// fetch.js
// composable to fetch data

import { ref, isRef, unref, watchEffect } from 'vue'
import axios from 'axios'

export function useFetch(url) {
  const data = ref(null)
  const error = ref(null)

  function doFetch() {
    data.value = null
    error.value = null

    // unref() unwraps potential refs
    axios.get(unref(url))
    .then((res) => (data.value = res.data))
    .catch((err) => (error.value = err))
  }

  if (isRef(url)) {
    // setup reactive re-fetch if input URL is a ref
    watchEffect(doFetch)
  } else {
    doFetch()
  }

  return { data, error }
}