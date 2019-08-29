from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '4090b112f4ca6b3972ca1deab52b71fd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # specify db location

db = SQLAlchemy(app) # create db instance

from blog import routes