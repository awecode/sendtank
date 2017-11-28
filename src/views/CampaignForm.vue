<template>
    <div>
        <h1 v-if="fields.id">Update {{fields.name}}</h1>
        <h1 v-else-if="!loading">Create New Campaign</h1>
        <vue-form :fields="fields" :action="endpoint()">
            <template slot-scope="form">
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" v-model="fields.name" id="name" class="form-control" name="name" placeholder="Name"/>
                    <span class="text-danger">{{form.errors.get('name')}}</span>
                </div>
                <div class="form-group" v-if="lists">
                    <label for="list">List</label>
                    <select id="list" v-model="fields.list" class="form-control">
                        <option disabled value="">Please select a list for the campaign</option>
                        <option v-for="option in lists.objects" :value="option.id">
                            {{ option.name }}
                        </option>
                    </select>
                    <span class="text-danger">{{form.errors.get('list')}}</span>
                </div>
                <div class="form-group">
                    <label for="template">Template</label>
                    <textarea v-model="fields.template" id="template" class="form-control" name="template">
                    </textarea>
                    <span class="text-danger">{{form.errors.get('template')}}</span>
                </div>
            </template>
        </vue-form>
    </div>
</template>

<script>
  import Form from '../mixins/Form'
  import ListForm from '../views/ListForm.vue'
  import LoginRequired from '../mixins/LoginRequired'
  import {mapState} from 'vuex'

  export default {
    mixins: [Form, LoginRequired],
    endpoint: 'campaigns/',
    success_url: '/campaigns/',
    collection_name: 'campaigns',
    dependencies: [ListForm],
    computed: mapState({
      lists: state => state.collections.lists,
    })
  }
</script>