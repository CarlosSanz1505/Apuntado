<<<<<<< HEAD
// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Menu from './components/Menu';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/login" component={Login} />
        <Route path="/menu" component={Menu} />
      </Routes>
    </Router>
  );
};
=======
import Login from "./components/Login";

function App() {
  return (
    <div className="App">
      <Login />
    </div>
  );
}
>>>>>>> 4461033ea43637d4fb36633c71e97e6ed9efa8ea

export default App;
