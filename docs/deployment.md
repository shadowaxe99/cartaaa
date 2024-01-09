# Deployment Guide for Olvy's Customer Survey Tool

This document provides detailed instructions for deploying Olvy's Customer Survey Tool, which includes both backend and frontend components.

## Prerequisites

Before you begin the deployment process, ensure you have the following:

- Docker and Docker Compose installed on your deployment machine.
- An AWS or Google Cloud Platform account for backend deployment.
- Domain name for the frontend application (optional).

## Backend Deployment

### 1. Set up Environment Variables

Create a `.env` file in the root directory of your backend application with the following variables:

```
DATABASE_URL=your_database_connection_string
OPENAI_API_KEY=your_openai_api_key
CARTA_API_KEY=your_carta_api_key
CRM_API_KEY=your_crm_api_key
```

Replace `your_database_connection_string`, `your_openai_api_key`, `your_carta_api_key`, and `your_crm_api_key` with your actual credentials.

### 2. Build and Run with Docker

Navigate to the root directory of the backend application and run the following command to build and start your containers:

```
docker-compose up --build
```

This command will start the backend server and all associated services as defined in the `docker-compose.yml` file.

### 3. Database Migrations

After the containers are up and running, execute the following command to perform database migrations:

```
docker-compose exec backend alembic upgrade head
```

This will apply all the Alembic migrations to your database, setting up the necessary tables and relationships.

## Frontend Deployment

### 1. Build the Frontend Application

Navigate to the root directory of the frontend application and run:

```
npm install
npm run build
```

This will install all dependencies and create a production build of the application in the `build` folder.

### 2. Serve the Frontend Application

You can serve the frontend application using a web server like Nginx or Apache. For simplicity, we'll use the `serve` package.

Install `serve` globally:

```
npm install -g serve
```

Serve the application:

```
serve -s build
```

This will start the frontend application on the default port 5000.

## Domain Configuration (Optional)

If you have a domain name, configure your DNS settings to point to the IP address of your deployment machine. Then, set up your web server to serve the frontend application on port 80 or 443 for HTTPS.

## Verifying the Deployment

After completing the deployment steps, open your web browser and navigate to the IP address or domain name of your deployment machine. You should see the Olvy's Customer Survey Tool login page.

## Troubleshooting

If you encounter any issues during deployment, check the following:

- Ensure all environment variables are correctly set.
- Check the Docker container logs for any error messages.
- Verify that the database migrations have been applied successfully.
- Ensure the frontend application's build process completed without errors.

For detailed error logs, you can run:

```
docker-compose logs
```

## Conclusion

You have now successfully deployed Olvy's Customer Survey Tool. For further assistance, refer to the `README.md` and other documentation files in the `docs` directory.