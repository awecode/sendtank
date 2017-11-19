<template>
    <div>
        <div class="row">
            <h1 class="col-8">Customers</h1>
            <div class="col-4 text-right">
                <router-link to="/customers/create/">
                    <a href="javascript:;" class="btn btn-success">Create New Customer</a>
                </router-link>
            </div>
        </div>
        <ul>
            <li v-for="item in this.data">
                <router-link :to="`/customers/update/${item.id}/`">{{ item.name }}</router-link>
            </li>
        </ul>
    </div>
</template>

<script>
  import Collection from '../mixins/Collection'
  import LoginRequired from '../mixins/LoginRequired'

  export default {
    endpoint: 'customers/',
    collection_name: 'customers',
    mixins: [Collection, LoginRequired],
  }
</script>