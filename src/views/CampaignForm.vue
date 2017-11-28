<template>
    <div>
        <h1 v-if="fields.id">Update {{fields.name}}</h1>
        <h1 v-else-if="!loading">Create New Campaign</h1>
        <vue-form :fields="fields" :action="endpoint()">
            <template slot-scope="form">
                <div class="form-group">
                    <input type="text" v-model="fields.name" id="name" class="form-control" name="name"/>
                    <span class="text-danger">{{form.errors.get('name')}}</span>
                </div>
                <div class="form-group" v-if="lists">
                    <select v-model="fields.list">
                        <option disabled value="">Please select a list for the campaign</option>
                        <option v-for="option in lists.objects" :value="option.id">
                            {{ option.name }}
                        </option>
                    </select>
                    <span class="text-danger">{{form.errors.get('list')}}</span>
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
//    computed: mapState([
//      'lists',
//    ]),
    computed: mapState({
      lists: state => state.collections.lists,
    })
  }
</script>