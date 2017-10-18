<template>
    <div class="vue-form">
        <form method="POST" @submit.prevent="save(action)" @keydown="errors.clear($event.target.name)">
            <span class="text-danger">{{errors.get('__form__')}}</span>
            <div>
                <slot :errors="errors">
                </slot>
            </div>

            <div class="form-group pt-2">
                <slot name="submit">
                    <button v-if="fields.id" class="btn btn-warning" :disabled="errors.any()">Update</button>
                    <button class="btn btn-success" :disabled="errors.any()" v-else>Create</button>
                </slot>
            </div>
        </form>
    </div>
</template>
<script>

  class Errors {
    constructor() {
      this.errors = {};
    }

    has(field) {
      return this.errors.hasOwnProperty(field);
    }


    any() {
      return Object.keys(this.errors).length > 0;
    }


    get(field) {
      if (this.errors[field]) {
        return this.errors[field][0];
      }
    }


    record(errors) {
      this.errors = errors;
    }


    clear(field) {
      if (field) {
        global.Vue.delete(this.errors, field);
        return;
      }
      this.errors = {};
    }
  }


  export default {

    props: ['fields', 'action'],

    data() {
      let dct = {};
      dct.field_names = [];

      for (let field in this.data) {
        dct.field_names.push(field);
      }

      dct.errors = new Errors();
      return dct
    },

    methods: {

      reset() {
        this.errors.clear();
      },

      save(url) {
        let verb;
        if (this.fields.id) {
          verb = 'put';
        } else {
          verb = 'post';
        }
        this.submit(verb, url);
      },


      post(url) {
        return this.submit('post', url);
      },


      put(url) {
        return this.submit('put', url);
      },


      patch(url) {
        return this.submit('patch', url);
      },


      delete(url) {
        return this.submit('delete', url);
      },


      submit(requestType, url) {
        return new Promise((resolve, reject) => {
          axios[requestType](url, this.fields)
            .then(response => {
              this.onSuccess(response.data);
              this.$parent.$emit('success', response.data);
              resolve(response.data);
            })
            .catch(error => {
              this.onFail(error.response.data);
              this.$parent.$emit('failure', error.response.data);
              reject(error.response.data);
            });
        });
      },


      onSuccess(data) {
        this.reset();
      },

      onFail(errors) {
        this.errors.record(errors);
      }
    }
  }
  //  import Vue from 'vue'
  //
  //  const FieldError = Vue.component('field-error', {
  //    props: ['error'],
  //    template: ' <span class="text-danger" v-if="error">{{error}}</span>'
  //  });
  //  
  //  export FieldError;
</script>