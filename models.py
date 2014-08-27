from flask.ext.sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100))
    biography = db.Column(db.String(150))
    stream_items = db.relationship('StreamItem', backref='user', lazy='dynamic')

    def __init__(self, name, email, password, biography):
        self.name = name.title()
        self.email = email.lower()
        self.password = password
        self.biography = biography

class StreamItem(db.Model):
    __tablename__ = 'streamitems'
    stream_item_id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(150))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'))
    created = db.Column(db.DateTime)
    expiration = db.Column(db.DateTime)

    def __init__(self, description, latitude, longitude, user_id, expiration_minutes):
        self.name = description
        self.latitude = latitude
        self.longitude = longitude
        user_id = user_id
        created = datetime.now()
        expired = created + datetime.timedelta(minutes = int(expiration_minutes))
        

    
