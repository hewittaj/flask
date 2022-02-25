# Where we initialize application and bring together components.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")

app.config['SECRET_KEY'] = '981d3f4b6d95a2b9606cf10c746d9ffd' # make environment variable?
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flask_blog import routes