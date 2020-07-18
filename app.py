from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL") or 'postgres://postgres:postgres@localhost/flask-hw'
print(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def hello_world():
    #return 'Hello World!'
    #users = db.User.all()
    return render_template("index.html")

@app.route('/data')
def data():
    # QUERY the DB
    data = [1,2,3]
    return jsonify(data)

if __name__ == '__main__':
    app.run()