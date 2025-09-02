from flask import Blueprint, request, jsonify

from backend.models import db, Feedback
from datetime import datetime

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    comment = data.get('comment')
    if not name or not email or not comment:
        return jsonify({'error': 'All fields are required.'}), 400
    fb = Feedback(name=name, email=email, comment=comment)
    db.session.add(fb)
    db.session.commit()
    return jsonify({'message': 'Thank you for your feedback!'})
