```python
import requests
from typing import Any, Dict

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def send_request(self, method: str, endpoint: str, payload: Dict[str, Any] = None, headers: Dict[str, str] = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        if method == "GET":
            response = requests.get(url, params=payload, headers=headers)
        elif method == "POST":
            response = requests.post(url, json=payload, headers=headers)
        elif method == "PUT":
            response = requests.put(url, json=payload, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        return response

    def get(self, endpoint: str, payload: Dict[str, Any] = None, headers: Dict[str, str] = None) -> requests.Response:
        return self.send_request("GET", endpoint, payload, headers)

    def post(self, endpoint: str, payload: Dict[str, Any] = None, headers: Dict[str, str] = None) -> requests.Response:
        return self.send_request("POST", endpoint, payload, headers)

    def put(self, endpoint: str, payload: Dict[str, Any] = None, headers: Dict[str, str] = None) -> requests.Response:
        return self.send_request("PUT", endpoint, payload, headers)

    def delete(self, endpoint: str, headers: Dict[str, str] = None) -> requests.Response:
        return self.send_request("DELETE", endpoint, headers=headers)
```
