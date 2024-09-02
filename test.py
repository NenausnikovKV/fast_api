import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello world"


def test_path_variable_url(client):
    response = client.get("/hi/Spain")
    assert response.status_code == 200
    assert response.json() == "Hello Spain"


def test_query_variable_url(client):
    who = "Italy"
    response = client.get("/hi", params={"who": who})
    assert response.status_code == 200
    assert response.json() == f"Hello {who}"


def test_say_hi_body(client):
    who = "Moldova"
    others = "others"
    response = client.post("/hi_body", json={"who": who})
    assert response.status_code == 200
    assert response.json() == f"Hello {who} and {others}"


def test_say_hi_body_two_params(client):
    who = "Moldova"
    other = "Serbia"
    response = client.post("/hi_body", json={"who": who, "other": other})
    assert response.status_code == 200
    assert response.json() == f"Hello {who} and {other}"


def test_say_hi_additional_header(client):
    who = "Moldova"
    response = client.post("/hi_header", headers={"who": who})
    assert response.status_code == 200
    assert response.json() == f"Hello {who}"
