from flask import render_template
from app import app
from app.models import Journals

@app.route('/')
@app.route('/index')
def index():
    column_names = ['Journal Title', 'Publisher', 'Country', 'Rating']
    query = Journals.query.with_entities(Journals.title, Journals.publisher, Journals.country, Journals.rating).all()
    return render_template('index.html', column_names=column_names, query=query)

