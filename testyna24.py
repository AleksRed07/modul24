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

    def test_create_item_success(self, api):
        item_data = {"name": "New Item", "description": "Item description"}
        response = api.create_item(item_data)
        assert response.status_code == 201
        assert response.json()["name"] == "New Item"

    def test_create_item_without_name(self, api):
        item_data = {"description": "Item without name"}
        response = api.create_item(item_data)
        assert response.status_code == 400

    def test_create_item_with_long_name(self, api):
        item_data = {"name": "A" * 100, "description": "Item with long name"}
        response = api.create_item(item_data)
        assert response.status_code == 400

    def test_delete_item_success(self, api):
        item_id = 1
        response = api.delete_item(item_id)
        assert response == 204

    def test_delete_non_existing_item(self, api):
        item_id = 9999
        response = api.delete_item(item_id)
        assert response == 404

    def test_get_items_with_invalid_api_key(self):
        api = api("invalid_api_key")
        response = api.get_items()
        assert response.status_code == 401

    def test_create_item_with_invalid_data(self, api):
        item_data = {"invalid_field": "Invalid"}
        response = api.create_item(item_data)
        assert response.status_code == 400

    def test_create_item_with_empty_data(self, api):
        response = api.create_item({})
        assert response.status_code == 400

    def test_create_item_with_extra_fields(self, api):
        item_data = {"name": "Item with extra fields", "extra_field": "Extra"}
        response = api.create_item(item_data)
        assert response.status_code == 400
