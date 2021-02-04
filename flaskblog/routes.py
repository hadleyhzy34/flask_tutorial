from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
import yaml

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