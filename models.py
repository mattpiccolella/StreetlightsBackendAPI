from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    facebook_id = db.Column(db.String(100))
    photo_url = db.Column(db.String(200))

    def __init__(self, firstname, lastname, email, facebook_id, photo_url):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.facebook_id = facebook_id
        self.photo_url = photo_url

