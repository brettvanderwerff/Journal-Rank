from flask import render_template, jsonify, request, flash, redirect, url_for
from app import app, login_manager, db
import json
import pandas as pd
import sqlite3
from app.models import Journals, User
from app.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', logged_in=current_user.is_authenticated)

@app.route('/journal_info/<journal_name>')
def journal_info(journal_name):
    journal_name = journal_name.replace('_', ' ')
    journal_data = Journals.query.filter_by(title=journal_name).first()
    data_dict = {}
    data_dict['Journal Title'] = journal_data.title
    data_dict['Publisher'] = journal_data.publisher
    data_dict['Country'] = journal_data.country
    return render_template('journal_info.html', data_dict=data_dict, logged_in=current_user.is_authenticated)


@app.route('/table_result')
def table_result():

    def parse_query_string(query_string, column_names):
        '''
        Parses query string to determine what values should be used to query the database
        :param query_string: the query string from the web app response
        :param column_names: a list of column names to be queried from the database
        :return:
        '''
        query_values = {}
        query_values['search_term'] = '_' if query_string['search']['value'] == '' else query_string['search']['value']
        query_values['start_index'] = query_string['start']
        query_values['length'] = query_string['length']
        query_values['sort_column'] = column_names[int(query_string['order'][0]['column'])]
        query_values['sort_dir'] = 'ASC' if query_string['order'][0]['dir'] == 'asc' else 'DESC'
        return query_values

    def get_table_length(con, table):
        '''
        Determines The length of a table within a databse
        :param db: the database uri
        :param table: the table name
        :return: the length of the table as a string
        '''
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM {}".format(table))
        table_length = cur.fetchone()[0]
        return table_length


    def build_table(con, column_names, table, query_values):
        '''
        Builds pandas dataframe from SQL query
        :param con: database connection
        :param column_names: database table columns to be included in dataframe
        :param table: database table name
        :param query_values: SQL arguments dictionary
        :return: Pandas dataframe
        '''
        concatenate_columns = ', '.join(column_names)
        df = pd.read_sql_query("SELECT {} FROM (SELECT * FROM {} ORDER BY {} {})"
                               " WHERE (title LIKE '%{}%' OR publisher LIKE '%{}%' OR country LIKE '%{}%') LIMIT {},{};"
                               "".format(concatenate_columns,
                                         table,
                                         query_values['sort_column'],
                                         query_values['sort_dir'],
                                         query_values['search_term'],
                                         query_values['search_term'],
                                         query_values['search_term'],
                                         query_values['start_index'],
                                         query_values['length']),
                               con)
        return df

    def convert_to_href(column_name, df, prefix=''):
        '''
        Converts a dataframe column to a hypertext link with optional prefix
        :return: Pandas dataframe
        '''
        df[column_name] = '<a href="{}/'.format(prefix) + \
                          df[column_name].str.replace(' ', '_') + '">' + \
                          df[column_name] + '</a>'
        return df

    def build_json_response(df, query_string, table_length):
        '''
        Builds the JSON response based on the structure of a pandas dataframe
        :return: JSON data structure
        '''
        df_list = df.values.tolist()
        results = {}
        results['draw'] = query_string['draw']
        results['recordsTotal'] = table_length
        results['recordsFiltered'] = table_length
        results['data'] = df_list
        return jsonify(results)


    con = sqlite3.connect('database.sqlite3')
    table_length = get_table_length(con, table='journals')
    query_string = json.loads(request.values.get("args"))
    column_names = ['title', 'country', 'publisher', 'rating']
    table = 'journals'
    query_values = parse_query_string(query_string, column_names)
    df = build_table(con, column_names, table, query_values)
    df_with_href = convert_to_href('title', df, 'journal_info')
    json_response = build_json_response(df_with_href, query_string, table_length)
    con.close()

    return json_response

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if User.query.filter_by(username=username).first() != None:
            if check_password_hash(user.password, password):
                login_user(user)
                flash('Successfully logged in!')
                return redirect(url_for('index'))
        else:
            error = 'username or password is incorrect or does not exist'

    return render_template('login.html', form=form, error=error, logged_in=current_user.is_authenticated)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    #ToDo may need underscore in render field
    form = RegisterForm()
    error = None
    if form.validate_on_submit():
        print("validate")
        username = form.username.data
        password = generate_password_hash(form.password.data)
        if User.query.filter_by(username=username).first() != None:
            error = 'user already exits'
        else:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash('Successfully registered and logged in!')
            return redirect(url_for('index'))
    return render_template('register.html', form=form, error=error, logged_in=current_user.is_authenticated)

@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html', logged_in=current_user.is_authenticated)
