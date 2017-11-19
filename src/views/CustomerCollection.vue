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
        <ul v-if="this.data">
            <li v-for="item in this.data.results">
                <router-link :to="`/customers/update/${item.id}/`">{{ item.name }}</router-link>
            </li>
        </ul>
        <Pagination :page_data="this.data"/>
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