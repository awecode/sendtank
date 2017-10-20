<template>
    <div>
        <h1>Login</h1>
        <vue-form :fields="fields" :action="endpoint()">
            <template slot-scope="form">
                <div class="form-group">
                    <label class="control-label" for="id_email">Email:</label>
                    <input class="form-control" v-model="fields.email" name="email" type="email" id="id_email"/>
                    <span class="text-danger">{{form.errors.get('email')}}</span>
                </div>
                <div class="form-group">
                    <label class="control-label" for="id_password">Password:</label>
                    <input class="form-control" v-model="fields.password" name="password" type="password" id="id_password"/>
                    <span class="text-danger">{{form.errors.get('password')}}</span>
                </div>
            </template>
            <div slot="submit">
                <input type="submit" class="btn btn-primary" value="Login" name="submit"/>
            </div>
        </vue-form>
    </div>
</template>

<script>
  import Form from '../mixins/Form'

  export default {
    mixins: [Form],
    endpoint: 'users/login/',
    object_name: 'user',
    success_url: '/',
    success_message: 'Logged In',
    mounted() {
      if (this.$store.state.user) {
        this.$router.push({path: this.$options.success_url});
        this.$notify.info('You are already logged in.');
      }
    }
  }
</script>