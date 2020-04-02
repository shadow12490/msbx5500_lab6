from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

# add cross-origin allow to all routes
CORS(app)

########
### PSQL
########
# get psql db up. quickstart here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self

@app.route('/db_test')
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)

###########
### MONGODB
###########
# get a mongodb up
app.config["MONGO_URI"] = os.getenv('MONGODB_URI')
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
