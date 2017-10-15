import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import './includes/bootstrap'
import router from './routes'
import axios from 'axios';

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
window.axios = axios;

Vue.use(VueRouter);


new Vue({
  el: '#app',
  template: '<App/>',
  components: { App },
  router
});