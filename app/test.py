"""test for project"""

import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module", name="test_client")
def client():
    """client module fixture"""
    return TestClient(app)


def test_root(test_client):
    """testt root url"""
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == "Root page"


def test_path_variable_url(test_client):
    """testt path variable url"""
    response = test_client.get("/hi/path/Spain")
    assert response.status_code == 200
    assert response.json() == "Hello Spain"


def test_query_variable_url(test_client):
    """testt query variable url"""
    who = "Italy"
    response = test_client.get("/hi/query", params={"who": who})
    assert response.status_code == 200
    assert response.json() == f"Hello {who}"


def test_say_hi_body(test_client):
    """test base type body variable url"""
    who = "Moldova"
    others = "others"
    response = test_client.post("/hi/body", json={"who": who})
    assert response.status_code == 200
    assert response.json() == f"Hello {who} and {others}"


def test_say_hi_body_two_params(test_client):
    """test base type body variable url. two params"""
    who = "Moldova"
    other = "Serbia"
    response = test_client.post("/hi/body", json={"who": who, "other": other})
    assert response.status_code == 200
    assert response.json() == f"Hello {who} and {other}"


def test_say_hi_additional_header(test_client):
    """test header variable url"""
    who = "Moldova"
    response = test_client.post("/hi/header", headers={"who": who})
    assert response.status_code == 200
    assert response.json() == f"Hello {who}"
