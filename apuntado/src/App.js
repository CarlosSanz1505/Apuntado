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

export default App;
