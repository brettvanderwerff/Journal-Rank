from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.configurations['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.configurations['SQLALCHEMY_TRACK_MODIFICATIONS']
db = SQLAlchemy(app)

class Journals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sourceid = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(64), nullable=False, unique=True)
    total_docs_2017 = db.Column(db.String(64))
    total_docs_3_years = db.Column(db.String(64))
    total_refs = db.Column(db.String(64))
    total_cites_3_years = db.Column(db.String(64))
    citable_docs_3_years = db.Column(db.String(64))
    cites_per_doc_2_years = db.Column(db.String(64))
    refs_per_doc = db.Column(db.String(64))
    country = db.Column(db.String(64))
    publisher = db.Column(db.String(64), nullable=False)
    rating = db.Column(db.String(64))


def create_db():
    '''
    Builds the database by writing each row of the journal_list.csv to a sqlite database
    '''
    print('Creating database...')
    db.create_all()

    # Populate Journals table

    df = pd.read_csv('journal_list.csv', sep=';')
    df_drop_dup = df.drop_duplicates(['Title'])
    df_drop_na = df_drop_dup.dropna(subset=['Publisher'])
    current_time = datetime.now()

    counter = 0
    for index, row in df_drop_na.iterrows():
        print(counter / df_drop_na.shape[0], " percent complete writing to database")
        entry = Journals(sourceid=row['Sourceid'],
                         title=row['Title'],
                         total_docs_2017=row['Total Docs. (2017)'],
                         total_docs_3_years=row['Total Docs. (3years)'],
                         total_refs=row['Total Refs.'],
                         total_cites_3_years=row['Total Cites (3years)'],
                         citable_docs_3_years=row['Citable Docs. (3years)'],
                         cites_per_doc_2_years=row['Cites / Doc. (2years)'],
                         refs_per_doc=row['Ref. / Doc.'],
                         country=row['Country'],
                         publisher=row['Publisher'])
        db.session.add(entry)
        db.session.commit()
        counter += 1

    elapsed_time = datetime.now() - current_time
    print('Elapsed time was {}'.format(elapsed_time))


if __name__ == '__main__':
    # Create sqlite database if it does not exits
    if not os.path.exists(config.database_path):
        create_db()