import VueRouter from 'vue-router'
import Home from './views/Home.vue'
import ListCollection from './views/ListCollection.vue'
import CampaignCollection from './views/CampaignCollection.vue'
import NotFound from './views/NotFound.vue'

let routes = [
  {path: '/', component: Home},
  {path: '/lists/', component: ListCollection},
  {path: '/campaigns/', component: CampaignCollection},
  { path: "*", component: NotFound }
];

export default new VueRouter({
  routes,
  mode: 'history',
  linkActiveClass: 'active',
  
});