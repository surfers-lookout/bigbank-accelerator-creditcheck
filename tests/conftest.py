import pytest
from main import create_app
from fastapi.testclient import TestClient

@pytest.fixture(scope="session")
def app():
    app = create_app()
    return app


@pytest.fixture(scope='module')
def new_dummy(app):
    from main.data.models import Dummy
    _dummy = Dummy(name='FancyName',
                comment='Some random comment')
    return _dummy


@pytest.fixture(scope='module')
def test_client(app):
    testing_client = TestClient(app)
    yield testing_client  # this is where the testing happens
