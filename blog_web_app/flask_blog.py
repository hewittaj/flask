from crypt import methods
from distutils.log import debug
from sre_constants import SUCCESS
from flask import Flask, redirect, render_template, url_for, flash
from forms import RegistrationForm, LoginForm
app = Flask(__name__, template_folder="templates")

app.config['SECRET_KEY'] = '981d3f4b6d95a2b9606cf10c746d9ffd' # make environment variable?

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