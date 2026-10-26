from pydantic import BaseModel, Field
from typing import List, Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserProfile(BaseModel):
    name: str
    email: str
    phone: Optional[str] = ""
    location: Optional[str] = ""
    education: Optional[str] = ""
    degree: Optional[str] = ""
    college: Optional[str] = ""
    grad_year: Optional[str] = ""
    experience_level: Optional[str] = ""
    current_role: Optional[str] = ""
    target_role: Optional[str] = ""
    github: Optional[str] = ""
    linkedin: Optional[str] = ""
    portfolio: Optional[str] = ""

class SkillItem(BaseModel):
    name: str
    category: str
    proficiency: str
    years: float

class AnalyzeRequest(BaseModel):
    job_id: Optional[str] = None
    target_role: Optional[str] = None

class RecommendRequest(BaseModel):
    limit: int = 10
