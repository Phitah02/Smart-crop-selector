from flask import Blueprint, request, jsonify
from backend.utils.db import save_user_input

submit_bp = Blueprint('submit', __name__)

@submit_bp.route('/submit', methods=['POST'])
def submit():
    data = request.json
    result = save_user_input(data)
    if result:
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'}), 500
