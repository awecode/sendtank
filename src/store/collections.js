export default {
  state: {},
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
      Vue.set(state, collection_name, [{objects: [], pagination: {}, pages: {}}]);
    },
    update_collection(state, [collection_name, data]) {
      let collection = state[collection_name];
      // Create collection if it doesn't exist
      if (!collection) {
        collection = Vue.set(state, collection_name, {objects: [], pagination: {}, pages: {}});
      }
      // Find current page
      let page_no = data.pagination.page.toString();
      // Update pagination
      collection.pagination = data.pagination;
      // Find ids of objects in current page
      let ids = data.results.map(obj => obj.id);
      // Remove each id from all other pages
      ids.forEach(id => {
        Object.keys(collection.pages).forEach(key => {
          let page = collection.pages[key];
          if (page.includes(id)) {
            page = page.splice(page.indexOf(id), 1);
          }
        });
      });
      // Update current page ids
      collection.pages[page_no] = ids;
    // Update/add to objects list
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
  actions: {},
};