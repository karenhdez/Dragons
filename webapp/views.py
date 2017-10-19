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

@app.route('/search')
@login_required
def search():
    return render_template('search.html', name=current_user.username)

@app.route('/search2/<selected>')
def search2(selected=None):
    if selected == "ssn":
        type = 'ssn'
        form = SearchBySSN()
        return render_template('search.html', form=form, type=type)
    return render_template('search.html')

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
    return render_template('viewRecords.html')