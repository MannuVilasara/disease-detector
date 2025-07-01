from flask import Flask, request, jsonify
from src.utils.utils import encode_symptoms, get_symptoms, inverse_encode_symptoms
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