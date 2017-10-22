<template>
    <nav aria-label="breadcrumb" role="navigation" id="v-breadcrumbs-container">
        <ol class="breadcrumb">
            <li v-for="obj in breadcrumbs" class="breadcrumb-item">
                {{obj}}
            </li>
        </ol>
    </nav>
</template>

<script>
  import {mapState, mapActions} from 'vuex'

  export default {
    computed: {
      breadcrumbs() {
        let path_splits = this.$route.path.split('/');
        let objs = [];
        global.xyz = this;
        path_splits.forEach((split, index) => {
          if (split) {
            let path = path_splits.slice(0, index + 1).join('/');
            let matched = this.$router.resolve(path).route.matched;
            if (matched.length && !matched[0].components.default.error) {
              console.log(path);
            }
            objs.push(split);
          }
        });
        return objs;

      }
    }
  }
</script>