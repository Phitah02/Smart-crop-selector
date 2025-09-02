from flask import Blueprint, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

pay_bp = Blueprint('pay', __name__)

INTASEND_SECRET_KEY = os.getenv('INTASEND_SECRET_KEY')
INTASEND_PUBLISHABLE_KEY = os.getenv('INTASEND_PUBLISHABLE_KEY')
INTASEND_BASE_URL = 'https://api.intasend.com/api/v1/payment/'

@pay_bp.route('/pay', methods=['POST'])
def pay():
    data = request.json
    email = data.get('email')
    amount = data.get('amount', 5)  # Default premium price
    if not email:
        return jsonify({'error': 'Email required'}), 400
    headers = {
        'Authorization': f'Bearer {INTASEND_SECRET_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        'public_key': INTASEND_PUBLISHABLE_KEY,
        'currency': 'KES',
        'amount': amount,
        'email': email,
        'redirect_url': data.get('redirect_url', 'https://your-frontend-url.com/premium-success')
    }
    try:
        print('IntaSend payload:', payload)
        resp = requests.post(INTASEND_BASE_URL + 'checkout/', json=payload, headers=headers)
        print('IntaSend response status:', resp.status_code)
        print('IntaSend response body:', resp.text)
        resp.raise_for_status()
        return jsonify(resp.json())
    except Exception as e:
        print('IntaSend error:', str(e))
        return jsonify({'error': str(e)}), 500
