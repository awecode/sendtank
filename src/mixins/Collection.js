export default {
  data() {
    return {
      loading: true,
      post: null,
      error: null,
      // data: []
    }
  },
  created() {
    let endpoint = this.$options.endpoint;
    // this.$store.commit('create_collection', this.$options.collection_name);
    global.axios.get(endpoint).then(({data}) => {
        this.$store.commit('update_collection', [this.$options.collection_name, data]);
      }
    );
    // this.data = this.$store.state.lists;

  },
  computed: {
    data() {
      return this.$store.state[this.$options.collection_name];
    }
  }
}