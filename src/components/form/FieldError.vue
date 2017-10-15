<template>
    <span class="text-danger" v-if="error">{{error}}</span>
</template>

<script>
  export default {
    props: ['error']
  }
</script>