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
        number = request.args.get('number', type=float)
        
        if number is None:
            return jsonify({
                "number": "invalid",
                "error": True,
                "message": "Invalid number input"
            }), 400

        # Convert to positive integer for mathematical properties
        number_int = abs(int(number))

        properties = []
        if is_armstrong_number(number_int):
            properties.append("armstrong")
        
        properties.append("odd" if number_int % 2 != 0 else "even")

        fun_fact = get_number_fact(number_int) or f"No interesting fact found for {number_int}"

        return jsonify({
            "number": number_int,
            "is_prime": is_prime(number_int),
            "is_perfect": is_perfect_number(number_int) if number_int != 0 else False,
            "properties": properties,
            "digit_sum": digit_sum(number_int),
            "fun_fact": fun_fact
        }), 200

    except ValueError:
        return jsonify({
            "number": request.args.get('number'),
            "error": True,
            "message": "Input must be a valid number"
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
