// import styles
import './App.css';
import { useState } from "react"


function App() {
  const [todos, setTodos] = useState([])
  const [todo, setTodo] = useState('')

  const addTodo = () => {
    if (todo != '') {
    setTodos([...todos, todo])
    }
  }

  return (
    <div className="App">
      <h1 className='main-h1'>
        Add Task</h1>
      <input type="text" 
      name="todo" 
      placeholder="Enter Task Details" 
      className='add-task'
      value={todo}
      onChange={
        (e) => {
          setTodo(e.target.value)
        }
        } 
      />
      <button className="add-button"
        onClick={addTodo}>Add</button>
    <ul className='todo-list'>
      {
        todos.map((todo, index) => (
          <div className='todo'>
            <li key={index} className="task"> {todo} </li>
            <button className="delete-button" onClick={
              () => {
                const newTodos = todos.filter((t, i) => i !== index)
                setTodos(newTodos)
              }
            }>Delete</button>
          </div>
        ))
      }
    </ul>
    </div>
  );
}

export default App;
