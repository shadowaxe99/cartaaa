```python
import os
import requests
from typing import Optional, Dict, Any

# Shared dependencies
CARTA_API_KEY = os.getenv('CARTA_API_KEY')

class CartaIntegrationException(Exception):
    pass

class CartaClient:
    """
    This class handles the integration with Carta's API for cap table management.
    It provides methods to import and export data to and from the Olvy platform.
    """

    BASE_URL = 'https://api.carta.com'

    def __init__(self, api_key: str = CARTA_API_KEY):
        if not api_key:
            raise CartaIntegrationException("Missing Carta API key")
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def _send_request(self, method: str, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Sends a request to the Carta API.

        :param method: HTTP method (e.g., 'GET', 'POST', 'PUT', 'DELETE').
        :param endpoint: API endpoint to be appended to the base URL.
        :param data: Optional dictionary containing the JSON payload.
        :return: JSON response from the API.
        """
        url = f'{self.BASE_URL}{endpoint}'
        try:
            response = requests.request(method, url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            raise CartaIntegrationException(f"HTTPError: {e.response.text}") from e
        except requests.exceptions.RequestException as e:
            raise CartaIntegrationException(f"RequestException: {e}") from e

    def import_cap_table(self, company_id: str) -> Dict[str, Any]:
        """
        Imports the cap table data from Carta for a given company.

        :param company_id: The unique identifier for the company in Carta.
        :return: Cap table data.
        """
        endpoint = f'/companies/{company_id}/cap_table'
        return self._send_request('GET', endpoint)

    def export_cap_table(self, company_id: str, cap_table_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Exports the cap table data to Carta for a given company.

        :param company_id: The unique identifier for the company in Carta.
        :param cap_table_data: The cap table data to be exported.
        :return: Response from the Carta API.
        """
        endpoint = f'/companies/{company_id}/cap_table'
        return self._send_request('POST', endpoint, data=cap_table_data)

# Example usage:
# carta_client = CartaClient()
# try:
#     cap_table = carta_client.import_cap_table('company_id_123')
#     print(cap_table)
#     response = carta_client.export_cap_table('company_id_123', {'data': 'new cap table data'})
#     print(response)
# except CartaIntegrationException as e:
#     print(f"An error occurred: {e}")
```