import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex);

// noinspection JSUnresolvedVariable
const store = new Vuex.Store({
  state: {
    'blocking': false,
    'loading': false,
    'roles': global._roles,
    'user': global._user,
    'role': role,
    'notifications': [],
  },
  mutations: {
    loading(state, bool) {
      state.loading = bool;
    },
    blocking(state, bool) {
      state.blocking = bool;
    },
    notify(state, [type, message]) {
      state.notifications.push({type, message})
    },
    update_object(state, [object_name, data]) {
      Vue.set(state, object_name, data);
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
    },
    update_roles(state, roles) {
      state.roles = roles;
    },

  },
  actions: {
    change_role({commit, state}, role_id) {
      commit('blocking', true);
      global.axios.post('roles/switch/', {id: role_id}).then(data => {
        let roles = global.clone(state.roles);
        roles.forEach(role => {
          role.active = role.id == role_id;
        });
        commit('update_roles', roles);
        commit('blocking', false);
      });
    }
  },
  strict: process.env.NODE_ENV !== 'production'
});

export default store