import axios from 'axios';
import { API_BASE_URL } from '../utils/constants';

const authService = {
  login: async function (email, password) {
    try {
      const response = await axios.post(`${API_BASE_URL}/api/auth/login`, {
        email,
        password,
      });
      if (response.data.accessToken) {
        localStorage.setItem('user', JSON.stringify(response.data));
      }
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  logout: function () {
    localStorage.removeItem('user');
  },

  register: async function (userData) {
    try {
      const response = await axios.post(`${API_BASE_URL}/api/auth/register`, userData);
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  getCurrentUser: function () {
    return JSON.parse(localStorage.getItem('user'));
  },

  updateProfile: async function (userData) {
    try {
      const user = this.getCurrentUser();
      const response = await axios.put(`${API_BASE_URL}/api/users/${user.id}`, userData, {
        headers: {
          Authorization: `Bearer ${user.accessToken}`,
        },
      });
      if (response.data) {
        localStorage.setItem('user', JSON.stringify({ ...user, ...response.data }));
      }
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  changePassword: async function (oldPassword, newPassword) {
    try {
      const user = this.getCurrentUser();
      const response = await axios.put(`${API_BASE_URL}/api/users/${user.id}/change-password`, {
        oldPassword,
        newPassword,
      }, {
        headers: {
          Authorization: `Bearer ${user.accessToken}`,
        },
      });
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },
};

export default authService;