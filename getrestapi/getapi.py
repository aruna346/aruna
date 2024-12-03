from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for demonstration
data = [
{"id": 1, "name": "Rama"},
{"id": 2, "name": "prasanna"},
{"id": 3, "name": "prathibha"},
{"id": 4, "name": "mounika"}
]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
