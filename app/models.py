from app import db
import os
import config
import pandas as pd


class Journals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False, unique=True)

# Create sqlite database if it does not exits
if not os.path.exists(config.database_path):
    print('Creating database...')
    db.create_all()

#Populate Journals table
    items = ['test1', 'test2']
    df = pd.read_csv('journal_list.csv', sep=';')
    for item in df[df.Type == 'journal']['Title']:
        print('Adding {}'.format(item))
        entry = Journals(title=item)
        db.session.add(entry)
    print('Committing')
    db.session.commit()

    print('Done')