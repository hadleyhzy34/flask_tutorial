from flask import Flask
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import yaml

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'c4126f5f37caf566f531034d394187bc'

# create connection between flask and mysql database
d2f = yaml.load(open('db.yaml'))
engine = create_engine('mysql+pymysql://'+d2f['mysql_user']+':'+d2f['mysql_password']+'@'+d2f['mysql_host']+'/'+d2f['mysql_db'])
# db = SQLAlchemy(app)






# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(20), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}','{self.email}','{self.image_file}')"


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)

#     def __repr__(self):
#         return f"Post('{self.title}','{self.date_posted}')"


# db.create_all()

# admin = User('hadley2', 'hadle2@162.com')

# db.session.add(admin)

# db.session.commit()


