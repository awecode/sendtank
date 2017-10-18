<template>
    <div>
        <nav-bar :loading="loading && !blocking"></nav-bar>
        <div v-if="blocking" class="blocking loader">
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
  import {mapState} from 'vuex'

  export default {
    name: 'app',
    components: {NavBar},

    created() {

      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      axios.defaults.xsrfCookieName = "csrftoken";
      axios.defaults.baseURL = '/api/v1/';

      axios.interceptors.request.use((config) => {
        this.$store.commit('loading', true);
        return config;
      }, (error) => {
        this.$store.commit('loading', false);
        alert(error);
        return Promise.reject(error);
      });

      axios.interceptors.response.use((response) => {
        this.$store.commit('loading', false);
        return response;
      }, (error) => {
        this.$store.commit('loading', false);
        return Promise.reject(error);
      });
      global.axios = axios;

      global.clone = (obj => {
        return JSON.parse(JSON.stringify(obj))
      });

      global.Vue = Vue;

    },
    computed: mapState([
      'loading', 'blocking'
    ])
  }

</script>