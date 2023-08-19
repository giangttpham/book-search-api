from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app
import pytest

client = TestClient(app)


@pytest.fixture(autouse=True)
def test_get_book():
    response = client.get("/books/frankeinstein")

    assert response.status_code == 200
