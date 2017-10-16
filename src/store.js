import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {},
  mutations: {
    create_collection(state, collection_name) {
      if (!state[collection_name]) {
        Vue.set(state, collection_name, []);
      }
    },
    update_collection(state, payload) {
      let collection_name = payload[0];
      let data = payload[1];
      Vue.set(state, collection_name, data);
      // state[collection_name] = data;
    }
  },
  strict: process.env.NODE_ENV !== 'production'
});

export default store