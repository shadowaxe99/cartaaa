# Olvy - Customer Survey Tool Usage Guide

Welcome to the Olvy Customer Survey Tool. This document will guide you through the usage of the platform to create, distribute, and analyze surveys for your stakeholders.

## Getting Started

Before you begin, ensure you have the following prerequisites:

- An account on Olvy with appropriate permissions.
- The `.env` file configured with your `DATABASE_URL`, `OPENAI_API_KEY`, `CARTA_API_KEY`, and `CRM_API_KEY`.

## Creating a Survey

To create a survey, follow these steps:

1. Log in to your Olvy account.
2. Navigate to the Survey Creation section using the `Navbar` component.
3. Click on the "Create Survey" button.
4. Fill out the `survey-form` with your questions and select the response type for each.
5. Set the survey expiration date and response limit as needed.
6. Save the survey to create it.

## Distributing a Survey

Once a survey is created, you can distribute it through the following methods:

1. Go to the Survey List section using the `Navbar` component.
2. Find the survey you wish to distribute and select "Distribute".
3. Choose to share via email, embed on your website, or share on social media.
4. If needed, restrict access to specific individuals or groups.

## Collecting Responses

Responses are collected automatically when respondents submit their answers. To view responses:

1. Navigate to the Survey List section.
2. Click on the "View Responses" button next to the relevant survey.

## Analyzing Survey Responses

To analyze the responses and gain insights:

1. In the Survey List section, select "Analyze" for the survey you are interested in.
2. The `SurveyAnalytics` component will display the results with sentiment analysis, keyword extraction, and other analytics features.
3. Use the `analytics-chart` to visualize the data.

## Integration with Carta and CRM

Olvy integrates with Carta and CRM platforms to enhance your experience:

- To integrate with Carta, use the `integrateCarta` function provided in the `backend/integrations/carta_integration.py` file.
- For CRM integration, refer to the `backend/integrations/crm_integration.py` file and use the `integrateCRM` function.

## Conclusion

The Olvy Customer Survey Tool is designed to be intuitive and user-friendly. For detailed API documentation, refer to `docs/api_documentation.md`. For setup instructions, see `docs/setup.md`. If you encounter any issues or have questions, consult the `README.md` file for support and contact information.

Thank you for choosing Olvy for your cap table management and stakeholder feedback needs.