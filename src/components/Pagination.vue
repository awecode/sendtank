<template>
    <div id="v-pagination-container" v-if="pagination && pagination.count">
        <span class="badge badge-secondary">Showing {{ pagination.size }} of {{pagination.count}}</span>
        <span class="badge badge-secondary">Page {{pagination.page}} of {{pagination.pages}}</span>

        <nav>
            <ul class="pagination">
                <li class="page-item" v-if="pagination.previous">
                    <a class="page-link" href="#" tabindex="-1">Previous</a>
                </li>
                <li class="page-item" v-for="pg in page_links" :class="{active: pg==pagination.page}">
                    <a class="page-link" href="#">{{pg}}</a>
                </li>
                <li class="page-item" v-if="pagination.next">
                    <a class="page-link" href="#">Next</a>
                </li>
            </ul>
        </nav>

    </div>
</template>

<script>
  import {mapState, mapActions} from 'vuex'

  export default {
    props: ['pagination'],
    computed: {
      page_links: function () {
        let c = this.pagination.page;
        let m = this.pagination.pages;

        let delta = 2,
          range = [],
          rangeWithDots = [],
          l;

        range.push(1);
        for (let i = c - delta; i <= c + delta; i++) {
          if (i < m && i > 1) {
            range.push(i);
          }
        }
        range.push(m);

        for (let i of range) {
          if (l) {
            if (i - l === 2) {
              rangeWithDots.push(l + 1);
            } else if (i - l !== 1) {
              rangeWithDots.push('...');
            }
          }
          rangeWithDots.push(i);
          l = i;
        }

        return rangeWithDots;

      }
    }
  }
</script>