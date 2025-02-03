# app.py
import os
import flask
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math
from utils.number_utils import (
    is_armstrong_number, 
    is_prime, 
    is_perfect_number, 
    digit_sum
)

app = Flask(__name__)
CORS(app)

def get_number_fact(number):
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math")
        return response.text if response.status_code == 200 else None
    except:
        return None

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        number = request.args.get('number', type=int)
        
        if number is None:
            return jsonify({
                "number": "invalid",
                "error": True,
                "message": "Invalid number input"
            }), 400

        properties = []
        if is_armstrong_number(number):
            properties.append("armstrong")
        
        properties.append("odd" if number % 2 != 0 else "even")

        fun_fact = get_number_fact(number) or f"No interesting fact found for {number}"

        return jsonify({
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect_number(number),
            "properties": properties,
            "digit_sum": digit_sum(number),
            "fun_fact": fun_fact
        }), 200

    except ValueError:
        return jsonify({
            "number": request.args.get('number'),
            "error": True,
            "message": "Input must be a valid integer"
        }), 400

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "error": True,
        "message": "Bad request"
    }), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)