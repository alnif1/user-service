from fastapi import FastAPI, HTTPException
from app.database import users

app = FastAPI()

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for u in users:
        if u["id"] == user_id:
            return u
    raise HTTPException(status_code=404, detail="User not found")
