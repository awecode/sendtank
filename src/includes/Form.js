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
      delete this.errors[field];

      return;
    }

    this.errors = {};
  }
}


class Form {
  constructor(data) {
    this.original_data = data;
    this.fields = [];


    for (let field in data) {
      this[field] = data[field];
      this.fields.push(field);
    }

    this.errors = new Errors();
  }


  data() {
    let data = {};

    for (let property in this.fields) {
      data[property] = this[property];
    }

    return data;
  }


  reset() {
    for (let field in this.fields) {
      this[field] = '';
    }

    this.errors.clear();
  }


  post(url) {
    console.log(url);
    return this.submit('post', url);
  }


  put(url) {
    return this.submit('put', url);
  }


  patch(url) {
    return this.submit('patch', url);
  }


  delete(url) {
    return this.submit('delete', url);
  }


  submit(requestType, url) {
    return new Promise((resolve, reject) => {
      axios[requestType](url, this.data())
        .then(response => {
          this.onSuccess(response.data);

          resolve(response.data);
        })
        .catch(error => {
          this.onFail(error.response.data);

          reject(error.response.data);
        });
    });
  }


  onSuccess(data) {
    alert(data.message); // temporary

    this.reset();
  }


  onFail(errors) {
    this.errors.record(errors);
  }
}

export default Form