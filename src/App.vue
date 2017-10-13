<template>
    <div>
        <nav-bar></nav-bar>
        <div class="container-fluid p-2">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
  import NavBar from './components/NavBar.vue'

  export default {
    name: 'app',
    components: {NavBar},
  }
</script>