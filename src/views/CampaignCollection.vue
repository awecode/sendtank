<template>
    <div>
        <div class="row">
            <h1 class="col-8">Campaigns</h1>
            <div class="col-4 text-right">
                <router-link to="/campaigns/create/">
                    <a href="javascript:;" class="btn btn-success">Create New Campaign</a>
                </router-link>
            </div>
        </div>
        <ul v-if="this.data">
            <li v-for="item in this.data.objects">
                <router-link :to="`/campaigns/update/${item.id}/`">{{ item.name }}</router-link>
            </li>
        </ul>
    </div>
</template>

<script>
  import Collection from '../mixins/Collection'
  import LoginRequired from '../mixins/LoginRequired'

  export default {
    endpoint: 'campaigns/',
    collection_name: 'campaigns',
    mixins: [Collection, LoginRequired],
  }
</script>