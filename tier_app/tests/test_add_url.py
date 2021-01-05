import pytest
from tier_app import create_app
from tier_app.models import Url


TEST_URL = "https://testing/test.com"

def test_add_new_url(app, client):
    client.post('/shorten_url', data={'long_url':TEST_URL})
    with app.app_context():
        assert Url.query.filter_by(original_url=TEST_URL).first().original_url == TEST_URL
