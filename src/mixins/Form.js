import VueForm from '../components/form/VueForm.vue'

export default {
  components: {VueForm},
  data() {
    return {
      loading: true,
      fields: {
        name: ''
      }
    }
  },
  methods: {
    endpoint() {
      // noinspection JSUnresolvedVariable
      let endpoint = this.$options.endpoint;
      // noinspection ES6ModulesDependencies
      if (this.$route.params.pk) {
        endpoint += this.$route.params.pk + '/';
      }
      return endpoint
    }
  },
  created() {
    // noinspection ES6ModulesDependencies
    axios.get(this.endpoint()).then(({data}) => {
      this.fields = data
    });
  }
}