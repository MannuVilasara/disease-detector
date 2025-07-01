from flask import Flask, request, jsonify
from src.utils.utils import encode_symptoms, get_symptoms, inverse_encode_symptoms, get_disease_description
from joblib import load

app = Flask(__name__)


model = load('src/model/model.joblib')



@app.route('/')
def index():
    return jsonify(message='Welcome to the Flask API!')

@app.route('/predict', methods=['POST'])
def encode_symptoms_route():
    data = request.get_json()
    if not data:
        return jsonify(error='No data provided'), 400
    encoded_symptoms = encode_symptoms(get_symptoms(data))
    prediction = model.predict([encoded_symptoms])
    return jsonify(disease=str(inverse_encode_symptoms(prediction)[0]))

@app.route('/disease_description', methods=['POST'])
def disease_description_route():
    data = request.get_json()
    if not data or 'disease_name' not in data:
        return jsonify(error='No disease name provided'), 400
    disease_name = data['disease_name']
    description = get_disease_description(disease_name)
    if description:
        return jsonify(description=str(description))
    else:
        return jsonify(error='Description not found for the given disease'), 404