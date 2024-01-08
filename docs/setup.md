# Olvy Setup Guide

Welcome to the Olvy setup guide. This document will guide you through the process of setting up the Olvy platform on your local machine or production environment.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Node.js 14 or higher
- Docker and Docker Compose (for containerization)
- Git (for version control)

## Local Development Setup

### Backend Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-repository/olvy.git
   cd olvy/backend
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Copy the `.env.example` file to `.env` and fill in the necessary environment variables:
   ```
   cp .env.example .env
   ```

5. Run the Alembic migrations to set up the database schema:
   ```
   alembic upgrade head
   ```

6. Start the Flask application:
   ```
   python app.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd ../frontend
   ```

2. Install the required Node.js packages:
   ```
   npm install
   ```

3. Copy the `.env.example` file to `.env.local` and fill in the necessary environment variables:
   ```
   cp .env.example .env.local
   ```

4. Start the React development server:
   ```
   npm start
   ```

The frontend should now be running on `http://localhost:3000`.

## Production Setup

For production, we will use Docker to containerize our application.

1. Navigate to the root directory of the project:
   ```
   cd ..
   ```

2. Build the Docker images:
   ```
   docker-compose build
   ```

3. Start the containers:
   ```
   docker-compose up -d
   ```

The application should now be running and accessible via the configured ports.

## Testing

To ensure that everything is set up correctly, you can run the automated tests.

### Backend Tests

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Run the tests:
   ```
   pytest
   ```

### Frontend Tests

1. Navigate to the frontend directory:
   ```
   cd ../frontend
   ```

2. Run the tests:
   ```
   npm test
   ```

## Additional Information

For detailed API documentation, refer to `docs/api_documentation.md`.
For information on how to contribute to the project, refer to `docs/contribution.md`.
For deployment instructions, refer to `docs/deployment.md`.

Thank you for setting up Olvy. If you encounter any issues, please refer to the documentation or contact support.