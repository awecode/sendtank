<template>
    <div>
        Home
    </div>
</template>

<script>
  import LoginRequired from "../mixins/LoginRequired"

  export default {
    title: 'Home',
    mixins: [LoginRequired],
  }
</script>
