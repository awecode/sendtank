<template>
    <div id="v-notifications-container">
        <div class="alert alert-dismissable alert-danger fade show" role="alert" v-for="notification in notifications">
            {{notification.message}}
            <button type="button" class="close ml-2" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
    </div>
</template>

<script>
  import {mapState, mapActions} from 'vuex'

  export default {
    computed: mapState([
      'notifications',
    ]),
  }
</script>