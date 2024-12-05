import requests
from requests.auth import HTTPBasicAuth

class APISession:
    def __init__(self, base_url, username=None, password=None):
        self.base_url = base_url
        self.session = requests.Session()
        if username and password:
            self._login(username, password)

    def _login(self, username, password):
        response = self.session.post(
            f"{self.base_url}/auth",
            auth=HTTPBasicAuth(username, password)
        )
        response.raise_for_status()
        access_token = response.json().get("access_token")
        if access_token:
            self.session.headers.update({'Authorization': f'Bearer {access_token}'})
        else:
            raise ValueError("Access token not found in response.")

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, params=params)

    def post(self, endpoint, data=None, json=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, data=data, json=json)

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
