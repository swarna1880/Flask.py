from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user data store
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid data"}), 400

    new_id = max(users.keys(), default=0) + 1
    users[new_id] = {"name": data["name"], "email": data["email"]}
    return jsonify({"id": new_id, "user": users[new_id]}), 201

# PUT to update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    users[user_id].update(data)
    return jsonify({"message": "User updated", "user": users[user_id]})

# DELETE a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        deleted = users.pop(user_id)
        return jsonify({"message": "User deleted", "user": deleted})
    return jsonify({"error": "User not found"}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
