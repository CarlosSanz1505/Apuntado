<<<<<<< HEAD
// Login.js
import React from 'react';

const Login = () => {
  return (
    <div>
      <h1>Login Screen</h1>
      {/* Add your login form or other content here */}
    </div>
  );
};
=======
import { Navigate } from 'react-router-dom';

const LoginScreen = () => (
    <div>
        <h1>Login Screen</h1>
        <a href="/Menu">Menu Screen</a>
    </div>
)

const Menu = () => (
    <div>
        <h1>Menu Screen</h1>
        <a href="/Login">Login Screen</a>
    </div>
)

function Login() {
  const Funct = () => {
    return (
      <Navigate to="/LoginScreen"/>
    )
  }

  return (
    <div className="App">
      <button onClick={Funct}>Funct</button>
    </div>
  );
}
>>>>>>> 4461033ea43637d4fb36633c71e97e6ed9efa8ea

export default Login;
