from app import db
from flask_login import UserMixin
import config
import os
import pandas as pd

class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False, unique=True)
    country = db.Column(db.String(64))
    publisher = db.Column(db.String(64), nullable=False)
    review = db.relationship('Review', backref='journal')


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    email_confirmed = db.Column(db.Integer, nullable=False, default=0)
    password = db.Column(db.String(64), nullable=False)
    profile_pic = db.Column(db.String(64), default='/static/images/profile_pictures/default_avatar.png')
    review = db.relationship('Review', backref='user')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.String(64))
    time_stamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    journal_id = db.Column(db.Integer, db.ForeignKey('journal.id'))

def create_db():
    '''
    Builds the database by writing each row of the journal_list.csv to a sqlite database. Should really only be needed
    once to set up database upon initial deployment.
    '''
    print('Creating database...')
    db.create_all()

    # Populate Journals table

    df = pd.read_csv('data/journal_list.csv', sep=';')
    df_drop_dup = df.drop_duplicates(['Title'])
    df_drop_na = df_drop_dup.dropna(subset=['Publisher'])

    for index, row in df_drop_na.iterrows():
        entry = Journal(
                         title=row['Title'],
                         country=row['Country'],
                         publisher=row['Publisher'])
        db.session.add(entry)
    print('Populating database, this may take a long time...')
    db.session.commit()
    print('Database is ready')
    print('App is ready')


# Create sqlite database if it does not exist
if not os.path.exists(config.database_path):
    create_db()

