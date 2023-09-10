# Import necessary modules from Flask
from flask import Flask, jsonify

# Create a Flask web application
app = Flask(__name__)

# Sample data for demonstration
data = [
    {"id": 1, "name": "Rama"},
    {"id": 2, "name": "prasanna"},
    {"id": 3, "name": "prathibha"},
    {"id": 4, "name": "mounika"}
]

# Define a route for the '/api/users' endpoint that responds to HTTP GET requests
@app.route('/api/users', methods=['GET'])
def get_users():
    # Return the data as JSON response
    return jsonify(data)

# Entry point of the application when executed as the main program
if __name__ == '__main__':
    # Run the Flask app in debug mode (auto-reloading on code changes)
    app.run(debug=True)
