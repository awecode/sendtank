import VueRouter from 'vue-router'
import Home from './views/Home.vue'
import ListCollection from './views/ListCollection.vue'

let routes = [
  {path: '/', component: Home},
  {path: '/lists', component: ListCollection},
];

export default new VueRouter({
  routes,
  linkActiveClass: 'active',
});