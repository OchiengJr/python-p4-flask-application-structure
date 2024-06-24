#!/usr/bin/env python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# Configuration
app.config['DEBUG'] = True  # Enable debugging mode
app.config['SECRET_KEY'] = 'supersecretkey'  # Set a secret key for sessions

# Route Example
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# Add more routes as needed
@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    return jsonify(message=f"Hello, {name}!")

# Error Handling
@app.errorhandler(404)
def not_found_error(error):
    return jsonify(error="Resource not found"), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify(error="Internal server error"), 500

# Running the app
if __name__ == '__main__':
    app.run()
