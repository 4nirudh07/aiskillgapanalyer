import io, re
from pathlib import Path

SKILLS = [
    "Python","Java","C++","JavaScript","TypeScript","HTML","CSS","React",
    "Node.js","Django","Flask","FastAPI","MySQL","PostgreSQL","MongoDB","SQL",
    "Redis","Pandas","NumPy","Matplotlib","Machine Learning","Deep Learning",
    "NLP","Computer Vision","Scikit-learn","TensorFlow","PyTorch","AWS","Azure",
    "Docker","Kubernetes","Git","GitHub","Linux"
]

def _text(data: bytes, filename: str) -> str:
    ext = Path(filename).suffix.lower()
    try:
        if ext == ".pdf":
            import pymupdf as fitz
            doc = fitz.open(stream=data, filetype="pdf")
            return "\n".join(page.get_text() for page in doc)
        if ext == ".docx":
            from docx import Document
            doc = Document(io.BytesIO(data))
            return "\n".join(p.text for p in doc.paragraphs)
    except Exception as e:
        print(f"Error extracting text from {filename}: {e}")
    return data.decode("utf-8", errors="ignore")

def extract_skills(data: bytes, filename: str):
    text = _text(data, filename).lower()
    found = []
    # Pad text with spaces for simple boundary checking
    padded_text = " " + re.sub(r'[^a-z0-9+#]', ' ', text) + " "
    for skill in SKILLS:
        # Simple string inclusion check for skills with special chars
        if skill.lower() == "c++" and "c++" in text:
            found.append(skill)
        elif skill.lower() == "node.js" and "node.js" in text:
            found.append(skill)
        elif " " + skill.lower() + " " in padded_text:
            found.append(skill)
    return sorted(set(found))
