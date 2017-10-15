<template>
    <div>
        <h1>Campaigns</h1>
        <ul>
            <li v-for="item in this.data">{{ item.name }}</li>
        </ul>
    </div>
</template>

<script>
  export default {
    data() {
      return {
        loading: false,
        post: null,
        error: null,
        data: []
      }
    },
    created() {
      axios.get('/api/v1/campaigns/').then(({data}) => this.data = data);
    }
  }
</script>