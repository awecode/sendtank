export default {
  methods: {
    $success: function (message) {
      this.$store.dispatch('notify', ['success', message]);
    },
    $info: function (message) {
      this.$store.dispatch('notify', ['info', message]);
    },
    $warning: function (message) {
      this.$store.dispatch('notify', ['warning', message]);
    },
    $error: function (message) {
      this.$store.dispatch('notify', ['danger', message]);
    },
  }
}