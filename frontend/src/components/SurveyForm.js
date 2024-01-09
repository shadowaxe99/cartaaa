import React, { useState } from 'react';
import { useForm } from '../hooks/useForm';
import surveyService from '../services/surveyService';
import validate from '../utils/validate';

const SurveyForm = () => {
  const { values, errors, handleChange, handleSubmit } = useForm(createSurvey, validate);

  function createSurvey() {
    surveyService.createSurvey(values).then(response => {
      // Handle response here
    }).catch(error => {
      // Handle errors here
    });
  }

  return (
    <form id="survey-form" onSubmit={handleSubmit} noValidate>
      <h2>Create Survey</h2>
      <div className="form-group">
        <label htmlFor="surveyTitle">Survey Title</label>
        <input
          type="text"
          name="title"
          id="surveyTitle"
          value={values.title || ''}
          onChange={handleChange}
          className={`form-control ${errors.title && 'is-invalid'}`}
        />
        {errors.title && <p className="invalid-feedback">{errors.title}</p>}
      </div>
      <div className="form-group">
        <label htmlFor="surveyDescription">Description</label>
        <textarea
          name="description"
          id="surveyDescription"
          value={values.description || ''}
          onChange={handleChange}
          className={`form-control ${errors.description && 'is-invalid'}`}
        />
        {errors.description && <p className="invalid-feedback">{errors.description}</p>}
      </div>
      <div className="form-group">
        <label htmlFor="surveyLanguage">Language</label>
        <select
          name="language"
          id="surveyLanguage"
          value={values.language || ''}
          onChange={handleChange}
          className={`form-control ${errors.language && 'is-invalid'}`}
        >
          <option value="">Select Language</option>
          <option value="en">English</option>
          <option value="es">Spanish</option>
          <option value="fr">French</option>
          {/* Add more languages as needed */}
        </select>
        {errors.language && <p className="invalid-feedback">{errors.language}</p>}
      </div>
      <div className="form-group">
        <label htmlFor="surveyExpiration">Expiration Date</label>
        <input
          type="date"
          name="expiration"
          id="surveyExpiration"
          value={values.expiration || ''}
          onChange={handleChange}
          className={`form-control ${errors.expiration && 'is-invalid'}`}
        />
        {errors.expiration && <p className="invalid-feedback">{errors.expiration}</p>}
      </div>
      <button type="submit" className="btn btn-primary">Create Survey</button>
    </form>
  );
};

export default SurveyForm;