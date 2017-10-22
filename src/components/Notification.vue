<template>
    <div id="v-notifications-container">

        <div v-for="notification in notifications">
            <transition name="fade">
                <div v-if="notification.active"
                     class="alert alert-danger" :class="notification.dismissable && 'alert-dismissable'" role="alert">
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
    computed: mapState([
      'notifications',
    ]),
  }
</script>