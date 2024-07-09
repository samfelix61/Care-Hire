from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from datetime import datetime

db = SQLAlchemy()

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    profile_image = db.Column(db.String(200), nullable=True)
    phone_number = db.Column(db.String(20), nullable=False)

    reviews = db.relationship('Review', backref='user', lazy=True)
    bookings = db.relationship('Booking', backref='user', lazy=True)


class CarOwner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    profile_image = db.Column(db.String(200), nullable=True)

    cars = db.relationship('Car', backref='owner', lazy=True)
    bookings = db.relationship('Booking', backref='car_owner', lazy=True)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price_per_day = db.Column(db.Float, nullable=False)
    availability_status = db.Column(db.Boolean, default=True)
    car_image_url = db.Column(db.String(200), nullable=True)
    
    owner_id = db.Column(db.Integer, db.ForeignKey('car_owner.id'), nullable=False)
    reviews = db.relationship('Review', backref='car', lazy=True)
    bookings = db.relationship('Booking', backref='car', lazy=True)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    car_owner_id = db.Column(db.Integer, db.ForeignKey('car_owner.id'), nullable=False)
