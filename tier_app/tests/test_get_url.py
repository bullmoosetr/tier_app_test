import pytest
import string, random
from tier_app import create_app
from tier_app.models import Url


TEST_URL = "https://testing_get/test.com"
NEW_URL = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(7))
def setUp(app, client):
    with app.app_context():
        # Add Some Data
        new_url = Url(TEST_URL, NEW_URL)
        db.session.add(new_url)
        db.session.commit()

def test_get_url(app, client):
    assert client.get(f'tier.app/{NEW_URL}').status_code == 200
