from fastapi import FastAPI

app = FastAPI()

users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    return user or {"message": "User not found"}

@app.post("/users")
def create_user(user: dict):
    user["id"] = len(users) + 1
    users.append(user)
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, user_update: dict):
    for user in users:
        if user["id"] == user_id:
            user.update(user_update)
            return user
    return {"message": "User not found"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    users = [u for u in users if u["id"] != user_id]
    return {"message": "User deleted"}
