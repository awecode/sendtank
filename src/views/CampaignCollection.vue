<template>
    <div>
        <h1>Campaigns</h1>
        <ul>
            <li v-for="item in this.data">{{ item.name }}</li>
        </ul>
    </div>
</template>

<script>
  import Collection from '../mixins/Collection'

  export default {
    endpoint: 'campaigns/',
    mixins: [Collection],
  }
</script>