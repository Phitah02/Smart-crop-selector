from flask import Blueprint, request, jsonify
from backend.utils.ai import get_crop_recommendations

recommend_bp = Blueprint('recommend', __name__)

@recommend_bp.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    soil = data.get('soil_type')
    rainfall = data.get('rainfall_level')
    region = data.get('region')
    # Call AI logic
    crops, error = get_crop_recommendations(soil, rainfall, region)
    if error:
        return jsonify({'error': error}), 500
    return jsonify({'crops': crops})
