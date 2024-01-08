# Integration Guide for Olvy's Customer Survey Tool

## Table of Contents
- [Introduction](#introduction)
- [Carta Integration](#carta-integration)
- [CRM Integration](#crm-integration)
- [OpenAI Integration](#openai-integration)
- [API Integration](#api-integration)
- [Troubleshooting](#troubleshooting)

## Introduction
This guide provides instructions on how to integrate Olvy's Customer Survey Tool with third-party services such as Carta, CRM platforms, and OpenAI. Follow the steps outlined below to ensure a smooth integration process.

## Carta Integration
To integrate with Carta, you will need to use the `CARTA_API_KEY` and interact with Carta's API endpoints.

### Setup
1. Ensure you have the `CARTA_API_KEY` set in your `.env` file.
2. Use the `integrateCarta` function located in `backend/integrations/carta_integration.py`.

### Usage
```python
from backend.integrations.carta_integration import integrateCarta

# Call the function with necessary parameters
integrateCarta(carta_api_key=CARTA_API_KEY, data_to_sync={})
```

## CRM Integration
Integrating with a CRM platform allows you to sync survey respondent data with your CRM records.

### Setup
1. Set the `CRM_API_KEY` in your `.env` file.
2. Utilize the `integrateCRM` function found in `backend/integrations/crm_integration.py`.

### Usage
```python
from backend.integrations.crm_integration import integrateCRM

# Sync data with CRM
integrateCRM(crm_api_key=CRM_API_KEY, respondent_data={})
```

## OpenAI Integration
Leverage OpenAI's natural language processing capabilities to analyze survey responses.

### Setup
1. Add `OPENAI_API_KEY` to your `.env` file.
2. Use the `openai_client.py` module to interact with OpenAI's API.

### Usage
```python
from backend.openai_client import OpenAIClient

# Initialize the OpenAI client
openai_client = OpenAIClient(api_key=OPENAI_API_KEY)

# Analyze text
analysis = openai_client.analyze_text(text="Your survey response here")
```

## API Integration
Olvy's Customer Survey Tool provides API endpoints for integration with other systems.

### Endpoints
- User operations: `/api/users`
- Survey operations: `/api/surveys`
- Response operations: `/api/responses`
- Analytics operations: `/api/analytics`
- Authentication operations: `/api/auth`

### Example API Call
```javascript
import axios from 'axios';
import { API_BASE_URL } from 'frontend/src/services/apiClient';

// Fetch surveys
axios.get(`${API_BASE_URL}/api/surveys`)
  .then(response => {
    // Handle response data
  })
  .catch(error => {
    // Handle error
  });
```

## Troubleshooting
If you encounter issues during the integration process, please refer to the following steps:

1. Check your `.env` file for correct API keys.
2. Ensure that the third-party service is operational and accessible.
3. Review the error logs in `backend/logs` for detailed error messages.
4. Consult the `docs/api_documentation.md` for endpoint specifications.

For further assistance, please contact Olvy's support team.