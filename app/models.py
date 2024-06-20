from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), index=True, unique=True, nullable=False)
    email = db.Column(db.String(25), index=True, unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
  
    def __repr__(self):
        return f'<User {self.username}>'
