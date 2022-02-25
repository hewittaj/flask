from crypt import methods
from datetime import datetime
from distutils.log import debug
from sre_constants import SUCCESS
from flask import Flask, redirect, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__, template_folder="templates")

app.config['SECRET_KEY'] = '981d3f4b6d95a2b9606cf10c746d9ffd' # make environment variable?
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(20), nullable=False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref="Author", lazy=True)

    # how our object is printed when printed out.
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # how our object is printed when printed out.
    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"

posts = [
    {
    'author': 'Alex Hewitt',
    'title': 'Creating a blog',
    'content': 'I created a blog.',
    'date_posted': 'February 24, 2022'
    },
    {
    'author': 'Kristen Hewitt',
    'title': 'Reading a blog',
    'content': 'I read a blog.',
    'date_posted': 'February 24, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for: {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You are logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title="Login", form=form)

"""Help
Instead of typing 'flask run' into terminal we can just run the python file and it will run the code
"""
if __name__ == '__main__':
    app.run(debug=True)