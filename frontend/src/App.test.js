import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from './App';
import { BrowserRouter } from 'react-router-dom';
import AuthService from './services/authService';

jest.mock('./services/authService');

describe('App Component', () => {
  test('renders App component', () => {
    render(
      <BrowserRouter>
        <App />
      </BrowserRouter>
    );
    expect(screen.getByText(/Olvy/i)).toBeInTheDocument();
  });

  test('navigates to login when not authenticated', async () => {
    AuthService.isAuthenticated = jest.fn().mockResolvedValue(false);
    render(
      <BrowserRouter>
        <App />
      </BrowserRouter>
    );
    await waitFor(() => expect(screen.getByText(/Login/i)).toBeInTheDocument());
  });

  test('navigates to dashboard when authenticated', async () => {
    AuthService.isAuthenticated = jest.fn().mockResolvedValue(true);
    render(
      <BrowserRouter>
        <App />
      </BrowserRouter>
    );
    await waitFor(() => expect(screen.getByText(/Dashboard/i)).toBeInTheDocument());
  });

  test('allows user to log out', async () => {
    AuthService.isAuthenticated = jest.fn().mockResolvedValue(true);
    AuthService.logout = jest.fn();
    render(
      <BrowserRouter>
        <App />
      </BrowserRouter>
    );
    await waitFor(() => fireEvent.click(screen.getByText(/Logout/i)));
    expect(AuthService.logout).toHaveBeenCalled();
  });
});