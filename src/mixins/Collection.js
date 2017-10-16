export default {
  created() {
    let endpoint = this.$options.endpoint;
    // this.$store.commit('create_collection', this.$options.collection_name);
    if (this.$store.state[this.$options.collection_name]) {
      this.$store.commit('blocking', false);
    } else {
      this.$store.commit('blocking', true);
    }
    global.axios.get(endpoint).then(({data}) => {
        this.$store.commit('update_collection', [this.$options.collection_name, data]);
        this.$store.commit('blocking', false);
      }
    );
    // }
  },
  computed: {
    data() {
      return this.$store.state[this.$options.collection_name];
    }
  }
}