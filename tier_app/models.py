import datetime
from sqlalchemy import Column, Integer, String, DateTime
from . import db
from tier_app.db import Base

class Url(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    original_url = Column(String(2083))
    new_url = Column(String(7), unique=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, original_url=None, new_url=None, created_at=None):
        self.original_url = original_url
        self.new_url = new_url
        self.created_at = created_at
    
    def __repr__(self):
        return "<Url(long_url='%s', shortened_url_code='%s', created_at='%s')>" % (
                                self.original_url, self.new_url, self.created_at)

# create_all()
# session.commit()