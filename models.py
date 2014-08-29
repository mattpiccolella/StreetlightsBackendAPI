from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

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

    def toJSON(self):
        json = {}
        json['user_id'] = self.uid
        json['name'] = self.name
        return json

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
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.user_id = user_id
        self.created = datetime.now()
        self.expiration = self.created + timedelta(minutes = int(expiration_minutes))

    def toJSON(self):
        json = {}
        json['stream_item_id'] = self.stream_item_id
        json['description'] = self.description
        json['latitude'] = self.latitude
        json['longitude'] = self.longitude
        json['created'] = unix_time_millis(self.created)
        json['expiration'] = unix_time_millis(self.expiration)
        return json
        
def unix_time_millis(dt):
    epoch = datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return delta.total_seconds()
    
