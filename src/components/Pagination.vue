<template>
    <div id="v-pagination-container" v-if="page_data">
        <span class="badge badge-secondary">Showing {{ page_data.results.length }} of {{page_data.count}}</span>
        <span class="badge badge-secondary">Page {{page_data.page}} of {{page_data.pages}}</span>

        <nav>
            <ul class="pagination">
                <li class="page-item" v-if="page_data.previous">
                    <a class="page-link" href="#" tabindex="-1">Previous</a>
                </li>
                <li class="page-item" v-for="pg in page_links" :class="{active: pg==page_data.page}">
                    <a class="page-link" href="#">{{pg}}</a>
                </li>
                <li class="page-item" v-if="page_data.next">
                    <a class="page-link" href="#">Next</a>
                </li>
            </ul>
        </nav>

    </div>
</template>

<script>
  import {mapState, mapActions} from 'vuex'

  export default {
    props: ['page_data'],
    computed: {
      page_links: function () {
        let c = this.page_data.page;
        let m = this.page_data.pages;

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