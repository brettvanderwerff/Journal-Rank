from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from flask_login import LoginManager
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
app.secret_key = config.configurations['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = config.configurations['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.configurations['SQLALCHEMY_TRACK_MODIFICATIONS']
app.config.update(
    DEBUG=True,
	MAIL_SERVER=config.configurations['MAIL_SERVER'],
	MAIL_PORT=config.configurations['MAIL_PORT'],
	MAIL_USE_SSL=config.configurations['MAIL_USE_SSL'],
	MAIL_USERNAME = config.configurations['MAIL_USERNAME'],
	MAIL_PASSWORD = config.configurations['MAIL_PASSWORD']
)


db = SQLAlchemy(app)
login_manager = LoginManager(app)
mail = Mail(app)
serial = URLSafeTimedSerializer(app.secret_key)

from app import routes, models