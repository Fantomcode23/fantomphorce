from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from database import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    emissions = db.relationship('Emission', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Emission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    car_emissions = db.Column(db.Float)
    two_wheeler_emissions = db.Column(db.Float)
    air_travel_emissions = db.Column(db.Float)
    electricity_emissions = db.Column(db.Float)
    diet_emissions = db.Column(db.Float)
    waste_emissions = db.Column(db.Float)
    total_emissions = db.Column(db.Float)