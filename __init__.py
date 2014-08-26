from flask import Flask, jsonify, request
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cranberry@localhost/development'

db.init_app(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/get_user/<user_id>")
def get_user(user_id):
    user = User.query.filter_by(uid=user_id).first()
    response = {}
    response['status'] = 'success'
    response['name'] = user.name
    response['email'] = user.email
    response['biography'] = user.biography
    response['password'] = user.password
    response['user_id'] = user.uid
    return jsonify(response)

@app.route("/create_new_user", methods=['POST', 'GET'])
def create_new_user():
    response = {}
    if request.method == 'POST':
        if 'name' in request.form and 'email' in request.form and 'password' in request.form and 'biography' in request.form:
            new_user = User(request.form['name'], request.form['email'], request.form['password'], request.form['biography'])
            if len(User.query.filter_by(email=request.form['email']).all()) == 0:
                db.session.add(new_user)
                db.session.commit()
                response['status'] = 'success'
                saved_user = User.query.filter_by(email=request.form['email']).first()
                response['user_id'] = saved_user.uid
            else:
                response['status'] = 'already exists'
        else:
            response['status'] = 'incomplete'
    else:
        response['status'] = 'you must post'
    return jsonify(response)

if __name__ == "__main__":
    app.run()
