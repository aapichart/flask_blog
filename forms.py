from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=8) ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=8) ])
    confirm_password = PasswordField('Confirm_Password', validators=[DataRequired(), Length(min=2, max=8), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=8) ])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=8) ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('LogIn')


    
