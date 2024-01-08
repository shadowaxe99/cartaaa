# Contribution Guidelines

Welcome to the Olvy contribution guide. Thank you for your interest in contributing to our project! This document provides the guidelines and information you need to contribute to Olvy effectively.

## Getting Started

Before you begin, ensure you have the following prerequisites installed and set up:

- Git
- Python 3.8 or higher
- Node.js 14 or higher
- Docker and Docker Compose (for containerization)

## Setting Up Your Development Environment

1. Fork the repository and clone your fork to your local machine.
2. Navigate to the project directory and install the backend dependencies:

```bash
cd backend
pip install -r requirements.txt
```

3. Set up the frontend dependencies:

```bash
cd ../frontend
npm install
```

4. Copy the `.env.example` file to `.env` and fill in the necessary environment variables:

```bash
cp .env.example .env
```

5. Start the development servers:

```bash
# Start the backend server
cd backend
python main.py

# In a new terminal, start the frontend development server
cd frontend
npm start
```

## Code Contributions

When contributing to the codebase, please follow these steps:

1. Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/your-feature-name
```

2. Write your code, adhering to the shared dependencies and naming conventions outlined in the project documentation.
3. Ensure your code passes all tests and meets the style guidelines (PEP 8 for Python, ESLint for JavaScript).
4. Commit your changes with a clear and descriptive commit message:

```bash
git commit -am "Add a new feature for creating surveys"
```

5. Push your branch to your fork:

```bash
git push origin feature/your-feature-name
```

6. Open a pull request against the main repository with a clear title and description.

## Documentation Contributions

To contribute to the documentation:

1. Make your changes to the markdown files in the `docs` directory.
2. Follow the markdown syntax and project documentation style.
3. Submit a pull request with your changes.

## Reporting Issues

If you find a bug or have a suggestion for improvement, please report it via the project's issue tracker. Include as much detail as possible, such as steps to reproduce the bug, expected behavior, and actual behavior.

## Code Review Process

Our maintainers will review your pull request. We may suggest changes or improvements. Once approved, a maintainer will merge your changes into the main codebase.

## Community Guidelines

We strive to maintain a welcoming and inclusive community. Please respect all contributors, adhere to the code of conduct, and collaborate constructively.

Thank you for contributing to Olvy! Your efforts help us build a better cap table management platform.