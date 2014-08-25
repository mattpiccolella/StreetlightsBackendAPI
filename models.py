from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100))
    biography = db.Column(db.String(150))

    def __init__(self, name, email, password, biography):
        self.name = name.title()
        self.email = email.lower()
        self.password = password
        self.biography = biography

