import VueForm from '../components/form/VueForm.vue'

export default {
  components: {VueForm},
  data() {
    return {
      loading: true,
      fields: {}
    }
  },
  methods: {
    endpoint() {
      let endpoint = this.$options.endpoint;
      if (this.$route.params.pk) {
        endpoint += this.$route.params.pk + '/';
      }
      return endpoint
    },
    log(x) {
      console.log(x);
    }
  },
  created() {
    if (this.$route.params.pk) {
      global.axios.get(this.endpoint()).then(({data}) => {
        this.fields = data;
      });
    }
  },
  mounted() {
    this.$on('success', (data) => {
      this.$store.commit('update_collection_item', [this.$options.collection_name, data]);
      this.$router.push({path: this.$options.success_url});
    });
  }
}