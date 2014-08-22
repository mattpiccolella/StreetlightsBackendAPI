from flask import Flask
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cranberry@localhost/development'

db.init_app(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/newfacebookuser/<first>/<last>/<email>/<facebook_id>/<photo_url>")
def new_facebook_user(first, last, email, facebook_id, photo_url):
    newfacebookuser = User(first, last, email, facebook_id, photo_url)
    db.session.add(newfacebookuser)
    db.session.commit()
    return "Successfully created a new user."

if __name__ == "__main__":
    app.run()
