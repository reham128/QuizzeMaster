from flask import render_template, url_for, redirect, flash, request
from app import app, db
from app.forms import RegistrationForm, LoginForm
from app.models import User

@app.route('/')
@app.route('/home')
def home():
  return render_template('index.html')


@app.route('/about')
def about():
  return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'r_nour30@yahoo.com' and form.password.data == 'password':
      flash('Login Successfully. Welcome.', 'success')
      return redirect(url_for('home'))
    else:
      flash('Login Failed. Please check username and password', 'danger')
  return render_template('login.html', title='Login', form=form, submitted=request.method == 'POST')

@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'{form.username.data} Account Created Successfully. Wellcom.', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form, submitted=request.method == 'POST')
