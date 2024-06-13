from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=12)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=14, max=25)])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=4, max=16)])
    password_confirm = PasswordField('Confirm Password', 
                                     validators=[DataRequired(), EqualTo('password')])
    submit_btn = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email(), Length(min=14, max=25)])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=4, max=16)])
    remember = BooleanField('Remember Me')
    submit_btn = SubmitField('Login')
