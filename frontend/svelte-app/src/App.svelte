<script>
  import axios from 'axios';

  let todos = [];
  let newTodo = '';

  async function fetchTodos() {
      const response = await axios.get('http://localhost:5000/list');
      todos = response.data;
  }

  async function addTodo() {
      if (newTodo.trim() !== '') {
          await axios.post('http://localhost:5000/add', { text: newTodo });
          newTodo = '';
          fetchTodos();
      }
  }

  async function deleteTodo(todo) {
      await axios.delete(`http://localhost:5000/delete/${todo.id}`);
      fetchTodos();
  }

  async function clearAll() {
      await axios.delete('http://localhost:5000/clear');
      fetchTodos();
  }

  fetchTodos();
</script>

<style>
* {
  box-sizing: border-box;
}

body {
  font-family: 'Arial', sans-serif;
  background-color: #f2f2f2;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

div {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-width: 100%;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 10px 0;
  padding: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

li:hover {
  background-color: #f5f5f5;
}

li:hover .delete-icon {
  visibility: visible;
}

.delete-icon {
  visibility: hidden;
  color: red;
  font-weight: bold;
}

button {
  display: block;
  padding: 10px;
  margin: 10px 0;
  border: none;
  background-color: #007BFF;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
}

button:hover {
  background-color: #0056b3;
}

input {
  padding: 5px;
  width: 75%;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.add-button {
  width: 15%;
  background-color: purple;
  margin-left: 10px;
}
</style>

<div>
<h1>Todo App</h1>
<div style="display: flex; justify-content: space-between; align-items: center;">
  <input bind:value={newTodo} placeholder="Add your new todo" />
  <button class="add-button" on:click={addTodo}>+</button>
</div>
<ul>
  {#each todos as todo}
    <li>
      {todo.text}
      <span class="delete-icon" on:click={() => deleteTodo(todo)}>🗑️</span>
    </li>
  {/each}
</ul>
<p>You have {todos.length} pending tasks</p>
<button on:click={clearAll}>Clear All</button>
</div>
