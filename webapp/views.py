from app import app, db
from flask import render_template, redirect, url_for, flash, jsonify, session
from forms import LoginForm, RegisterForm, AddRecordForm, SearchBySSN, SearchByTimeFrame, SearchByProvider, AddPatientForm
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from blockchain.blockchain import Blockchain
from uuid import uuid4
import time
import json

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# This will create a random name for the node
node_identifier = str(uuid4()).replace('-', '')
dragoncoin = Blockchain()

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

@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form1 = SearchBySSN()
    form2 = SearchByTimeFrame()
    form3 = SearchByProvider()

    #Fix below, only first form works
    if form1.is_submitted():
        if form1.validate():
            return searchBySSN(form1.ssn.data)
        else:
            return str(form1.errors)
    elif form2.is_submitted():
        if form2.validate():
            return searchByTime(form2.start_date.data, form2.end_date.data)
        else:
            return str(form2.errors)
    elif form3.is_submitted():
        if form3.validate_on_submit():
            return searchByProvider(form3.provider.data)
        else:
            return str(form3.errors)
    else:
        return render_template('search.html', form1=form1, form2=form2, form3=form3)

    #return render_template('search.html', form1=form1, form2=form2, form3=form3)

def searchBySSN(ssn):
    result = []
    patient_events = getPatientEvents()
    for event in patient_events:
        if event['ssn'] == ssn:
            result.append(event)
    jsonify(result)
    return render_template('/searchResult.html', records=result)


def searchByTime(start_date, end_date):
    return 'Records with specified time frame'


def searchByProvider(provider):
    result = []
    patient_events = getPatientEvents()
    for event in patient_events:
        if event['provider'] == provider:
            result.append(event)
    jsonify(result)
    return render_template('/searchResult.html', records=result)


@app.route('/addRecord', methods=['GET','POST'])
@login_required
def addRecord():
    form = AddRecordForm()

    if form.validate_on_submit():
        return 'Record Added'

    return render_template('addRecord.html', name=current_user.username, form=form)


@app.route('/records/all', methods=['GET'])
@login_required
def viewRecords():
    viewType = None
    records = dragoncoin.blockchain
    jsonify(records)
    return render_template('viewRecords.html', records=records, viewType=viewType)


@app.route('/patient/new', methods=['GET', 'POST'])
@login_required
def addPatient():
    form = AddPatientForm()

    if form.is_submitted():
        if form.validate():
            dragoncoin.add_patient_event(form.patient_id.data,
                                                str(time.time()),
                                                form.ssn.data,
                                                form.name.data,
                                                form.provider.data)
            return add_block()
        else:
            return str(form.errors)

    return render_template('newPatient.html', form=form)


#Mine and add block
@app.route('/block/new', methods=['GET'])
def add_block():
    proof, hashed_block  = dragoncoin.proof_of_work(dragoncoin.last_block)
    if(proof != 0):
        response = dragoncoin.add_block(proof)
        jsonify(response)
    else:
        response = 'Sorry, the record could not be added.'
    return render_template('block.html', block=response)


#Get current blockchain
@app.route('/blockchain', methods=['GET'])
def full_blockchain():
    response = {
        'chain': dragoncoin.blockchain,
        'length': len(dragoncoin.blockchain)
    }
    jsonify(response)
    return render_template('blockchain.html', blockchain=response)


def getPatientEvents():
    result = []
    chain = dragoncoin.blockchain
    jsonify(chain)
    for record in chain:
        for event in record['patient_events']:
            result.append(event)
    return result
