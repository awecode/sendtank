<template>
    <div id="v-notifications-container">
        <div class="alert alert-danger fade show" :class="notification.dismissable && 'alert-dismissable'"role="alert" v-for="notification in notifications">
            {{notification.message}}
            <button v-if="notification.dismissable" type="button" class="close ml-2" data-dismiss="alert" aria-label="Close">
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