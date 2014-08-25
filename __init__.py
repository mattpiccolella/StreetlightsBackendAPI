from flask import Flask, jsonify, request
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

@app.route("/create_new_user", methods=['POST', 'GET'])
def create_new_user():
    response = {}
    if request.method == 'POST':
        if 'name' in request.form and 'email' in request.form and 'password' in request.form and 'biography' in request.form:
            response['status'] = 'SUCCESS'

        else:
            response['status'] = 'INCOMPLETE'
    else:
        response['status'] = 'FAILURE'
    return jsonify(response)

if __name__ == "__main__":
    app.run()
