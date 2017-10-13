import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import './includes/bootstrap'
import router from './routes'
import axios from 'axios';

window.axios = axios;

Vue.use(VueRouter);


new Vue({
  el: '#app',
  template: '<App/>',
  components: { App },
  router
});