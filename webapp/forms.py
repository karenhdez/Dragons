from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, IntegerField, DateField
from wtforms.validators import InputRequired, Email, Length, Optional

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')
    
class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(min=4, max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class AddRecordForm(FlaskForm):
    first_name = StringField('Patient First Name', validators=[InputRequired(), Length(max=50)])
    last_name = StringField('Patient Last Name', validators=[InputRequired(), Length(max=50)])
    ssn = IntegerField('Patient SSN', validators=[InputRequired(), Length(min=9, max=9)])
    provider = StringField('Healthcare Provider', validators=[InputRequired(), Length(max=50)])
    reason = TextAreaField('Reason for visit', validators=[Optional(), Length(max=200)])

class SearchBySSN(FlaskForm):
    ssn = IntegerField('SSN', validators=[InputRequired(), Length(min=9, max=9)])

class SearchByTimeFrame(FlaskForm):
    start_date = DateField('Start Date', validators=[InputRequired()])
    end_date = DateField('End Date', validators=[InputRequired()])

class SearchByProvider(FlaskForm):
    provider = StringField('Healthcare Provider', validators=[InputRequired(), Length(max=50)])