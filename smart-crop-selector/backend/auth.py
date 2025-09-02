from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from backend.models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username or not email or not password:
        return jsonify({'error': 'Missing fields'}), 400
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'error': 'User already exists'}), 409
    user = User(
        username=username,
        email=email,
        password_hash=generate_password_hash(password)
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username_or_email = data.get('username')
    password = data.get('password')
    user = User.query.filter((User.username == username_or_email) | (User.email == username_or_email)).first()
    if user and check_password_hash(user.password_hash, password):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful'})
    return jsonify({'error': 'Invalid credentials'}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out'})