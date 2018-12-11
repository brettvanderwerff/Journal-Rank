import os

database_name = 'database.sqlite3'

basedir = os.path.abspath(os.path.dirname(__file__))

database_path = os.path.join(basedir, database_name)

configurations = {}

configurations['SECRET_KEY'] = 'secret'
configurations['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
configurations['SQLALCHEMY_TRACK_MODIFICATIONS'] = False