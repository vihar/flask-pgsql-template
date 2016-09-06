from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/hello'

db = SQLAlchemy(app)


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self,name,description):
        self.name = name
        self.description = description

class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(80), unique=True)
    posttext = db.Column(db.String(255))

    def __init__(self,title,posttext):
        self.title = title
        self.posttext = posttext


@app.route('/')
def index():
    return "Hello World"
app = Flask(__name__)

if __name__ == "__main__":
    app.run()
