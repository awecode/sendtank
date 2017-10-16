import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'

import App from './App.vue'
import './includes/bootstrap'
import './styles/main.scss'
import router from './routes'

Vue.use(VueRouter);
Vue.use(Vuex);


new Vue({
  el: '#app',
  template: '<App/>',
  components: {App},
  router
});