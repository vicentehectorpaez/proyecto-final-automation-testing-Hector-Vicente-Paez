import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Accept": "application/json"
        }

    def get(self, endpoint):
        return requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)
    
    def post(self, endpoint, payload):
        return requests.post(f"{self.base_url}/{endpoint}", json=payload, headers=self.headers)

    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}/{endpoint}", headers=self.headers)
         