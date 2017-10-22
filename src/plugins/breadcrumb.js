export default {
  install(Vue, options) {

    const placeholder_id = 'v-breadcrumbs-container';
    
    Vue.component('breadcrumbs', {
      template: `<div id="${placeholder_id}"></div>`
    });
  }
};