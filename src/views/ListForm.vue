<template>
    <div>
        <h1>Create New List</h1>
        <vue-form :fields="fields" action="/api/v1/lists/">
            <template scope="form">
                <input type="text" v-model="fields.name" id="name" class="form-control" name="name" required/>
                <!--<field-error :error="form.errors.get('name')"></field-error>-->
                <span class="text-danger">{{form.errors.get('name')}}</span>
            </template>
        </vue-form>
    </div>
</template>

<script>
  import VueForm from '../components/form/VueForm.vue';
  import FieldError from '../components/form/FieldError.vue';

  export default {
    components: {VueForm, FieldError},
    data() {
      return {
        fields: {
          name: ''
        }
      }
    }
  }
</script>