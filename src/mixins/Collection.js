export default {
  created() {
    let endpoint = this.$options.endpoint;
    // this.$store.commit('create_collection', this.$options.collection_name);
    global.axios.get(endpoint).then(({data}) => {
        this.$store.commit('update_collection', [this.$options.collection_name, data]);
      }
    );
  },
  computed: {
    data() {
      return this.$store.state[this.$options.collection_name];
    }
  }
}