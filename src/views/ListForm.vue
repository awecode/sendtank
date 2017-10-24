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
        <div v-if="fields.customers">
            <h2>Users</h2>
            {{fields.customers.page_size}} of {{fields.customers.count}}
            <a :href="`/lists/${fields.id}/export/customers/`">Export XLS</a>
            <table class="table">
                <tr v-for="customer in fields.customers.results">
                    <td>
                        <router-link :to="`/customers/update/${customer.id}/`">
                            {{customer.name}}
                        </router-link>
                    </td>
                    <td><span class="badge badge-secondary mr-1" v-for="email in customer.email">{{email}}</span></td>
                    <td><span class="badge badge-secondary mr-1" v-for="phone in customer.phone">{{phone}}</span></td>
                </tr>
            </table>
        </div>
    </div>
</template>

<script>
  import Form from '../mixins/Form'
  import LoginRequired from '../mixins/LoginRequired'

  export default {
    endpoint: 'lists/',
    success_url: '/lists/',
    collection_name: 'lists',
    mixins: [Form, LoginRequired],
  }
</script>