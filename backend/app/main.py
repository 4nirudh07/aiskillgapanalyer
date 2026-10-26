from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from typing import List, Optional
from datetime import timedelta
from bson import ObjectId

from .database import get_db
from .auth import get_password_hash, verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from .models import UserCreate, UserLogin, UserProfile, SkillItem, AnalyzeRequest, RecommendRequest, Token
from .dependencies import get_current_user
from .seed import seed_database
from .ml.skill_extractor import extract_skills
from .ml.skill_gap import skill_gap
from .ml.job_recommender import recommend_jobs

app = FastAPI(title="AI SkillGap & Job Recommendation API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.on_event("startup")
def startup():
    seed_database()

# --- Auth Routes ---
@app.post("/api/auth/register")
def register(user: UserCreate):
    db = get_db()
    if db.users.find_one({"email": user.email}):
        raise HTTPException(400, "Email already registered")
    
    new_user = {
        "name": user.name,
        "email": user.email,
        "password": get_password_hash(user.password),
        "profile": {},
        "skills": []
    }
    db.users.insert_one(new_user)
    return {"message": "User registered successfully"}

@app.post("/api/auth/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = get_db()
    user = db.users.find_one({"email": form_data.username})
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(401, "Incorrect email or password")
    
    access_token = create_access_token(
        data={"sub": str(user["_id"])}, 
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/api/auth/me")
def me(current_user: dict = Depends(get_current_user)):
    return {
        "id": current_user["_id"],
        "name": current_user["name"],
        "email": current_user["email"]
    }

# --- Profile & Skills Routes ---
@app.get("/api/profile")
def get_profile(current_user: dict = Depends(get_current_user)):
    return current_user.get("profile", {})

@app.put("/api/profile")
def update_profile(profile: UserProfile, current_user: dict = Depends(get_current_user)):
    db = get_db()
    db.users.update_one({"_id": ObjectId(current_user["_id"])}, {"$set": {"profile": profile.dict()}})
    return {"message": "Profile updated"}

@app.get("/api/skills")
def get_user_skills(current_user: dict = Depends(get_current_user)):
    return current_user.get("skills", [])

@app.post("/api/skills")
def add_skill(skill: SkillItem, current_user: dict = Depends(get_current_user)):
    db = get_db()
    # Check if skill exists
    skills = current_user.get("skills", [])
    if any(s.get("name").lower() == skill.name.lower() for s in skills):
        raise HTTPException(400, "Skill already exists")
    db.users.update_one({"_id": ObjectId(current_user["_id"])}, {"$push": {"skills": skill.dict()}})
    return {"message": "Skill added"}

@app.delete("/api/skills/{skill_name}")
def delete_skill(skill_name: str, current_user: dict = Depends(get_current_user)):
    db = get_db()
    db.users.update_one({"_id": ObjectId(current_user["_id"])}, {"$pull": {"skills": {"name": skill_name}}})
    return {"message": "Skill removed"}

# --- Roles & ML Routes ---
@app.get("/api/roles")
def get_roles():
    db = get_db()
    roles = list(db.roles.find({}, {"_id": 0}))
    if not roles:
        roles = seed_database(return_roles=True)
    return {"roles": roles}

@app.post("/api/skill-gap/analyze")
def analyze(req: AnalyzeRequest, current_user: dict = Depends(get_current_user)):
    db = get_db()
    roles = list(db.roles.find({}, {"_id": 0}))
    role = next((r for r in roles if r["role_id"] == req.target_role), None)
    if not role:
        raise HTTPException(404, "Role not found")
        
    user_skills = current_user.get("skills", [])
    result = skill_gap(user_skills, role["skills"], target_role_title=role["title"])
    
    # Save the latest analysis for dashboard
    db.users.update_one(
        {"_id": ObjectId(current_user["_id"])}, 
        {"$set": {"latest_analysis": {"target_role": role["title"], "result": result}}}
    )
    return result

@app.get("/api/skill-gap/latest")
def get_latest_analysis(current_user: dict = Depends(get_current_user)):
    return current_user.get("latest_analysis", None)

@app.get("/api/jobs")
def get_all_jobs():
    db = get_db()
    jobs = list(db.jobs.find({}, {"_id": 0}))
    if not jobs:
        jobs = seed_database(return_jobs=True)
    return {"jobs": jobs}

@app.post("/api/jobs/recommended")
def get_recommended_jobs(current_user: dict = Depends(get_current_user)):
    db = get_db()
    jobs = list(db.jobs.find({}, {"_id": 0}))
    user_skills = [s["name"] for s in current_user.get("skills", [])]
    recommendations = recommend_jobs(user_skills, jobs)
    return {"recommendations": recommendations}

@app.post("/api/resume/skills")
async def resume_skills(file: UploadFile = File(...)):
    data = await file.read()
    skills = extract_skills(data, file.filename or "")
    return {"filename": file.filename, "extracted_skills": skills}
