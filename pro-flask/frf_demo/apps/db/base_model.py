from datetime import datetime
from frf_demo import db


class BaseModel(object):
    """Base Model"""
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
