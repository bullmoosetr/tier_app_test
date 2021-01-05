import random, string
from tier_app.models import Url, db

def get_or_create_shortened_url(url):
    if url and isinstance(url, str):
       # Check if URL exist and if so return entry
        existing_url = Url.query.filter_by(original_url=url).first()
        if existing_url:
           return existing_url
        else:
            # Create a new Url
            # This will be the code used to find the stored Url and redirect
            unique_id = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(7))
            new_url = Url(url, unique_id)
            db.session.add(new_url)
            db.session.commit()
            return new_url

def get_original_url(short_url_code):
    if len(short_url_code) == 7:
        long_url = Url.query.filter_by(new_url=short_url_code).first()
        if long_url:
            return long_url.original_url
        else:
            return None #"No Url found with that code :("
    else:
        return None #"The Url Code is too short take another look"
