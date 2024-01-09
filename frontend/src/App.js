```javascript
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import SurveyForm from './components/SurveyForm';
import SurveyList from './components/SurveyList';
import SurveyAnalytics from './components/SurveyAnalytics';
import Login from './components/Login';
import Register from './components/Register';
import PrivateRoute from './components/PrivateRoute';
import { AuthProvider } from './context/AuthContext';
import './styles/index.css';
import './styles/App.css';

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="App">
          <Navbar />
          <Switch>
            <Route exact path="/" component={SurveyList} />
            <Route path="/login" component={Login} />
            <Route path="/register" component={Register} />
            <PrivateRoute path="/create-survey" component={SurveyForm} />
            <PrivateRoute path="/analytics" component={SurveyAnalytics} />
            {/* More private or public routes can be added here */}
          </Switch>
          <Footer />
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
```