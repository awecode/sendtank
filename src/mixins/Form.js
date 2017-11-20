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
  },
  computed: {
    success_message() {
      return this.$options.success_message || 'Saved';
    }
  },
  created() {
    if (this.$route.params.pk) {
      global.axios.get(this.endpoint()).then(({data}) => {
        this.fields = data;
      });
    }
    if (this.$options.dependencies) {
      this.$options.dependencies.forEach((model) => {
        global.axios.get(model.endpoint).then(({data}) => {
          this.$store.commit('update_collection', [model.collection_name, data]);
        });
      });
    }
  },
  mounted() {
    this.$on('success', (data) => {
      if (this.$options.collection_name) {
        this.$store.commit('update_collection_item', [this.$options.collection_name, data]);
      }
      if (this.$options.object_name) {
        this.$store.commit('update_object', [this.$options.object_name, data]);
      }
      if (this.$options.success_url) {
        this.$router.push({path: this.$options.success_url});
      }
      this.$store.dispatch('notify', ['success', this.success_message]);
    });
  },
}