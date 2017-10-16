<template>
    <div>
        <nav-bar></nav-bar>
        <div v-if="loading" class="loader">
            <div class='inner'></div>
        </div>
        <div class="container-fluid p-2">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
  import NavBar from './components/NavBar.vue'
  import Vue from 'vue'
  import axios from 'axios'

  export default {
    name: 'app',
    components: {NavBar},
    data() {
      return {
        loading: false
      }
    },
    created() {

      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      axios.defaults.xsrfCookieName = "csrftoken";
      axios.defaults.baseURL = '/api/v1/';

      axios.interceptors.request.use((config) => {
        this.loading = true;
        return config;
      }, (error) => {
        this.loading = false;
        alert(error);
        return Promise.reject(error);
      });

      axios.interceptors.response.use((response) => {
        this.loading = false;
        return response;
      }, (error) => {
        this.loading = false;
        return Promise.reject(error);
      });
      global.axios = axios;

      global.Vue = Vue;

      global.bus = new Vue();
      global.bus.$on('loading', () => {
        this.loading = true;
      });
      global.bus.$on('loaded', () => {
        this.loading = false;
      });
    }
  }

</script>