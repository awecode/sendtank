export default {
  mounted() {
    if (!this.$store.state.user) {
      this.$router.push({path: '/login/'});
      this.$warning('Please login first.');
    }
  },
}