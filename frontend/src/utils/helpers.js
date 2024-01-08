// frontend/src/utils/helpers.js

/**
 * Helper functions for Olvy frontend application.
 */

/**
 * Formats date to a human-readable string.
 * @param {Date} date - The date to format.
 * @returns {string} - Formatted date string.
 */
export const formatDate = (date) => {
  return new Date(date).toLocaleDateString();
};

/**
 * Validates email using a simple regex pattern.
 * @param {string} email - The email to validate.
 * @returns {boolean} - True if the email is valid, false otherwise.
 */
export const validateEmail = (email) => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
};

/**
 * Capitalizes the first letter of a string.
 * @param {string} string - The string to capitalize.
 * @returns {string} - The capitalized string.
 */
export const capitalizeFirstLetter = (string) => {
  return string.charAt(0).toUpperCase() + string.slice(1);
};

/**
 * Extracts query parameters from a URL.
 * @param {string} url - The URL to parse.
 * @returns {Object} - An object containing query parameters.
 */
export const getQueryParams = (url) => {
  const params = {};
  new URL(url).searchParams.forEach((value, key) => {
    params[key] = value;
  });
  return params;
};

/**
 * Debounce function to limit the rate at which a function can fire.
 * @param {Function} func - The function to debounce.
 * @param {number} wait - The time to wait in milliseconds.
 * @returns {Function} - A debounced version of the original function.
 */
export const debounce = (func, wait) => {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
};

/**
 * Generates a unique identifier.
 * @returns {string} - A unique identifier string.
 */
export const generateUniqueId = () => {
  return Math.random().toString(36).substr(2, 9);
};

/**
 * Checks if an object is empty.
 * @param {Object} obj - The object to check.
 * @returns {boolean} - True if the object is empty, false otherwise.
 */
export const isEmptyObject = (obj) => {
  return Object.keys(obj).length === 0 && obj.constructor === Object;
};

/**
 * Encodes an object into a query string.
 * @param {Object} params - The object to encode.
 * @returns {string} - The encoded query string.
 */
export const encodeQueryParams = (params) => {
  return Object.keys(params)
    .map((key) => encodeURIComponent(key) + '=' + encodeURIComponent(params[key]))
    .join('&');
};

/**
 * Scrolls to the top of the page smoothly.
 */
export const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

/**
 * Checks if a response status code indicates a successful request.
 * @param {number} statusCode - The status code to check.
 * @returns {boolean} - True if the status code is a success code, false otherwise.
 */
export const isSuccessStatusCode = (statusCode) => {
  return statusCode >= 200 && statusCode < 300;
};