from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/hellomydarling'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


# Write your models here.

#class Snippet(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String(128))
#   def __init__(self, name):
#  	self.name = name

if __name__ == '__main__':
    manager.run()

