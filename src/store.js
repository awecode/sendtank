import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    'blocking': false,
    'loading': false,
  },
  mutations: {
    loading(state, bool){
      state.loading = bool;
    },
    blocking(state, bool){
      state.blocking = bool;
    },
    create_collection(state, collection_name) {
      if (!state[collection_name]) {
        Vue.set(state, collection_name, []);
      }
    },
    update_collection(state, payload) {
      let collection_name = payload[0];
      let data = payload[1];
      Vue.set(state, collection_name, data);
    },
    update_collection_item(state, payload) {
      let collection = state[payload[0]];
      let data = payload[1];
      if (collection && data.id) {
        let index = collection.findIndex(x => x.id == data.id);
        collection[index] = data;
      }
    }
  },
  strict: process.env.NODE_ENV !== 'production'
});

export default store