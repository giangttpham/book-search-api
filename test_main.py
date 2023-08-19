from fastapi.testclient import TestClient

from main import app
import pytest

client = TestClient(app)


class TestBookApi:
    def test_get_book(self):
        response = client.get("/books/frankeinstein")

        assert response.status_code == 200
