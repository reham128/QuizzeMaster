from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '70678d4c4f51674c3974bfccdff5b7b2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./app_data.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test_data.db'
db= SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
