export default {
  state: {
    'collections': {}
  },
  getters: {
    get_object: (state, getters) => (collection_name, key, key_name = 'id') => {
      let collection = state[collection_name];
      if (collection) {
        return state[collection_name].results.find(obj => obj[key_name] == key);
      }
    }
  },
  mutations: {
    create_collection(state, collection_name) {
      if (!state[collection_name]) {
        Vue.set(state, collection_name, []);
      }
    },
    update_collection(state, [collection_name, data]) {
      Vue.set(state.collections, collection_name, data);
    },
    update_collection_item(state, [collection_name, data]) {
      let collection = state[collection_name];
      if (collection && data.id) {
        // noinspection EqualityComparisonWithCoercionJS
        let index = collection.results.findIndex(x => x.id == data.id);
        collection.results[index] = data;
      }
    },
  },
  actions: {
    
  },
};