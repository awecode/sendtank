<template>
    <div>
        <div class="row">
            <h1 class="col-8">Lists</h1>
            <div class="col-4 text-right">
                <router-link to="/lists/create/">
                    <a class="btn btn-success">Create New List</a>
                </router-link>
            </div>
        </div>
        <ul>
            <li v-for="item in this.data">{{ item.name }}</li>
        </ul>
    </div>
</template>

<script>
  import Collection from '../mixins/Collection'

  export default {
    endpoint: 'lists/',
    mixins: [Collection],
  }
</script>