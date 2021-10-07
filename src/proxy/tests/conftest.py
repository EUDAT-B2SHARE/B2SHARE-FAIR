import pytest
from falcon import testing

from proxy.app import app


@pytest.fixture()
def client():
    return testing.TestClient(app)
