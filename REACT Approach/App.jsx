import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './Login';
import Menu from './Menu';

const App = () => {
    return (
        <Router>
            <Switch>
                <Route path="/Login" component={Login} />
                <Route path="/Menu" component={Menu} />
            </Switch>
        </Router>
    );
};

export default App;