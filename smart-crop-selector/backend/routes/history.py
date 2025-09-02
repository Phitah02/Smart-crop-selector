from flask import Blueprint, jsonify
from backend.utils.db import get_user_history

history_bp = Blueprint('history', __name__)

@history_bp.route('/history', methods=['GET'])
def history():
    history = get_user_history()
    return jsonify({'history': history})
