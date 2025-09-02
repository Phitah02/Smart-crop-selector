from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    recommendations = db.relationship('Recommendation', backref='user', lazy=True)

class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    soil_type = db.Column(db.String(50))
    rainfall_level = db.Column(db.String(50))
    region = db.Column(db.String(80))

class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    crop_id = db.Column(db.Integer, db.ForeignKey('crop.id'))
    input_soil_type = db.Column(db.String(50))
    input_rainfall_level = db.Column(db.String(50))
    input_region = db.Column(db.String(80))
    recommended_crop = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Feedback model for feedback/comments
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)