<template>
    <div>
        Home
    </div>
</template>

<script>
    import LoginRequired from "../mixins/LoginRequired"

    export default{
      mixins: [LoginRequired],
      created(){
        this.$store.commit('notify', ['error', 'Failed'])
      }
    }
</script>
