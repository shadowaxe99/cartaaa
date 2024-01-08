import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import surveyService from '../services/surveyService';
import './SurveyList.css';

const SurveyList = () => {
  const [surveys, setSurveys] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchSurveys = async () => {
      setLoading(true);
      try {
        const response = await surveyService.listSurveys();
        setSurveys(response.data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchSurveys();
  }, []);

  if (loading) {
    return <div>Loading surveys...</div>;
  }

  if (error) {
    return <div>Error fetching surveys: {error}</div>;
  }

  return (
    <div className="survey-list">
      <h2>Surveys</h2>
      {surveys.length === 0 ? (
        <div>No surveys available. Create one?</div>
      ) : (
        <ul>
          {surveys.map((survey) => (
            <li key={survey.id}>
              <Link to={`/surveys/${survey.id}`}>
                <h3>{survey.title}</h3>
                <p>{survey.description}</p>
              </Link>
            </li>
          ))}
        </ul>
      )}
      <Link to="/create-survey" className="btn btn-primary">
        Create Survey
      </Link>
    </div>
  );
};

export default SurveyList;