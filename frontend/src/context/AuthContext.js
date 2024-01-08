import React, { createContext, useContext, useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import authService from '../services/authService';

const AuthContext = createContext();

export const useAuth = () => {
  return useContext(AuthContext);
};

export const AuthProvider = ({ children }) => {
  const [currentUser, setCurrentUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const history = useHistory();

  const login = async (email, password) => {
    try {
      const user = await authService.login(email, password);
      setCurrentUser(user);
      history.push('/');
    } catch (error) {
      throw error;
    }
  };

  const register = async (email, password) => {
    try {
      const user = await authService.register(email, password);
      setCurrentUser(user);
      history.push('/');
    } catch (error) {
      throw error;
    }
  };

  const logout = () => {
    authService.logout();
    setCurrentUser(null);
    history.push('/login');
  };

  useEffect(() => {
    const unsubscribe = authService.onAuthStateChanged(user => {
      setCurrentUser(user);
      setLoading(false);
    });

    // Cleanup subscription on unmount
    return unsubscribe;
  }, []);

  const value = {
    currentUser,
    login,
    register,
    logout,
    loading
  };

  return (
    <AuthContext.Provider value={value}>
      {!loading && children}
    </AuthContext.Provider>
  );
};