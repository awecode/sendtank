<template>
    <div>
        <h1 v-if="fields.id">Update {{fields.name}}</h1>
        <h1 v-else>Create New Customer</h1>
        <vue-form :fields="fields" :action="endpoint()">
            <template slot-scope="form">
                <div class="form-group">
                    <label class="control-label" for="full_name">Full Name</label>
                    <input type="text" v-model="fields.full_name" id="full_name" class="form-control" name="full_name"/>
                    <span class="text-danger">{{form.errors.get('full_name')}}</span>
                </div>
                <div class="form-group">
                    <label class="control-label" for="first_name">First Name</label>
                    <input type="text" v-model="fields.first_name" id="first_name" class="form-control" name="first_name"/>
                    <span class="text-danger">{{form.errors.get('first_name')}}</span>
                </div>
                <div class="form-group">
                    <label class="control-label" for="middle_name">Middle Name</label>
                    <input type="text" v-model="fields.middle_name" id="middle_name" class="form-control" name="middle_name"/>
                    <span class="text-danger">{{form.errors.get('first_name')}}</span>
                </div>
                <div class="form-group">
                    <label class="control-label" for="last_name">Last Name</label>
                    <input type="text" v-model="fields.last_name" id="last_name" class="form-control" name="last_name"/>
                    <span class="text-danger">{{form.errors.get('last_name')}}</span>
                </div>
                <div class="form-group">
                    <label class="control-label" for="email">E-mail</label>
                    <input type="text" v-model="fields.email" id="email" class="form-control" name="email"/>
                    <span class="text-danger">{{form.errors.get('email')}}</span>
                </div>
                <div class="form-group">
                    <label class="control-label" for="phone">Phone</label>
                    <input type="text" v-model="fields.phone" id="phone" class="form-control" name="phone"/>
                    <span class="text-danger">{{form.errors.get('phone')}}</span>
                </div>
            </template>
        </vue-form>
    </div>
</template>

<script>
  import Form from '../mixins/Form'
  import LoginRequired from '../mixins/LoginRequired'

  export default {
    endpoint: 'customers/',
    success_url: '/lists/',
    mixins: [Form, LoginRequired],
  }
</script>