import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = 'Bearer ' + token;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

apiClient.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('token');
      // Redirect to login page or handle token expiration appropriately
    }
    return Promise.reject(error);
  }
);

export const registerUser = async (userData) => {
  return await apiClient.post('/users/register', userData);
};

export const loginUser = async (credentials) => {
  return await apiClient.post('/auth/login', credentials);
};

export const createSurvey = async (surveyData) => {
  return await apiClient.post('/surveys', surveyData);
};

export const listSurveys = async () => {
  return await apiClient.get('/surveys');
};

export const getSurveyById = async (surveyId) => {
  return await apiClient.get(`/surveys/${surveyId}`);
};

export const submitResponse = async (surveyId, responseData) => {
  return await apiClient.post(`/responses/${surveyId}`, responseData);
};

export const fetchSurveyAnalytics = async (surveyId) => {
  return await apiClient.get(`/analytics/${surveyId}`);
};

export const logoutUser = () => {
  localStorage.removeItem('token');
  // Redirect to login page or handle logout appropriately
};

export default apiClient;