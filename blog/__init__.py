from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '4090b112f4ca6b3972ca1deab52b71fd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # specify db location

db = SQLAlchemy(app) # create db instance
bcrypt = Bcrypt(app) # for hashing password
login_manager = LoginManager(app)
login_manager.login_view = 'login' # for redirect when trying to access to account page as logout
login_manager.login_message_category = 'info' # for alert message |^

from blog import routes