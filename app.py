from flask import Flask, render_template, url_for, redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '70678d4c4f51674c3974bfccdff5b7b2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_data.db'
db= SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), index=True, unique=True, nullable=False)
    email = db.Column(db.String(25), index=True, unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
  
    def __repr__(self):
        return f'<User {self.username}>'

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


with app.app_context():
    db.create_all()


if __name__ == "__main__":
  app.run(debug=True)
