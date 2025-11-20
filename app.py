from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}

# GET - fetch all users
@app.get("/users")
def get_users():
    return jsonify(users)

# POST - add new user
@app.post("/users")
def add_user():
    data = request.json
    user_id = str(len(users) + 1)
    users[user_id] = data
    return {"message": "User added", "id": user_id}

# PUT - update existing user
@app.put("/users/<user_id>")
def update_user(user_id):
    if user_id not in users:
        return {"error": "User not found"}, 404
    users[user_id].update(request.json)
    return {"message": "User updated"}

# DELETE - remove user
@app.delete("/users/<user_id>")
def delete_user(user_id):
    if user_id not in users:
        return {"error": "User not found"}, 404
    del users[user_id]
    return {"message": "User deleted"}


if __name__ == "__main__":
    app.run(debug=True)
