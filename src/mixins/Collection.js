export default {
  data() {
    return {
      loading: true,
      post: null,
      error: null,
      data: []
    }
  },
  created() {
    // noinspection JSUnresolvedVariable
    let endpoint = this.$options.endpoint;
    // noinspection ES6ModulesDependencies
    global.axios.get(endpoint).then(({data}) => {
        this.data = data
      }
    );
  }
}