from app import app, db
from flask import render_template, redirect, url_for, flash, session
from forms import LoginForm, RegisterForm, AddRecordForm, SearchBySSN, SearchByTimeFrame, SearchByProvider
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

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

    #Need to fix below so checks each form correctly
    if form1.is_submitted():
        if form1.validate():
            return 'Records with specified ssn'
        else:
            return 'Sorry cannot validate'
    if form2.is_submitted():
        if form2.validate():
            return 'Records with time frame'
        else:
            return 'Error'
    if form3.is_submitted():
        if form3.validate_on_submit():
            return 'Records with specified provider'
        else:
            return 'Error'

    return render_template('search.html', form1=form1, form2=form2, form3=form3)

@app.route('/search/ssn', methods=['GET', 'POST'])
@login_required
def searchBySSN():
    return 'Records with specified ssn'


@app.route('/search/time', methods=['GET'])
@login_required
def searchByTime():
    return 'Records with specified time frame'

@app.route('/search/provider', methods=['GET'])
@login_required
def searchByProvider():
    return 'Records with specified health care provider'

@app.route('/addRecord', methods=['GET','POST'])
@login_required
def addRecord():
    form = AddRecordForm()

    # Check if the form is submited
    if form.validate_on_submit():
        return 'Record Added'

    return render_template('addRecord.html', name=current_user.username, form=form)

@app.route('/viewRecords')
@login_required
def viewRecords():
    viewType = None
    return render_template('viewRecords.html', viewType=viewType)