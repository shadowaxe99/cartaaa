# Olvy API Documentation

Welcome to the Olvy API documentation. This document provides information on how to interact with the API endpoints of the Olvy platform, specifically for the Customer Survey Tool feature.

## Base URL

All URLs referenced in the documentation have the following base:

```
https://api.olvy.co
```

## Authentication

To access the API, you will need to authenticate using JWT tokens. Obtain your token by logging in through the `/api/auth/login` endpoint.

## Endpoints

### User Management

#### Register a new user

- **POST** `/api/users/register`
- **Payload**: `UserSchema`
- **Success Response**: `USER_CREATED`

#### Login

- **POST** `/api/auth/login`
- **Payload**: `{ "username": "string", "password": "string" }`
- **Success Response**: `LOGIN_SUCCESS`

#### Logout

- **POST** `/api/auth/logout`
- **Success Response**: `LOGOUT_SUCCESS`

### Survey Management

#### Create a new survey

- **POST** `/api/surveys`
- **Payload**: `SurveySchema`
- **Success Response**: `SURVEY_CREATED`

#### List all surveys

- **GET** `/api/surveys`
- **Success Response**: `List[SurveySchema]`

#### Get a specific survey

- **GET** `/api/surveys/{survey_id}`
- **Success Response**: `SurveySchema`

#### Update a survey

- **PUT** `/api/surveys/{survey_id}`
- **Payload**: `SurveySchema`
- **Success Response**: `SURVEY_CREATED`

#### Delete a survey

- **DELETE** `/api/surveys/{survey_id}`
- **Success Response**: `SURVEY_CREATED`

### Response Management

#### Submit a survey response

- **POST** `/api/responses`
- **Payload**: `ResponseSchema`
- **Success Response**: `RESPONSE_SUBMITTED`

#### Get responses for a survey

- **GET** `/api/responses/{survey_id}`
- **Success Response**: `List[ResponseSchema]`

### Analytics

#### Get analytics for a survey

- **GET** `/api/analytics/{survey_id}`
- **Success Response**: `AnalyticsSchema`

## Schemas

### UserSchema

```json
{
  "id": "UUID",
  "username": "string",
  "email": "string",
  "password": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### SurveySchema

```json
{
  "id": "UUID",
  "title": "string",
  "description": "string",
  "questions": "List[QuestionSchema]",
  "created_by": "UUID",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### QuestionSchema

```json
{
  "id": "UUID",
  "survey_id": "UUID",
  "text": "string",
  "response_type": "string",
  "options": "List[string]",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### ResponseSchema

```json
{
  "id": "UUID",
  "survey_id": "UUID",
  "question_id": "UUID",
  "respondent_id": "UUID",
  "response": "string",
  "created_at": "datetime"
}
```

### AnalyticsSchema

```json
{
  "survey_id": "UUID",
  "total_responses": "integer",
  "sentiment_analysis": "Map[string, float]",
  "keyword_extraction": "List[string]"
}
```

## Error Handling

All endpoints return standard HTTP status codes. In the case of an error, the response will include a message describing the issue.

## Integration Endpoints

For integrating with Carta and CRM platforms, please refer to the `integration_guide.md` document.

## Conclusion

This API documentation covers the main operations you can perform with the Olvy Customer Survey Tool. For more detailed information on setup, deployment, and usage, please refer to the respective documentation files in the `docs` directory.