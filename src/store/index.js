import Vuex from 'vuex'
import Vue from 'vue'

import app from './app'
import collections from './collections'

Vue.use(Vuex);

const store = new Vuex.Store({
  modules: {
    app: app,
    collections: collections,
  },
  strict: process.env.NODE_ENV !== 'production'
});

export default store