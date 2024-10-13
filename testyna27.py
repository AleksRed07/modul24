import pytest
from api import api

API_KEY = "your_api_key"

class TestApi:

    @pytest.fixture(scope="class")
    def api(self):
        return api(API_KEY)


    def test_get_items(self, api):
        response = api.get_items()
        assert response.status_code == 200
        assert isinstance(response.json(), list)


    def test_get_items_invalid_api_key(self):
        api = api("invalid_key")
        response = api.get_items()
        assert response.status_code == 401


    def test_update_item(self, api):
        item_id = 1
        update_data = {"name": "Updated Item"}
        response = api.update_item(item_id, update_data)
        assert response.status_code == 200
        assert response.json()["name"] == "Updated Item"


    def test_update_non_existing_item(self, api):
        item_id = 9999
        update_data = {"name": "Non-existing Item"}
        response = api.update_item(item_id, update_data)
        assert response.status_code == 404


    def test_delete_item(self, api):
        item_id = 2
        response = api.delete_item(item_id)
        assert response == 204


    def test_delete_non_existing_item(self, api):
        item_id = 9999
        response = api.delete_item(item_id)
        assert response == 404


    def test_create_item_success(self, api):
        item_data = {"name": "New Item", "description": "Valid description"}
        response = api.create_item(item_data)
        assert response.status_code == 201


    def test_create_item_with_long_name(self, api):
        item_data = {"name": "A" * 300}
        response = api.create_item(item_data)
        assert response.status_code == 400


    def test_create_item_invalid_data(self, api):
        item_data = {"invalid_field": "Invalid"}
        response = api.create_item(item_data)
        assert response.status_code == 400


    def test_create_item_empty(self, api):
        response = api.create_item({})
        assert response.status_code == 400
