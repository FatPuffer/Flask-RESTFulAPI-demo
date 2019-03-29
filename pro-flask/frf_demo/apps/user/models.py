# coding: utf-8

from frf_demo import db
from werkzeug.security import generate_password_hash, check_password_hash
from ..db.base_model import BaseModel


class User(BaseModel, db.Model):
    """User"""
    __tablename__ = "frf_user_profile"

    id = db.Column(db.Integer, primary_key=True)
    # nullable = False: 不能为空
    name = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    mobile = db.Column(db.String(11), unique=True, nullable=False)

    @property
    def password(self):
        """called on get password attributes"""
        raise AttributeError('not readable')

    @password.setter
    def password(self, passwd):
        """called on set password attributes , set encrypted password"""
        self.password_hash = generate_password_hash(passwd)

    def check_password(self, passwd):
        """check password correctness"""
        return check_password_hash(self.password_hash, passwd)
