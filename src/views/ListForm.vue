<template>
    <div>
        <h1 v-if="fields.id">Update {{fields.name}}</h1>
        <h1 v-else>Create New List</h1>
        <vue-form :fields="fields" :action="endpoint()">
            <template slot-scope="form">
                <input type="text" v-model="fields.name" id="name" class="form-control" name="name"/>
                <span class="text-danger">{{form.errors.get('name')}}</span>
            </template>
        </vue-form>
        <div v-if="fields.customers" class="card p-2">
            <h2>Users</h2>
            <div>
                <div class="badge badge-secondary"><h5 class="mb-1">
                    {{fields.customers.page_size}} of {{fields.customers.count}}</h5></div>
                <a class="btn btn-primary btn-sm" :href="`/lists/${fields.id}/export/customers/`">Export XLS</a>

                <button type="button" class="btn btn-success btn-sm" data-toggle="modal" data-target="#customers-import-modal">
                    Import XLS
                </button>

            </div>
            <table class="table">
                <tr v-for="customer in fields.customers.results">
                    <td>
                        <router-link :to="`/customers/update/${customer.id}/`">
                            {{customer.name}}
                        </router-link>
                    </td>
                    <td><span class="badge badge-secondary mr-1" v-for="email in customer.email">{{email}}</span></td>
                    <td><span class="badge badge-secondary mr-1" v-for="phone in customer.phone">{{phone}}</span></td>
                </tr>
            </table>
        </div>
        <div class="modal fade" id="customers-import-modal" tabindex="-1" role="dialog" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <form @submit="import_xls">
                        <div class="modal-header">
                            <h5 class="modal-title">Import Customers</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            Choose an XLS file:
                            <input type="file" ref="import_file" required/>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                            <input type="submit" class="btn btn-success" value="Upload"/>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  import Form from '../mixins/Form'
  import LoginRequired from '../mixins/LoginRequired'

  export default {
    endpoint: 'lists/',
    success_url: '/lists/',
    collection_name: 'lists',
    mixins: [Form, LoginRequired],
    data() {
      return {}
    },
    methods: {
      import_xls: function (e) {
        e.preventDefault();
        let files = this.$refs.import_file.files;
        let data = new FormData();
        // for single file
        data.append('file', files[0]);
        // Or for multiple files you can also do
        //  _.each(files, function(v, k){
        //    data.append('avatars['+k+']', v);
        // });

        axios_origin.post(`/lists/${this.fields.id}/import/customers/`, data).then(response => {
          this.$success('Saved!');
          $("#customers-import-modal").modal('hide');
        })
          .catch(error => {
            this.$error('Import failed!');
          });
      }
    }
  }
</script>