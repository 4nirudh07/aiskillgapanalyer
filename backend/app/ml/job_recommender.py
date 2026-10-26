from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_jobs(user_skills, jobs):
    """
    user_skills: list of skill names (strings)
    """
    if not jobs:
        return []
    
    user_text = " ".join([s.lower() for s in user_skills])
    if not user_text.strip():
        user_text = "none" # fallback
        
    corpus = [user_text] + [
        j["title"] + " " + j.get("description", "") + " " + " ".join(j.get("required_skills", []))
        for j in jobs
    ]
    
    matrix = TfidfVectorizer(stop_words="english").fit_transform(corpus)
    scores = cosine_similarity(matrix[0:1], matrix[1:]).flatten()
    
    result = []
    for job, score in zip(jobs, scores):
        required = {x.lower() for x in job.get("required_skills", [])}
        user = {x.lower() for x in user_skills}
        
        matched_set = required & user
        missing_set = required - user
        
        skill_score = len(matched_set) / len(required) if required else 0
        final = round((0.65 * skill_score + 0.35 * float(score)) * 100, 1)
        
        why_recommended = ""
        if skill_score > 0.8:
            why_recommended = "Excellent skill match for your profile."
        elif skill_score > 0.5:
            why_recommended = "Good match, with a few missing skills to learn."
        elif float(score) > 0.2:
            why_recommended = "Related to your overall career trajectory based on title/description."
        else:
            why_recommended = "Suggested for exploring a new path."
            
        result.append({
            "job_id": job["job_id"],
            "title": job["title"],
            "company": job["company"],
            "location": job["location"],
            "work_mode": job.get("work_mode", "Hybrid"),
            "experience": job.get("experience", "Not specified"),
            "salary": job.get("salary", "Not disclosed"),
            "match_percentage": final,
            "matched_skills": list(matched_set),
            "missing_skills": list(missing_set),
            "required_skills": job.get("required_skills", []),
            "why_recommended": why_recommended
        })
        
    return sorted(result, key=lambda x: x["match_percentage"], reverse=True)
