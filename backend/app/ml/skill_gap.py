import joblib
import pandas as pd
import os
import numpy as np

# Load models safely
MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")

model_match = None
model_readiness = None
clf_strongest = None
clf_missing = None
le_strongest = None
le_missing = None

def load_models():
    global model_match, model_readiness, clf_strongest, clf_missing, le_strongest, le_missing
    if not os.path.exists(os.path.join(MODEL_DIR, "model_match.pkl")):
        return False
        
    try:
        model_match = joblib.load(os.path.join(MODEL_DIR, "model_match.pkl"))
        model_readiness = joblib.load(os.path.join(MODEL_DIR, "model_readiness.pkl"))
        clf_strongest = joblib.load(os.path.join(MODEL_DIR, "model_strongest.pkl"))
        clf_missing = joblib.load(os.path.join(MODEL_DIR, "model_missing.pkl"))
        le_strongest = joblib.load(os.path.join(MODEL_DIR, "le_strongest.pkl"))
        le_missing = joblib.load(os.path.join(MODEL_DIR, "le_missing.pkl"))
        return True
    except Exception as e:
        print(f"Error loading models: {e}")
        return False

# Initialize
models_loaded = load_models()

def norm(s):
    return s.strip().lower()

def determine_readiness_level(percentage):
    if percentage < 40: return "Beginner"
    if percentage < 60: return "Developing"
    if percentage < 75: return "Intermediate"
    if percentage < 90: return "Job Ready"
    return "Highly Job Ready"

def skill_gap(user_skills, required_skills_with_weights, target_role_title="Target Role"):
    """
    user_skills: list of dicts {"name": str, "proficiency": str}
    required_skills_with_weights: list of dicts {"name": str, "importance": int, "category": str}
    """
    if not models_loaded:
        load_models()
        
    # We map user skills to categories to calculate the 7 features
    # 'technical_skills', 'programming_skills', 'problem_solving', 
    # 'projects', 'communication', 'education', 'experience'
    
    # We will simulate the scores out of 100 based on matching skills to requirements
    category_scores = {
        'technical_skills': 0, 'programming_skills': 0, 
        'problem_solving': 0, 'projects': 0, 
        'communication': 0, 'education': 0, 'experience': 0
    }
    category_max = {k: 0 for k in category_scores}
    
    user_map = {norm(s["name"]): s for s in user_skills}
    matched = []
    missing_list = []
    partially_matched = []
    
    levels = {"Beginner": 1, "Intermediate": 2, "Advanced": 3, "Expert": 4}
    
    for req in required_skills_with_weights:
        r_name = norm(req["name"])
        # Assume some basic categories if none provided
        cat = req.get("category", "technical_skills")
        if cat not in category_scores: cat = "technical_skills"
        
        r_importance = req.get("importance", 3)
        r_level_val = levels.get(req.get("level", "Intermediate"), 2)
        
        category_max[cat] += r_importance
        
        if r_name in user_map:
            u_skill = user_map[r_name]
            u_level_val = levels.get(u_skill.get("proficiency", "Beginner"), 1)
            
            if u_level_val >= r_level_val:
                matched.append(req["name"])
                category_scores[cat] += r_importance
            else:
                # Add to matched so it doesn't vanish from the UI
                matched.append(req["name"])
                partially_matched.append({
                    "skill": req["name"], 
                    "current": u_skill.get("proficiency", "Beginner"), 
                    "required": req.get("level", "Intermediate")
                })
                category_scores[cat] += r_importance * (u_level_val / r_level_val)
        else:
            missing_list.append(req["name"])

    # Calculate percentages for each feature
    features = []
    for cat in ['technical_skills', 'programming_skills', 'problem_solving', 
                'projects', 'communication', 'education', 'experience']:
        if category_max[cat] > 0:
            score = (category_scores[cat] / category_max[cat]) * 100
        else:
            # Random baseline if category doesn't apply to this job directly but model needs it
            score = np.random.randint(40, 70) if len(user_skills) > 0 else 0
        features.append(score)

    # If the user has explicitly 0 skills added to their profile, override the ML model entirely
    if len(user_skills) == 0:
        overall_match = 0.0
        readiness = 0.0
        strongest = "None"
        missing = required_skills_with_weights[0]["name"] if required_skills_with_weights else "Required Skills"
        level = "Beginner"
    elif models_loaded and model_match is not None:
        X = pd.DataFrame([features], columns=[
            'technical_skills_score', 'programming_skills_score', 
            'problem_solving_score', 'projects_score', 
            'communication_score', 'education_score', 'experience_score'
        ])
        
        overall_match = round(model_match.predict(X)[0], 2)
        readiness = round(model_readiness.predict(X)[0], 2)
        
        strongest = le_strongest.inverse_transform(clf_strongest.predict(X))[0]
        missing = le_missing.inverse_transform(clf_missing.predict(X))[0]
    else:
        # Rule based fallback
        weights = [0.30, 0.20, 0.15, 0.15, 0.10, 0.05, 0.05]
        overall_match = round(sum(f * w for f, w in zip(features, weights)), 2)
        readiness = overall_match
        strongest = "Technical Skills"
        missing = "Problem Solving"

    level = determine_readiness_level(readiness)

    # Generate Markdown Report
    report = f"""================================
AI SKILL TESTER RESULT
================================

Target Job Role:
{target_role_title}

Overall Skill Match:
{overall_match}%

Job Readiness:
{readiness}%

Readiness Level:
{level}

--------------------------------
SKILL ANALYSIS
--------------------------------
Technical Skills: {round(features[0],1)}%
Programming/Domain Skills: {round(features[1],1)}%
Problem Solving: {round(features[2],1)}%
Projects: {round(features[3],1)}%
Communication: {round(features[4],1)}%
Education/Certifications: {round(features[5],1)}%
Experience: {round(features[6],1)}%

--------------------------------
STRONGEST SKILLS
--------------------------------
1. {strongest.replace('_', ' ').title()}
2. {matched[0] if len(matched)>0 else 'Foundational Knowledge'}
3. {matched[1] if len(matched)>1 else 'Adaptability'}

--------------------------------
SKILLS TO IMPROVE
--------------------------------
1. {missing.replace('_', ' ').title()} - Required for complex tasks.
2. {missing_list[0] if len(missing_list)>0 else 'Advanced Tools'} - Industry standard.
3. {missing_list[1] if len(missing_list)>1 else 'Domain Expertise'} - High demand.

--------------------------------
RECOMMENDATIONS
--------------------------------
1. Take an advanced course in {missing.replace('_', ' ').title()}.
2. Practice building end-to-end systems.
3. Build a portfolio project demonstrating {missing_list[0] if len(missing_list)>0 else 'your core skills'}.

--------------------------------
FINAL AI ASSESSMENT
--------------------------------
Based on the analysis, the candidate is at the **{level}** stage with a readiness score of {readiness}%. 
Their strongest area is {strongest.replace('_', ' ').title()}, while the critical gap remains in {missing.replace('_', ' ').title()}. 
Focusing on practical projects and completing certifications in the missing skills will greatly enhance their suitability for the {target_role_title} role.
"""

    return {
        "readiness_score": readiness,
        "matched_skills": matched,
        "partially_matched_skills": partially_matched,
        "missing_skills": missing_list,
        "markdown_report": report
    }
