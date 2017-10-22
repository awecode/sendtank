<template>
    <nav aria-label="breadcrumb" role="navigation" id="v-breadcrumbs-container">
        <ol class="breadcrumb">
            <li v-for="crumb in breadcrumbs" class="breadcrumb-item">
                <router-link :to="crumb.path">{{crumb.title}}</router-link>

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
          let crumb = {};
          let path = path_splits.slice(0, index + 1).join('/') + '/';
          let matched = this.$router.resolve(path).route.matched;
          if (matched.length && !matched[0].components.default.error) {
            let component = matched[0].components.default;
            let title = component.title || split.replace('-', ' ');
            if (!isNaN(title)) {
              let obj = this.$store.getters.get_object(component.collection_name, title, component.collection_key || 'id');
              if (obj) {
                title = obj.name || obj.title || obj[component.title_field];
              }
            }
            crumb.title = title;
            crumb.path = path;
            objs.push(crumb);
          }
        });
        return objs;

      }
    }
  }
</script>