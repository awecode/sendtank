<template>
    <div>

        <h1 v-if="fields.id">Update {{fields.name}}</h1>
        <h1 v-else>Create New List</h1>

        <vue-form :fields="fields" :action="endpoint()">
            <template scope="form">
                <input type="text" v-model="fields.name" id="name" class="form-control" name="name" required/>
                <span class="text-danger">{{form.errors.get('name')}}</span>
            </template>
        </vue-form>

    </div>
</template>

<script>
  import VueForm from '../components/form/VueForm.vue';

  export default {
    endpoint: 'lists/',
    components: {VueForm},
    data() {
      return {
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
      axios.get(this.endpoint()).then(({data}) => this.fields = data);
    }
  }
</script>