from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=12)])
    email = StringField('Email address',
                        validators=[DataRequired(), Email(), Length(min=14, max=25)])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=4, max=16)])
    password_confirm = PasswordField('Confirm Password', 
                                     validators=[DataRequired(), EqualTo('password')])
    submit_btn = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is alredy exist!.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is alredy exist!.')


class LoginForm(FlaskForm):
    email = StringField('Email address', 
                        validators=[DataRequired(), Email(), Length(min=14, max=25)])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=4, max=16)])
    remember = BooleanField('Remember Me')
    submit_btn = SubmitField('Login')


class UpdateForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=12)])
    email = StringField('Email address',
                        validators=[DataRequired(), Email(), Length(min=14, max=25)])
    profile_pic = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit_btn = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is alredy exist!. Try Again.')
        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email is alredy exist!.')
