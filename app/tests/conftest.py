"""Test fixtures"""

import pytest
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from app.database import Base, engine
from app.main import app


@pytest.fixture(scope="session", name="test_client")
def client():
    """client module fixture"""
    return TestClient(app)


@pytest.fixture(scope="session")
def db_session():
    """
    Initiate db session
    Rollback and close it after tests
    """
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.rollback()
    session.close()
