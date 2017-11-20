let roles = global._roles || [];
let role = roles.find(x => x.active === true);
let user = global._user || {};

export default {
  state: {
    'blocking': false,
    'loading': false,
    'roles': roles,
    'user': user,
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
    notify(state, obj) {
      state.notifications.push(obj)
    },
    deactivate_notification(state, index) {
      state.notifications[index - 1].active = false;
    },
    update_roles(state, roles) {
      state.roles = roles;
    },
    update_role(state, role) {
      role.active = true;
      state.role = role;
    },
    clear_user(state) {
      state.user = null;
    },

  },
  actions: {
    notify({commit, state}, [type, message, dismissable = true, time_out = true, active = true]) {
      let index = state.notifications.length + 1;
      let obj = {index, type, message, dismissable, active};
      commit('notify', obj);
      if (time_out) {
        setTimeout(function () {
          commit('deactivate_notification', index);
        }, 3000);
      }
    },
    change_role({commit, state}, role_id) {
      commit('blocking', true);
      global.axios.post('roles/switch/', {id: role_id}).then(data => {
        let roles = global.clone(state.roles);
        roles.forEach(role => {
          if (role.id === role_id) {
            role.active = true;
            commit('update_role', role);
          } else {
            role.active = false;
          }
        });
        commit('update_roles', roles);
        commit('blocking', false);
      });
    },
    logout({commit}) {
      return new Promise((resolve, reject) => {
        commit('blocking', true);
        global.axios.post('users/logout/').then(data => {
          commit('clear_user');
          commit('blocking', false);
          resolve();
        });
      });
    }
  },
};