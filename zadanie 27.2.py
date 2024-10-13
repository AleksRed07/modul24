import requests

class Api:
    BASE_URL = "https://api.example.com"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_headers(self):
        return {"Authorization": f"Bearer {self.api_key}"}


    def get_items(self):
        response = requests.get(f"{self.BASE_URL}/items", headers=self.get_headers())
        return response.json()


    def update_item(self, item_id, update_data):
        response = requests.put(f"{self.BASE_URL}/items/{item_id}", headers=self.get_headers(), json=update_data)
        return response.json()

    def delete_item(self, item_id):
        response = requests.delete(f"{self.BASE_URL}/items/{item_id}", headers=self.get_headers())
        return response.status_code
