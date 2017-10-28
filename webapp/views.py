from app import app, db
from flask import render_template, redirect, url_for, flash, jsonify, session
from forms import LoginForm, RegisterForm, AddRecordForm, SearchBySSN, SearchByTimeFrame, SearchByProvider, AddPatientForm, SearchByName
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
import json
import requests

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
network_url = 'http://127.0.0.1:5000/'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    #Check if the form is submitted, 
    if form.validate_on_submit():
        #usernames are unique so it's okay to return the first query we find
        user = User.query.filter_by(username=form.username.data).first()

        # if user exists
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))
            else:
                flash('Incorrect Login Credentials')
                #return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = RegisterForm()

    #Check if the form is submited
    if form.validate_on_submit():

        #shaw256 generates a password that's 80 characters long, models should reflect that
        hashed_password = generate_password_hash(form.password.data, method='sha256')

        #we're passing the data without hashing for testing purposes
        new_user = User(email=form.email.data,
                        username=form.username.data,
                        password=hashed_password)
                        
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h>'
        #return '<p>{}</p><p>{}</p><p>{}</p><h1>'.format(form.email.data, form.username.data, form.password.data)

    return render_template('signup.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)


#Displays input forms for search records
@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form1 = SearchBySSN()
    form2 = SearchByName()
    #form2 = SearchByTimeFrame()
    form3 = SearchByProvider()

    return render_template('search.html', form1=form1, form2=form2, form3=form3)


#Get records with specified ssn
@app.route('/search/ssn', methods=['GET', 'POST'])
@login_required
def searchBySSN():
    form = SearchBySSN()
    result = []

    if form.validate_on_submit():
        patient_events = get_records()
        for event in patient_events:
            if event['ssn'] == str(form.ssn.data):
                result.append(event)
        jsonify(result)

    return render_template('/searchResult.html', records=result)


#Get records with specified first name
@app.route('/search/name', methods=['GET', 'POST'])
@login_required
def searchByName():
    form = SearchByName()
    result = []

    if form.validate_on_submit():
        patient_events = get_records()
        form_name = (form.first_name.data).lower()
        for event in patient_events:
            event_name = event['name'].lower()
            if event_name == form_name:
                result.append(event)
        jsonify(result)

    return render_template('/searchResult.html', records=result)


#Below is not fully implemented yet
@app.route('/search/time_window', methods=['GET', 'POST'])
def searchByTime():
    form = SearchByTimeFrame()
    result = []

    if form.validate_on_submit():
        start_date = form.start_date.data #find better way to allow user to input date (formatted)
        end_date = form.end_date.data
        patient_events = get_records()
        for event in patient_events:
            time = datetime.fromtimestamp(int(event['timestamp'])).strftime('%Y-%m-%d')
            if time == start_date: #find proper way to compare
                result.append(event)
        jsonify(result)

    return render_template('/searchResult.html', records=result)


#Get records with specified provider
@app.route('/search/provider', methods=['GET', 'POST'])
def searchByProvider():
    form = SearchByProvider()
    result = []

    if form.validate_on_submit():
        patient_events = get_records()
        form_provider = (form.provider.data).lower()
        for event in patient_events:
            event_provider = event['provider'].lower()
            if event_provider == form_provider:
                result.append(event)
        jsonify(result)

    return render_template('/searchResult.html', records=result)


#Get all records in blockchain
@app.route('/records/all', methods=['GET'])
@login_required
def view_records():
    viewType = None
    response = requests.get('http://127.0.0.1:5000/blockchain')
    if response.status_code == 200:
        json_response = response.content
        blockchain = json.loads(json_response)
        records = []
        for block in blockchain['chain']:
            for event in block['patient_events']:
                records.append(event)
    else:
        records = 'Sorry, cannot view records at this moment.'
    return render_template('viewRecords.html', records=records, viewType=viewType)


#Add patient event, mine it, and add to blockchain
@app.route('/patient/new', methods=['GET', 'POST'])
@login_required
def add_record():
    form = AddPatientForm()

    if form.validate_on_submit():
        request_body = {
            'name' : form.name.data,
            'patient_id' : str(form.patient_id.data),
            'ssn' : str(form.ssn.data),
            'provider' : str(form.provider.data)
        }
        response = requests.post('http://127.0.0.1:5000/patient_event/new', json=request_body)
        if response.status_code == 201:
            mine_response = requests.get('http://127.0.0.1:5000/mine')
            if mine_response.status_code == 201:
                block = json.loads(mine_response.text)
                return render_template('block.html', block=block)
            else:
                return mine_response.status_code
        else:
            return response.status_code
    else:
        flash(form.errors)

    return render_template('newPatient.html', form=form)


#Get current blockchain
@app.route('/blockchain', methods=['GET'])
def view_blockchain():
    response = requests.get('http://127.0.0.1:5000/blockchain')
    if response.status_code == 200:
        json_response = response.content
        python_obj = json.loads(json_response)
        response = python_obj
    else:
        response = 'Sorry, the record could not be added to block chain'
    return render_template('blockchain.html', blockchain=response)


#Returns records added to blockchain as array
def get_records():
    response = requests.get('http://127.0.0.1:5000/blockchain')
    if response.status_code == 200:
        json_response = response.content
        blockchain = json.loads(json_response)
        records = []
        for block in blockchain['chain']:
            for event in block['patient_events']:
                records.append(event)
        return records