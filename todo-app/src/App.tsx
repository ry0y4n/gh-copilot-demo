import React, { useState } from 'react';
import './App.css';

interface Todo {
  id: number;
  title: string;
  dueDate: string;
  status: 'Not Started' | 'In Progress' | 'Completed';
}

const App: React.FC = () => {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [title, setTitle] = useState('');
  const [dueDate, setDueDate] = useState('');

  const addTodo = () => {
    const newTodo: Todo = {
      id: Date.now(),
      title,
      dueDate,
      status: 'Not Started',
    };
    setTodos([...todos, newTodo]);
    setTitle('');
    setDueDate('');
  };

  const updateStatus = (id: number, status: Todo['status']) => {
    setTodos(todos.map(todo => todo.id === id ? { ...todo, status } : todo));
  };

  return (
    <div className="app">
      <h1>Todo App</h1>
      <div className="input-container">
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <input
          type="date"
          value={dueDate}
          onChange={(e) => setDueDate(e.target.value)}
        />
        <button onClick={addTodo}>Add Todo</button>
      </div>
      <ul className="todo-list">
        {todos.map(todo => (
          <li key={todo.id} className="todo-item">
            <h2>{todo.title}</h2>
            <p>Due Date: {todo.dueDate}</p>
            <p>Status: {todo.status}</p>
            <select
              value={todo.status}
              onChange={(e) => updateStatus(todo.id, e.target.value as Todo['status'])}
            >
              <option value="Not Started">Not Started</option>
              <option value="In Progress">In Progress</option>
              <option value="Completed">Completed</option>
            </select>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;