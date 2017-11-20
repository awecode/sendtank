<template>
    <div id="v-notifications-container">
        <div v-for="notification in notifications">
            <transition name="fade">
                <div v-if="notification.active" role="alert"
                     :class="['alert', notification.dismissable?'alert-dismissable':'', 'alert-'+notification.type]">
                    {{notification.message}}
                    <button v-if="notification.dismissable" type="button" class="close ml-2" data-dismiss="alert"
                            aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            </transition>
        </div>

    </div>
</template>

<script>
  import {mapState, mapActions} from 'vuex'

  export default {
    computed: mapState({
      notifications: state => state.app.notifications
    }),
  }
</script>