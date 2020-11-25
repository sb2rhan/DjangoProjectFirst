<template>
  <div id="nav">
    <div class="tasks">
      <h1 class="text-center">TODO List</h1>

      <!-- sending our create request to django rest framework -->
      <form
        class="m-5 d-flex justify-content-center"
        v-on:submit.prevent="create_todo"
      >
        <div class="form-group col-md-4 text-center">
          <label for="desc">Description</label>
          <input
            id="desc"
            type="text"
            class="form-control"
            v-model="description"
          />
        </div>
        <div class="form-group col-md-4 text-center">
          <label for="statusControl">Select status</label>
          <select
            v-model="status"
            name="status"
            id="statusControl"
            class="form-control"
          >
            <option value="todo">Todo</option>
            <option value="done">Done</option>
          </select>
        </div>
        <button class="btn btn-primary">Submit</button>
      </form>

      <div
        class="d-flex justify-content-center form-check"
        v-for="(item, index) in todos"
        :key="index"
      >
        <label v-bind:for="index">
          <h2>{{ item.description }}</h2>
        </label>
        <input
          v-bind:id="index"
          v-if="item.status == 'done'"
          @click="statusUpdate(item.id, 'todo')"
          name="task1"
          type="checkbox"
          checked
        />
        <input
          v-bind:id="index"
          v-if="item.status == 'todo'"
          @click="statusUpdate(item.id, 'done')"
          name="task1"
          type="checkbox"
        />
        <a @click="deleteTask(item.id)" class="text-danger">DELETE</a>
      </div>
    </div>
  </div>
</template>

<script>
// url address of our django rest api server
const API_URL = "http://127.0.0.1:8000/api/v1/todo/";

import axios from "axios"; // module for AJAX requests

// vue js environment
export default {
  name: "App",
  // our data in use
  data() {
    return {
      todos: [],
      id: "",
      description: "",
      status: "",
    };
  },
  // mounted runs when page is loaded
  mounted() {
    console.log("Hello");
    this.get_todos();
  },
  // all methods we can call from html template
  methods: {
    get_todos() {
      var vue = this;
      // request to back-end(python)
      axios({
        method: "GET",
        url: API_URL,
      }).then(function (response) {
        console.log(response.data);
        vue.todos = response.data;
      });
    },
    create_todo() {
      var vue = this;
      console.log(this.description);
      console.log(this.status);
      axios({
        url: API_URL,
        method: "POST",
        data: {
          description: this.description,
          status: this.status,
        },
      })
        .then(function (response) {
          console.log(response.data);
          var new_todo = {
            id: response.data.id,
            description: response.data.description,
            status: response.data.status,
          };
          vue.todos.push(new_todo);
          vue.description = "";
          vue.status = "";
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    // updates status of todos
    statusUpdate(id, flag) {
      var todo_ch = this.todos.filter((todo) => todo.id == id)[0];
      axios({
        url: API_URL + id + "/",
        method: "PUT",
        data: {
          description: todo_ch.description,
          status: flag,
        },
      }).then(function (response) {
        console.log(response.data);
      });
    },
    deleteTask(id) {
      var vue = this;
      axios({
        url: API_URL + id + "/",
        method: "DELETE",
      })
        .then(function (response) {
          console.log(response);
          vue.todos = vue.todos.filter((todo) => todo.id != id);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>