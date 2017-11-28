<template>
    <div>
        <div class="row">
            <h1 class="col-8">Lists</h1>
            <div class="col-4 text-right">
                <router-link to="/lists/create/">
                    <a href="javascript:;" class="btn btn-success">Create New List</a>
                </router-link>
            </div>
        </div>
        <ul v-if="this.data">
            <li v-for="item in this.data.objects">
                <router-link :to="`/lists/update/${item.id}/`">{{ item.name }}</router-link>
            </li>
        </ul>
    </div>
</template>

<script>
  import Collection from '../mixins/Collection'
  import LoginRequired from '../mixins/LoginRequired'

  export default {
    endpoint: 'lists/',
    collection_name: 'lists',
    mixins: [Collection, LoginRequired],
  }
</script>