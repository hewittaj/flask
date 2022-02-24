from distutils.log import debug
from flask import Flask, render_template, url_for
app = Flask(__name__, template_folder="templates")


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


"""Help
Instead of typing 'flask run' into terminal we can just run the python file and it will run the code
"""
if __name__ == '__main__':
    app.run(debug=True)