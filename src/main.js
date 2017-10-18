import Vue from 'vue'

import App from './App.vue'
import './includes/bootstrap'
import './styles/main.scss'
import router from './routes'
import store from './store'
import Notification from './plugins/notification'

Vue.use(Notification);

new Vue({
  el: '#app',
  template: '<App/>',
  components: {App},
  router,
  store,
});