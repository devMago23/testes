from fastapi.testclient import TestClient

from fast_zero.app import app

import pytest


@pytest.fixture
def client():
    return TestClient(app)
