const validateEmail = (email) => {
  const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
};

const validatePassword = (password) => {
  // Minimum eight characters, at least one letter and one number:
  const re = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
  return re.test(String(password));
};

const validateSurveyForm = (formData) => {
  const errors = {};
  if (!formData.title || formData.title.trim() === '') {
    errors.title = 'Title is required';
  }
  if (!formData.description || formData.description.trim() === '') {
    errors.description = 'Description is required';
  }
  if (formData.questions && formData.questions.length === 0) {
    errors.questions = 'At least one question is required';
  }
  formData.questions.forEach((question, index) => {
    if (!question.text || question.text.trim() === '') {
      errors[`questions[${index}].text`] = 'Question text is required';
    }
    if (!question.type || question.type.trim() === '') {
      errors[`questions[${index}].type`] = 'Question type is required';
    }
  });
  return {
    isValid: Object.keys(errors).length === 0,
    errors,
  };
};

const validateResponse = (response, questions) => {
  const errors = {};
  questions.forEach((question, index) => {
    if (question.required && (!response[index] || response[index].trim() === '')) {
      errors[`response[${index}]`] = 'Response is required';
    }
  });
  return {
    isValid: Object.keys(errors).length === 0,
    errors,
  };
};

export {
  validateEmail,
  validatePassword,
  validateSurveyForm,
  validateResponse,
};