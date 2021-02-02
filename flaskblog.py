from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c4126f5f37caf566f531034d394187bc'

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
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='register', form=form)    

# login page
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)  

if __name__== '__main__':
    app.run(debug=True)