import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App.vue'
import './includes/bootstrap'
import './styles/main.scss'
import router from './routes'
import store from './store'

Vue.use(VueRouter);


new Vue({
  el: '#app',
  template: '<App/>',
  components: {App},
  router,
  store,
});