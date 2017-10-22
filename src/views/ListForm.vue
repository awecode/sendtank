<template>
    <div>
        <h1 v-if="fields.id">Update {{fields.name}}</h1>
        <h1 v-else>Create New List</h1>
        <vue-form :fields="fields" :action="endpoint()">
            <template slot-scope="form">
                <input type="text" v-model="fields.name" id="name" class="form-control" name="name"/>
                <span class="text-danger">{{form.errors.get('name')}}</span>
            </template>
        </vue-form>
    </div>
</template>

<script>
  import Form from '../mixins/Form'
  import LoginRequired from '../mixins/LoginRequired'

  export default {
    mixins: [Form, LoginRequired],
    endpoint: 'lists/',
    success_url: '/lists/',
    collection_name: 'lists',
  }
</script>