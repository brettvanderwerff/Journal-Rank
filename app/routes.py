from flask import render_template, jsonify, request
from app import app
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
    search_term = input_data['search']['value']
    if search_term != '':
        df = df[df['title'].str.contains(search_term, case=False) | df['country'].str.contains(search_term, case=False)]
    sort_info = input_data['order'][0]
    sort_index = int(sort_info['column'])
    sort_column = list(df.columns.values)[sort_index]
    sort_dir = True if sort_info['dir'] == 'asc' else False
    sorted_df = df.sort_values(by=sort_column, ascending=sort_dir)
    start_index = int(input_data['start'])
    stop_index = int(input_data['start']) + int(input_data['length'])
    sub = sorted_df[start_index : stop_index]
    sub_list = sub.values.tolist()
    results = {}
    results['draw'] = input_data['draw']
    results['recordsTotal'] = df.shape[0]
    results['recordsFiltered'] = df.shape[0]
    results['data'] = sub_list
    return jsonify(results)
