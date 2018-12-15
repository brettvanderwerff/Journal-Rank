from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = config.configurations['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = config.configurations['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.configurations['SQLALCHEMY_TRACK_MODIFICATIONS']
db = SQLAlchemy(app)
login_manager = LoginManager(app)



from app import routes, models