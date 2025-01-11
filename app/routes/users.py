from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Mock database for user profiles
user_profiles = {}

class User(BaseModel):
    name: str
    email: str

@router.post("/register")
def register_user(user: User):
    user_profiles[user.email] = {"name": user.name, "level": "unknown", "progress": {}}
    return {"message": f"User {user.name} registered successfully!"}
