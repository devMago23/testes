import pytest

from fastapi.testclient import TestClient

from fast_zero.app import app

from fast_zero.database import get_Section

@pytest.fixture
def Client():
    def get_session_override(sesssion):
        return session
    with TestClient(app) as Client:
        app.dependency_overrides[get_Section] == get_session_override 
        yield Client 
    app.dependency_overrides.clear()


from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fast_zero.models import table_registry
from sqlalchemy.pool import StaticPool

@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
                           
    )

    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
     yield session

    table_registry.metadata.drop_all(engine)
