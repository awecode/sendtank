import VueRouter from 'vue-router'
import Vue from 'vue'

import Home from './views/Home.vue'
import LoginForm from './views/LoginForm.vue'
import ListCollection from './views/ListCollection.vue'
import ListForm from './views/ListForm.vue'
import CampaignCollection from './views/CampaignCollection.vue'
import NotFound from './views/NotFound.vue'

Vue.use(VueRouter);

let routes = [
  {path: '/', component: Home},
  {path: '/login/', component: LoginForm},
  {path: '/lists/', component: ListCollection},
  {path: '/lists/create/', component: ListForm},
  {path: '/lists/update/:pk', component: ListForm},
  {path: '/campaigns/', component: CampaignCollection},
  {path: "*", component: NotFound}
];

export default new VueRouter({
  routes,
  mode: 'history',
  linkActiveClass: 'active',
});