import React, { useState, useContext } from 'react';
import { useHistory } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';
import authService from '../services/authService';
import validate from '../utils/validate';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState({});
  const { setAuthData } = useContext(AuthContext);
  const history = useHistory();

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    switch (name) {
      case 'email':
        setEmail(value);
        break;
      case 'password':
        setPassword(value);
        break;
      default:
        break;
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const errors = validate({ email, password });
    if (Object.keys(errors).length === 0) {
      try {
        const data = await authService.login(email, password);
        setAuthData(data);
        history.push('/');
      } catch (error) {
        setErrors({ submit: error.message });
      }
    } else {
      setErrors(errors);
    }
  };

  return (
    <div className="login-container">
      <form id="login-form" onSubmit={handleSubmit}>
        <h2>Login</h2>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            name="email"
            id="email"
            value={email}
            onChange={handleInputChange}
            className={errors.email ? 'is-invalid' : ''}
            required
          />
          {errors.email && <div className="invalid-feedback">{errors.email}</div>}
        </div>
        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            name="password"
            id="password"
            value={password}
            onChange={handleInputChange}
            className={errors.password ? 'is-invalid' : ''}
            required
          />
          {errors.password && <div className="invalid-feedback">{errors.password}</div>}
        </div>
        {errors.submit && <div className="error-message">{errors.submit}</div>}
        <button type="submit" className="btn btn-primary">Login</button>
      </form>
    </div>
  );
};

export default Login;