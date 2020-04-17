from flask_login import UserMixin
from .extensions import mongo
import uuid


class User(UserMixin):
    def __init__(self, username, password, _id=None):
        self.username = username
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self._id)

    @classmethod
    def get_by_id(cls, _id):
        data = mongo.db.users.find_one({"_id": _id})
        if data is not None:
            return cls(**data)
