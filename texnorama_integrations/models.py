from . import db


class Post(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    msg_id = db.Column(db.Integer, nullable=True)
