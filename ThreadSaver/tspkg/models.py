from tspkg import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20))
    tweet = db.Column(db.String(2560))

    def __repr__(self):
        return f"User('{self.user_id}', '{self.tweet}')"
