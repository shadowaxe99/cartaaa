import React from 'react';
import { Link, useHistory } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';

const Navbar = () => {
  const { isAuthenticated, logout } = useAuth();
  const history = useHistory();

  const handleLogout = () => {
    logout();
    history.push('/login');
  };

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">Olvy</Link>
      </div>
      <div className="navbar-menu">
        <div className="navbar-start">
          <Link to="/surveys" className="navbar-item">Surveys</Link>
          {isAuthenticated && <Link to="/analytics" className="navbar-item">Analytics</Link>}
        </div>
        <div className="navbar-end">
          {!isAuthenticated ? (
            <>
              <Link to="/login" className="navbar-item">Login</Link>
              <Link to="/register" className="navbar-item">Register</Link>
            </>
          ) : (
            <button onClick={handleLogout} className="navbar-item">Logout</button>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;