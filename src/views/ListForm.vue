<template>
    <div>
        <h1>Create New List</h1>
        <vue-form :fields="fields" action="lists/">
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
    components: {VueForm},
    data() {
      return {
        fields: {
          name: ''
        }
      }
    }
  }
</script>