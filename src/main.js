import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import './includes/bootstrap'
import router from './routes'

Vue.use(VueRouter);

new Vue({
  el: '#app',
  template: '<App/>',
  components: { App },
  router
});