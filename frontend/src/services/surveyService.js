import apiClient from './apiClient';

const createSurvey = async (surveyData) => {
  try {
    const response = await apiClient.post('/api/surveys', surveyData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const listSurveys = async () => {
  try {
    const response = await apiClient.get('/api/surveys');
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const getSurvey = async (surveyId) => {
  try {
    const response = await apiClient.get(`/api/surveys/${surveyId}`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const updateSurvey = async (surveyId, surveyData) => {
  try {
    const response = await apiClient.put(`/api/surveys/${surveyId}`, surveyData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const deleteSurvey = async (surveyId) => {
  try {
    const response = await apiClient.delete(`/api/surveys/${surveyId}`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const submitResponse = async (surveyId, responseData) => {
  try {
    const response = await apiClient.post(`/api/surveys/${surveyId}/responses`, responseData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const getSurveyResponses = async (surveyId) => {
  try {
    const response = await apiClient.get(`/api/surveys/${surveyId}/responses`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const getSurveyAnalytics = async (surveyId) => {
  try {
    const response = await apiClient.get(`/api/surveys/${surveyId}/analytics`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export default {
  createSurvey,
  listSurveys,
  getSurvey,
  updateSurvey,
  deleteSurvey,
  submitResponse,
  getSurveyResponses,
  getSurveyAnalytics
};