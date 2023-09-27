from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load data from config_users.json
# Open and read the JSON file containing user data
with open('config_users.json', 'r') as json_file:
    data = json.load(json_file)

# Define a route for the "/api/users" endpoint
@app.route('/api/users', methods=['GET'])
def get_users():
    # Return the user data as JSON when the endpoint is accessed
    return jsonify(data)

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
