from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from model import User, Post
import yaml


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c4126f5f37caf566f531034d394187bc'

# create connection between flask and mysql database
d2f = yaml.load(open('db.yaml'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+d2f['mysql_user']+':'+d2f['mysql_password']+'@'+d2f['mysql_host']+'/'+d2f['mysql_db']
db = SQLAlchemy(app)

posts = [
    {
        'author': 'Hadley',
        'title':'blog post1',
        'content': 'first post content',
        'date_posted': 'april 20,2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'second blog post',
        'content': 'whatever this is',
        'date_posted': 'september 1,2016'
    }
]


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(20), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}','{self.email}','{self.image_file}')"

# root page for our web page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

# about page
@app.route("/about")
def about():
    return render_template('about.html', title='about')


# registration page
# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='register', form=form)   

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        if request.method == 'POST':
            # db.create_all()
            admin = User(form.username.data, form.email.data, form.password.data)
            db.session.add(admin)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)   

# login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        result = db.session.execute(f'select * from User where User.email = \'{form.email.data}\';')
        # result = User.query.filter_by(email=form.email.data).first()
        if result:
        # if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)  


if __name__== '__main__':
    app.run(debug=True)