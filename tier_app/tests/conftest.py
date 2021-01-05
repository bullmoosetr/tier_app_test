import pytest
from tier_app import create_app, db
from tier_app.models import Url
from flask import current_app

@pytest.fixture(scope='module')
def app():
    app = create_app(test_config=True)

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
