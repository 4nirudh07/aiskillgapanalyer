from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .auth import decode_access_token
from .database import get_db
from bson import ObjectId

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

def get_current_user():
    db = get_db()
    # Find or create a guest user
    user = db.users.find_one({"email": "guest@example.com"})
    if not user:
        new_user = {
            "name": "Guest User",
            "email": "guest@example.com",
            "profile": {"target_role": "Data Scientist"},
            "skills": [],
            "latest_analysis": None
        }
        db.users.insert_one(new_user)
        user = db.users.find_one({"email": "guest@example.com"})
        
    user["_id"] = str(user["_id"])
    return user
