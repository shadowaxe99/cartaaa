import { useState, useEffect, useCallback } from 'react';
import apiClient from '../services/apiClient';

const useSurveys = () => {
  const [surveys, setSurveys] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchSurveys = useCallback(async () => {
    setLoading(true);
    try {
      const response = await apiClient.get('/api/surveys');
      setSurveys(response.data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  const createSurvey = useCallback(async (surveyData) => {
    setLoading(true);
    try {
      const response = await apiClient.post('/api/surveys', surveyData);
      setSurveys(prevSurveys => [...prevSurveys, response.data]);
      setError(null);
      return response.data;
    } catch (err) {
      setError(err.message);
      return null;
    } finally {
      setLoading(false);
    }
  }, []);

  const deleteSurvey = useCallback(async (surveyId) => {
    setLoading(true);
    try {
      await apiClient.delete(`/api/surveys/${surveyId}`);
      setSurveys(prevSurveys => prevSurveys.filter(survey => survey.id !== surveyId));
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchSurveys();
  }, [fetchSurveys]);

  return {
    surveys,
    loading,
    error,
    fetchSurveys,
    createSurvey,
    deleteSurvey
  };
};

export default useSurveys;