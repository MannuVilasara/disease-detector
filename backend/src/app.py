from flask import Flask, request, jsonify
from flask_cors import CORS
from src.utils.utils import encode_symptoms, get_symptoms, inverse_encode_symptoms, get_disease_description
from joblib import load
import os
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configure CORS
CORS(app, origins=['*'])  # Configure this properly for production

# Load model with error handling
try:
    model = load('src/model/model.joblib')
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    model = None



@app.route('/')
def index():
    return jsonify(message='Welcome to the Flask API!')

@app.route('/predict', methods=['POST'])
def encode_symptoms_route():
    if model is None:
        return jsonify(error='Model not available'), 503
    
    data = request.get_json()
    if not data:
        return jsonify(error='No data provided'), 400
    
    try:
        encoded_symptoms = encode_symptoms(get_symptoms(data))
        prediction = model.predict([encoded_symptoms])
        return jsonify(disease=str(inverse_encode_symptoms(prediction)[0]))
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return jsonify(error='Prediction failed'), 500

@app.route('/disease_description', methods=['POST'])
def disease_description_route():
    data = request.get_json()
    if not data or 'disease_name' not in data:
        return jsonify(error='No disease name provided'), 400
    
    try:
        disease_name = data['disease_name']
        description = get_disease_description(disease_name)
        if description:
            return jsonify(description=str(description))
        else:
            return jsonify(error='Description not found for the given disease'), 404
    except Exception as e:
        logger.error(f"Description lookup error: {e}")
        return jsonify(error='Description lookup failed'), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'timestamp': str(int(time.time()))
    })

if __name__ == '__main__':
    app.run(debug=True)