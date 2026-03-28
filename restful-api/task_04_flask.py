from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory dictionary to store users
users = {}

@app.route('/')
def home():
    """Returns a welcome message."""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Returns a list of all usernames."""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Returns the API status."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Returns the full object for a specific user."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the dictionary."""
    parsed_data = request.get_json(silent=True)
    
    # Check if JSON is valid
    if parsed_data is None:
        return jsonify({"error": "Invalid JSON"}), 400
        
    username = parsed_data.get("username")
    
    # Check if username is missing
    if not username:
        return jsonify({"error": "Username is required"}), 400
        
    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
        
    # Add the user to the dictionary
    users[username] = parsed_data
    
    # Return success response
    return jsonify({
        "message": "User added",
        "user": parsed_data
    }), 201

if __name__ == "__main__":
    app.run()
