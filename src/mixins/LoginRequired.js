export default {
  mounted() {
    if (!this.$store.state.user) {
      this.$router.push({path: '/login/'});
      this.$notify.warning('Please login first.');
    }
    ;
  },

}