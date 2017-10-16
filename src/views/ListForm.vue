<template>
    <div>

        <h1 v-if="fields.id">Update {{fields.name}}</h1>
        <h1 v-else>Create New List</h1>

        <div class='loader'>
            <div class='inner'></div>
        </div>

        <vue-form :fields="fields" :action="endpoint()">
            <template scope="form">
                <input type="text" v-model="fields.name" id="name" class="form-control" name="name" required/>
                <span class="text-danger">{{form.errors.get('name')}}</span>
            </template>
        </vue-form>

    </div>
</template>

<script>
  import Form from '../mixins/Form'

  export default {
    endpoint: 'lists/',
    mixins: [Form],
  }
</script>