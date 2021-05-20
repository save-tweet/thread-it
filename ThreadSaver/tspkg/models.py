from tspkg import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20), unique=True, nullable=False)
    tweet = db.Column(db.Text, nullable=False)
    screen_name = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.user_id}', '{self.tweet}', '{self.screen_name}')"
