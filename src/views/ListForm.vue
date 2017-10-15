<template>
    <div>
        <h1>Create New List</h1>
        <form method="POST" @submit.prevent="form.post('/api/v1/lists/')" @keydown="form.errors.clear($event.target.name)">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" v-model="form.name" id="name" class="form-control" name="name"/>
                <span class="text-danger" v-if="form.errors.has('name')">{{ form.errors.get('name') }}</span>
            </div>
            <button class="btn btn-success" :disabled="form.errors.any()">Create</button>
        </form>
    </div>
</template>

<script>
  import Form from '../includes/Form';

  export default {
    data() {
      return {
        form: new Form({
          'name': ''
        })
      }
    }
  }
</script>