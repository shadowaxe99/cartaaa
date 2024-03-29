import React, { useState, useEffect } from 'react';
import { useSurveys } from '../hooks/useSurveys';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Doughnut } from 'react-chartjs-2';
import '../styles/SurveyAnalytics.css';

ChartJS.register(ArcElement, Tooltip, Legend);

const SurveyAnalytics = ({ surveyId }) => {
  const { getSurveyAnalytics } = useSurveys();
  const [analyticsData, setAnalyticsData] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAnalytics = async () => {
      try {
        setLoading(true);
        const data = await getSurveyAnalytics(surveyId);
        setAnalyticsData(data);
      } catch (error) {
        console.error('Error fetching survey analytics:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchAnalytics();
  }, [surveyId, getSurveyAnalytics]);

  const data = {
    labels: analyticsData.labels || [],
    datasets: [
      {
        label: '# of Votes',
        data: analyticsData.data || [],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
      }
    ]
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top'
      },
      title: {
        display: true,
        text: 'Survey Response Analytics'
      }
    }
  };

  return (
    <div className="survey-analytics-container">
      {loading ? (
        <p>Loading analytics...</p>
      ) : (
        <div className="chart-container">
          <Doughnut data={data} options={options} />
        </div>
      )}
    </div>
  );
};

export default SurveyAnalytics;