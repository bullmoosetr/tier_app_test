import datetime
from . import db

class Url(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2083))
    new_url = db.Column(db.String(7), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, original_url=None, new_url=None, created_at=None):
        self.original_url = original_url
        self.new_url = new_url
        self.created_at = created_at
    
    def __repr__(self):
        return "<Url(long_url='%s', shortened_url_code='%s', created_at='%s')>" % (
                                self.original_url, self.new_url, self.created_at)
