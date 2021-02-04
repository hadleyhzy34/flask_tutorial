from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
import yaml


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c4126f5f37caf566f531034d394187bc'

# create connection between flask and mysql database
d2f = yaml.load(open('db.yaml'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+d2f['mysql_user']+':'+d2f['mysql_password']+'@'+d2f['mysql_host']+'/'+d2f['mysql_db']
db = SQLAlchemy(app)