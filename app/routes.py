from flask import render_template, jsonify, request
from app import app
from app.models import Journals
from pprint import pprint
import json
import pandas as pd
import sqlite3


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/table_result')
def table_result():
    input_data = json.loads(request.values.get("args"))
    con = sqlite3.connect('database.sqlite3')
    df = pd.read_sql_query('SELECT title, country, publisher, rating FROM journals', con)
    sub = df[:5]
    sub_list = sub.values.tolist()
    results = {}
    results['draw'] = input_data['draw']
    results['recordsTotal'] = df.shape[0]
    results['recordsFiltered'] = df.shape[0]
    results['data'] = sub_list
    pprint(input_data)
    return jsonify(results)
