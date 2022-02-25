from datetime import datetime
from flask_blog import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(20), nullable=False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref="Author", lazy=True)

    # how our object is printed when printed out.
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # how our object is printed when printed out.
    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"