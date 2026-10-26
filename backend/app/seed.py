from .database import get_db

ROLES = [
    {
        "role_id": "ROLE001",
        "title": "Machine Learning Engineer",
        "description": "Professional role for a Machine Learning Engineer.",
        "skills": [
            {
                "name": "Python",
                "category": "Programming",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Machine Learning",
                "category": "AI/ML",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "Scikit-learn",
                "category": "AI/ML",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Pandas",
                "category": "Data Science",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "NumPy",
                "category": "Data Science",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Statistics",
                "category": "Other",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "TensorFlow",
                "category": "AI/ML",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "SQL",
                "category": "Database",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Docker",
                "category": "DevOps",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Git",
                "category": "Tools",
                "importance": 5,
                "level": "Intermediate"
            }
        ]
    },
    {
        "role_id": "ROLE002",
        "title": "Full Stack Developer",
        "description": "Professional role for a Full Stack Developer.",
        "skills": [
            {
                "name": "JavaScript",
                "category": "Programming",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "React",
                "category": "Frontend",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "Node.js",
                "category": "Backend",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "HTML",
                "category": "Frontend",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "CSS",
                "category": "Frontend",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "MongoDB",
                "category": "Database",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "SQL",
                "category": "Database",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "Git",
                "category": "Tools",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "TypeScript",
                "category": "Programming",
                "importance": 5,
                "level": "Advanced"
            }
        ]
    },
    {
        "role_id": "ROLE003",
        "title": "Data Analyst",
        "description": "Professional role for a Data Analyst.",
        "skills": [
            {
                "name": "SQL",
                "category": "Database",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "Python",
                "category": "Programming",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Pandas",
                "category": "Data Science",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "NumPy",
                "category": "Data Science",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Matplotlib",
                "category": "Data Science",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Statistics",
                "category": "Other",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "Excel",
                "category": "Tools",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "Tableau",
                "category": "Tools",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Power BI",
                "category": "Tools",
                "importance": 3,
                "level": "Intermediate"
            }
        ]
    },
    {
        "role_id": "ROLE004",
        "title": "Frontend Developer",
        "description": "Professional role for a Frontend Developer.",
        "skills": [
            {
                "name": "HTML",
                "category": "Frontend",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "CSS",
                "category": "Frontend",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "JavaScript",
                "category": "Programming",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "React",
                "category": "Frontend",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Vue.js",
                "category": "Frontend",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Tailwind CSS",
                "category": "Frontend",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Figma",
                "category": "Design",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Git",
                "category": "Tools",
                "importance": 5,
                "level": "Intermediate"
            }
        ]
    },
    {
        "role_id": "ROLE005",
        "title": "Backend Developer",
        "description": "Professional role for a Backend Developer.",
        "skills": [
            {
                "name": "Python",
                "category": "Programming",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Java",
                "category": "Programming",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "Node.js",
                "category": "Backend",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "SQL",
                "category": "Database",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "PostgreSQL",
                "category": "Database",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Docker",
                "category": "DevOps",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Redis",
                "category": "Database",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "AWS",
                "category": "Cloud",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Git",
                "category": "Tools",
                "importance": 3,
                "level": "Intermediate"
            }
        ]
    },
    {
        "role_id": "ROLE006",
        "title": "Data Scientist",
        "description": "Professional role for a Data Scientist.",
        "skills": [
            {
                "name": "Python",
                "category": "Programming",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Machine Learning",
                "category": "AI/ML",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "Statistics",
                "category": "Other",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Pandas",
                "category": "Data Science",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "NumPy",
                "category": "Data Science",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "SQL",
                "category": "Database",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Deep Learning",
                "category": "AI/ML",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "NLP",
                "category": "AI/ML",
                "importance": 3,
                "level": "Intermediate"
            }
        ]
    },
    {
        "role_id": "ROLE007",
        "title": "DevOps Engineer",
        "description": "Professional role for a DevOps Engineer.",
        "skills": [
            {
                "name": "Linux",
                "category": "IT",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "Docker",
                "category": "DevOps",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Kubernetes",
                "category": "DevOps",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "AWS",
                "category": "Cloud",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "CI/CD",
                "category": "DevOps",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Bash",
                "category": "Tools",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Python",
                "category": "Programming",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "Terraform",
                "category": "DevOps",
                "importance": 5,
                "level": "Advanced"
            }
        ]
    },
    {
        "role_id": "ROLE008",
        "title": "Cloud Engineer",
        "description": "Professional role for a Cloud Engineer.",
        "skills": [
            {
                "name": "AWS",
                "category": "Cloud",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Azure",
                "category": "Cloud",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "GCP",
                "category": "Cloud",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Linux",
                "category": "IT",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Networking",
                "category": "IT",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Docker",
                "category": "DevOps",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "Terraform",
                "category": "DevOps",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "Python",
                "category": "Programming",
                "importance": 4,
                "level": "Advanced"
            }
        ]
    },
    {
        "role_id": "ROLE009",
        "title": "Cybersecurity Analyst",
        "description": "Professional role for a Cybersecurity Analyst.",
        "skills": [
            {
                "name": "Networking",
                "category": "IT",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Linux",
                "category": "IT",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Python",
                "category": "Programming",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Security",
                "category": "Security",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "Bash",
                "category": "Tools",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Wireshark",
                "category": "Security",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Cryptography",
                "category": "Security",
                "importance": 5,
                "level": "Advanced"
            }
        ]
    },
    {
        "role_id": "ROLE010",
        "title": "Mobile Developer",
        "description": "Professional role for a Mobile Developer.",
        "skills": [
            {
                "name": "Swift",
                "category": "Programming",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Kotlin",
                "category": "Programming",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "React Native",
                "category": "Frontend",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Flutter",
                "category": "Frontend",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Java",
                "category": "Programming",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Git",
                "category": "Tools",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "UI/UX",
                "category": "Design",
                "importance": 3,
                "level": "Intermediate"
            }
        ]
    },
    {
        "role_id": "ROLE011",
        "title": "AI Engineer",
        "description": "Professional role for a AI Engineer.",
        "skills": [
            {
                "name": "Python",
                "category": "Programming",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "Deep Learning",
                "category": "AI/ML",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "TensorFlow",
                "category": "AI/ML",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "PyTorch",
                "category": "AI/ML",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "NLP",
                "category": "AI/ML",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "Machine Learning",
                "category": "AI/ML",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Mathematics",
                "category": "Other",
                "importance": 5,
                "level": "Intermediate"
            }
        ]
    },
    {
        "role_id": "ROLE012",
        "title": "Database Administrator",
        "description": "Professional role for a Database Administrator.",
        "skills": [
            {
                "name": "SQL",
                "category": "Database",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "PostgreSQL",
                "category": "Database",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "MySQL",
                "category": "Database",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Oracle",
                "category": "Database",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "MongoDB",
                "category": "Database",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "Linux",
                "category": "IT",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Performance Tuning",
                "category": "Database",
                "importance": 5,
                "level": "Advanced"
            }
        ]
    },
    {
        "role_id": "ROLE013",
        "title": "System Administrator",
        "description": "Professional role for a System Administrator.",
        "skills": [
            {
                "name": "Linux",
                "category": "IT",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Windows Server",
                "category": "IT",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Networking",
                "category": "IT",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Bash",
                "category": "Tools",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "PowerShell",
                "category": "Tools",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Active Directory",
                "category": "IT",
                "importance": 4,
                "level": "Advanced"
            }
        ]
    },
    {
        "role_id": "ROLE014",
        "title": "Product Manager",
        "description": "Professional role for a Product Manager.",
        "skills": [
            {
                "name": "Agile",
                "category": "Soft Skills",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "Scrum",
                "category": "Soft Skills",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Jira",
                "category": "Tools",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Communication",
                "category": "Soft Skills",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "Data Analysis",
                "category": "Data Science",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "SQL",
                "category": "Database",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "UI/UX",
                "category": "Design",
                "importance": 4,
                "level": "Advanced"
            }
        ]
    },
    {
        "role_id": "ROLE015",
        "title": "UX/UI Designer",
        "description": "Professional role for a UX/UI Designer.",
        "skills": [
            {
                "name": "Figma",
                "category": "Design",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Adobe XD",
                "category": "Design",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Sketch",
                "category": "Design",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "HTML",
                "category": "Frontend",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "CSS",
                "category": "Frontend",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Wireframing",
                "category": "Design",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Prototyping",
                "category": "Design",
                "importance": 3,
                "level": "Intermediate"
            }
        ]
    },
    {
        "role_id": "ROLE016",
        "title": "QA Engineer",
        "description": "Professional role for a QA Engineer.",
        "skills": [
            {
                "name": "Testing",
                "category": "Other",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Selenium",
                "category": "Tools",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Python",
                "category": "Programming",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Java",
                "category": "Programming",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "Cypress",
                "category": "Tools",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Git",
                "category": "Tools",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "Jira",
                "category": "Tools",
                "importance": 3,
                "level": "Intermediate"
            }
        ]
    },
    {
        "role_id": "ROLE017",
        "title": "Blockchain Developer",
        "description": "Professional role for a Blockchain Developer.",
        "skills": [
            {
                "name": "Solidity",
                "category": "Programming",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Blockchain",
                "category": "Other",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Cryptography",
                "category": "Security",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "JavaScript",
                "category": "Programming",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Node.js",
                "category": "Backend",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Go",
                "category": "Programming",
                "importance": 4,
                "level": "Advanced"
            }
        ]
    },
    {
        "role_id": "ROLE018",
        "title": "Game Developer",
        "description": "Professional role for a Game Developer.",
        "skills": [
            {
                "name": "C#",
                "category": "Programming",
                "importance": 5,
                "level": "Intermediate"
            },
            {
                "name": "C++",
                "category": "Programming",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Unity",
                "category": "Other",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Unreal Engine",
                "category": "Other",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Mathematics",
                "category": "Other",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "Physics",
                "category": "Other",
                "importance": 4,
                "level": "Intermediate"
            }
        ]
    },
    {
        "role_id": "ROLE019",
        "title": "Data Engineer",
        "description": "Professional role for a Data Engineer.",
        "skills": [
            {
                "name": "Python",
                "category": "Programming",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "SQL",
                "category": "Database",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "Hadoop",
                "category": "Data Science",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "Spark",
                "category": "Data Science",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "AWS",
                "category": "Cloud",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Kafka",
                "category": "Data Science",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "Airflow",
                "category": "Data Science",
                "importance": 5,
                "level": "Advanced"
            },
            {
                "name": "ETL",
                "category": "Data Science",
                "importance": 4,
                "level": "Advanced"
            }
        ]
    },
    {
        "role_id": "ROLE020",
        "title": "Business Analyst",
        "description": "Professional role for a Business Analyst.",
        "skills": [
            {
                "name": "SQL",
                "category": "Database",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "Excel",
                "category": "Tools",
                "importance": 4,
                "level": "Intermediate"
            },
            {
                "name": "Tableau",
                "category": "Tools",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Requirements Gathering",
                "category": "Soft Skills",
                "importance": 3,
                "level": "Intermediate"
            },
            {
                "name": "Communication",
                "category": "Soft Skills",
                "importance": 4,
                "level": "Advanced"
            },
            {
                "name": "Agile",
                "category": "Soft Skills",
                "importance": 5,
                "level": "Advanced"
            }
        ]
    }
]

JOBS = [
    {
        "job_id": "JOB001",
        "title": "Senior Blockchain Developer",
        "company": "Tech Giant",
        "location": "Austin, TX",
        "work_mode": "Hybrid",
        "experience": "1-3 years",
        "salary": "$117k - $153k",
        "description": "We are looking for a skilled Senior Blockchain Developer to join our team.",
        "required_skills": [
            "Cryptography",
            "JavaScript",
            "Blockchain",
            "Solidity",
            "Go",
            "Node.js"
        ]
    },
    {
        "job_id": "JOB002",
        "title": "Junior Frontend Developer",
        "company": "AI Labs",
        "location": "Bangalore, IN",
        "work_mode": "On-site",
        "experience": "5+ years",
        "salary": "$119k - $144k",
        "description": "We are looking for a skilled Junior Frontend Developer to join our team.",
        "required_skills": [
            "HTML",
            "Tailwind CSS",
            "Git",
            "React",
            "Figma",
            "JavaScript",
            "Vue.js",
            "CSS"
        ]
    },
    {
        "job_id": "JOB003",
        "title": "Principal Data Analyst",
        "company": "FinTech Co",
        "location": "New York, NY",
        "work_mode": "On-site",
        "experience": "2-4 years",
        "salary": "$123k - $182k",
        "description": "We are looking for a skilled Principal Data Analyst to join our team.",
        "required_skills": [
            "Python",
            "NumPy",
            "SQL",
            "Statistics",
            "Power BI"
        ]
    },
    {
        "job_id": "JOB004",
        "title": "Lead Blockchain Developer",
        "company": "AI Labs",
        "location": "Bangalore, IN",
        "work_mode": "Remote",
        "experience": "5+ years",
        "salary": "$139k - $168k",
        "description": "We are looking for a skilled Lead Blockchain Developer to join our team.",
        "required_skills": [
            "Node.js",
            "Blockchain",
            "Cryptography",
            "Solidity"
        ]
    },
    {
        "job_id": "JOB005",
        "title": "Cloud Engineer",
        "company": "Game Studio",
        "location": "Remote",
        "work_mode": "Remote",
        "experience": "1-3 years",
        "salary": "$141k - $162k",
        "description": "We are looking for a skilled Cloud Engineer to join our team.",
        "required_skills": [
            "GCP",
            "Networking",
            "Docker",
            "Azure",
            "Terraform",
            "Python"
        ]
    },
    {
        "job_id": "JOB006",
        "title": "Junior Full Stack Developer",
        "company": "AI Labs",
        "location": "Sydney, AU",
        "work_mode": "Remote",
        "experience": "1-3 years",
        "salary": "$88k - $125k",
        "description": "We are looking for a skilled Junior Full Stack Developer to join our team.",
        "required_skills": [
            "MongoDB",
            "JavaScript",
            "SQL",
            "CSS",
            "React",
            "Git"
        ]
    },
    {
        "job_id": "JOB007",
        "title": "Cybersecurity Analyst",
        "company": "AI Labs",
        "location": "Austin, TX",
        "work_mode": "Hybrid",
        "experience": "0-2 years",
        "salary": "$75k - $100k",
        "description": "We are looking for a skilled Cybersecurity Analyst to join our team.",
        "required_skills": [
            "Wireshark",
            "Cryptography",
            "Linux"
        ]
    },
    {
        "job_id": "JOB008",
        "title": "Lead Database Administrator",
        "company": "HealthTech",
        "location": "San Francisco, CA",
        "work_mode": "On-site",
        "experience": "2-4 years",
        "salary": "$70k - $115k",
        "description": "We are looking for a skilled Lead Database Administrator to join our team.",
        "required_skills": [
            "Linux",
            "Performance Tuning",
            "MongoDB"
        ]
    },
    {
        "job_id": "JOB009",
        "title": "Principal Data Engineer",
        "company": "HealthTech",
        "location": "San Francisco, CA",
        "work_mode": "Hybrid",
        "experience": "3-5 years",
        "salary": "$137k - $197k",
        "description": "We are looking for a skilled Principal Data Engineer to join our team.",
        "required_skills": [
            "Spark",
            "Airflow",
            "ETL",
            "SQL",
            "Python",
            "AWS"
        ]
    },
    {
        "job_id": "JOB010",
        "title": "Frontend Developer",
        "company": "Tech Giant",
        "location": "Sydney, AU",
        "work_mode": "On-site",
        "experience": "5+ years",
        "salary": "$118k - $163k",
        "description": "We are looking for a skilled Frontend Developer to join our team.",
        "required_skills": [
            "CSS",
            "Git",
            "Tailwind CSS"
        ]
    },
    {
        "job_id": "JOB011",
        "title": "Senior Data Analyst",
        "company": "DataWorks",
        "location": "Berlin, DE",
        "work_mode": "Hybrid",
        "experience": "2-4 years",
        "salary": "$101k - $144k",
        "description": "We are looking for a skilled Senior Data Analyst to join our team.",
        "required_skills": [
            "Tableau",
            "Matplotlib",
            "Excel",
            "Python"
        ]
    },
    {
        "job_id": "JOB012",
        "title": "Principal QA Engineer",
        "company": "WebNova",
        "location": "New York, NY",
        "work_mode": "On-site",
        "experience": "0-2 years",
        "salary": "$96k - $156k",
        "description": "We are looking for a skilled Principal QA Engineer to join our team.",
        "required_skills": [
            "Git",
            "Java",
            "Testing",
            "Jira",
            "Cypress",
            "Selenium",
            "Python"
        ]
    },
    {
        "job_id": "JOB013",
        "title": "Senior Data Analyst",
        "company": "FinTech Co",
        "location": "Sydney, AU",
        "work_mode": "On-site",
        "experience": "1-3 years",
        "salary": "$115k - $139k",
        "description": "We are looking for a skilled Senior Data Analyst to join our team.",
        "required_skills": [
            "Statistics",
            "Tableau",
            "Python",
            "Excel",
            "SQL",
            "NumPy",
            "Matplotlib",
            "Pandas"
        ]
    },
    {
        "job_id": "JOB014",
        "title": "Senior Full Stack Developer",
        "company": "WebNova",
        "location": "New York, NY",
        "work_mode": "Remote",
        "experience": "0-2 years",
        "salary": "$76k - $132k",
        "description": "We are looking for a skilled Senior Full Stack Developer to join our team.",
        "required_skills": [
            "TypeScript",
            "JavaScript",
            "Node.js"
        ]
    },
    {
        "job_id": "JOB015",
        "title": "Lead Cybersecurity Analyst",
        "company": "CyberSec Corp",
        "location": "Bangalore, IN",
        "work_mode": "Remote",
        "experience": "3-5 years",
        "salary": "$79k - $136k",
        "description": "We are looking for a skilled Lead Cybersecurity Analyst to join our team.",
        "required_skills": [
            "Security",
            "Linux",
            "Python",
            "Networking",
            "Cryptography",
            "Bash"
        ]
    },
    {
        "job_id": "JOB016",
        "title": "Junior Cloud Engineer",
        "company": "Cloud Systems",
        "location": "Sydney, AU",
        "work_mode": "On-site",
        "experience": "1-3 years",
        "salary": "$139k - $185k",
        "description": "We are looking for a skilled Junior Cloud Engineer to join our team.",
        "required_skills": [
            "GCP",
            "Terraform",
            "Python",
            "Linux"
        ]
    },
    {
        "job_id": "JOB017",
        "title": "Principal DevOps Engineer",
        "company": "WebNova",
        "location": "Sydney, AU",
        "work_mode": "Remote",
        "experience": "Senior",
        "salary": "$117k - $154k",
        "description": "We are looking for a skilled Principal DevOps Engineer to join our team.",
        "required_skills": [
            "Bash",
            "AWS",
            "Kubernetes"
        ]
    },
    {
        "job_id": "JOB018",
        "title": "Junior Frontend Developer",
        "company": "Tech Giant",
        "location": "Austin, TX",
        "work_mode": "Remote",
        "experience": "1-3 years",
        "salary": "$90k - $150k",
        "description": "We are looking for a skilled Junior Frontend Developer to join our team.",
        "required_skills": [
            "Vue.js",
            "React",
            "Figma",
            "JavaScript",
            "Tailwind CSS",
            "CSS"
        ]
    },
    {
        "job_id": "JOB019",
        "title": "Principal Data Analyst",
        "company": "FinTech Co",
        "location": "Bangalore, IN",
        "work_mode": "On-site",
        "experience": "3-5 years",
        "salary": "$120k - $171k",
        "description": "We are looking for a skilled Principal Data Analyst to join our team.",
        "required_skills": [
            "Tableau",
            "Power BI",
            "Excel",
            "Pandas",
            "Statistics",
            "Matplotlib"
        ]
    },
    {
        "job_id": "JOB020",
        "title": "Junior Frontend Developer",
        "company": "WebNova",
        "location": "Seattle, WA",
        "work_mode": "Remote",
        "experience": "Senior",
        "salary": "$64k - $109k",
        "description": "We are looking for a skilled Junior Frontend Developer to join our team.",
        "required_skills": [
            "CSS",
            "Tailwind CSS",
            "HTML",
            "JavaScript"
        ]
    },
    {
        "job_id": "JOB021",
        "title": "Junior Machine Learning Engineer",
        "company": "CyberSec Corp",
        "location": "New York, NY",
        "work_mode": "Remote",
        "experience": "2-4 years",
        "salary": "$119k - $139k",
        "description": "We are looking for a skilled Junior Machine Learning Engineer to join our team.",
        "required_skills": [
            "Statistics",
            "SQL",
            "Python",
            "Git",
            "Pandas",
            "Scikit-learn",
            "NumPy",
            "TensorFlow",
            "Machine Learning"
        ]
    },
    {
        "job_id": "JOB022",
        "title": "Junior Mobile Developer",
        "company": "StartUp Inc",
        "location": "Remote",
        "work_mode": "Remote",
        "experience": "1-3 years",
        "salary": "$88k - $138k",
        "description": "We are looking for a skilled Junior Mobile Developer to join our team.",
        "required_skills": [
            "React Native",
            "Java",
            "Kotlin",
            "Git",
            "Flutter",
            "Swift",
            "UI/UX"
        ]
    },
    {
        "job_id": "JOB023",
        "title": "Lead Cybersecurity Analyst",
        "company": "Blockchain Inc",
        "location": "Sydney, AU",
        "work_mode": "On-site",
        "experience": "5+ years",
        "salary": "$139k - $170k",
        "description": "We are looking for a skilled Lead Cybersecurity Analyst to join our team.",
        "required_skills": [
            "Linux",
            "Networking",
            "Cryptography"
        ]
    },
    {
        "job_id": "JOB024",
        "title": "Junior Cybersecurity Analyst",
        "company": "Blockchain Inc",
        "location": "Bangalore, IN",
        "work_mode": "Hybrid",
        "experience": "1-3 years",
        "salary": "$127k - $148k",
        "description": "We are looking for a skilled Junior Cybersecurity Analyst to join our team.",
        "required_skills": [
            "Security",
            "Networking",
            "Bash",
            "Wireshark",
            "Python"
        ]
    },
    {
        "job_id": "JOB025",
        "title": "Principal QA Engineer",
        "company": "E-commerce Giant",
        "location": "London, UK",
        "work_mode": "Remote",
        "experience": "1-3 years",
        "salary": "$124k - $169k",
        "description": "We are looking for a skilled Principal QA Engineer to join our team.",
        "required_skills": [
            "Cypress",
            "Jira",
            "Testing"
        ]
    },
    {
        "job_id": "JOB026",
        "title": "Senior Mobile Developer",
        "company": "Game Studio",
        "location": "Toronto, CA",
        "work_mode": "On-site",
        "experience": "Senior",
        "salary": "$102k - $144k",
        "description": "We are looking for a skilled Senior Mobile Developer to join our team.",
        "required_skills": [
            "Git",
            "Swift",
            "UI/UX",
            "React Native",
            "Kotlin"
        ]
    },
    {
        "job_id": "JOB027",
        "title": "Data Engineer",
        "company": "E-commerce Giant",
        "location": "Seattle, WA",
        "work_mode": "Remote",
        "experience": "5+ years",
        "salary": "$62k - $104k",
        "description": "We are looking for a skilled Data Engineer to join our team.",
        "required_skills": [
            "Hadoop",
            "SQL",
            "ETL",
            "AWS",
            "Spark"
        ]
    },
    {
        "job_id": "JOB028",
        "title": "Lead DevOps Engineer",
        "company": "Blockchain Inc",
        "location": "New York, NY",
        "work_mode": "Remote",
        "experience": "3-5 years",
        "salary": "$127k - $148k",
        "description": "We are looking for a skilled Lead DevOps Engineer to join our team.",
        "required_skills": [
            "Kubernetes",
            "CI/CD",
            "Terraform"
        ]
    },
    {
        "job_id": "JOB029",
        "title": "Lead Frontend Developer",
        "company": "Global Solutions",
        "location": "Berlin, DE",
        "work_mode": "Hybrid",
        "experience": "5+ years",
        "salary": "$121k - $152k",
        "description": "We are looking for a skilled Lead Frontend Developer to join our team.",
        "required_skills": [
            "JavaScript",
            "Figma",
            "HTML"
        ]
    },
    {
        "job_id": "JOB030",
        "title": "Lead Data Engineer",
        "company": "CyberSec Corp",
        "location": "Bangalore, IN",
        "work_mode": "Remote",
        "experience": "Senior",
        "salary": "$79k - $119k",
        "description": "We are looking for a skilled Lead Data Engineer to join our team.",
        "required_skills": [
            "Airflow",
            "Hadoop",
            "SQL",
            "Python",
            "Kafka",
            "ETL",
            "AWS"
        ]
    },
    {
        "job_id": "JOB031",
        "title": "Principal UX/UI Designer",
        "company": "Blockchain Inc",
        "location": "Toronto, CA",
        "work_mode": "Remote",
        "experience": "3-5 years",
        "salary": "$94k - $154k",
        "description": "We are looking for a skilled Principal UX/UI Designer to join our team.",
        "required_skills": [
            "Sketch",
            "Figma",
            "HTML",
            "Prototyping",
            "Adobe XD",
            "Wireframing"
        ]
    },
    {
        "job_id": "JOB032",
        "title": "Senior Database Administrator",
        "company": "Tech Giant",
        "location": "Seattle, WA",
        "work_mode": "Hybrid",
        "experience": "Senior",
        "salary": "$109k - $146k",
        "description": "We are looking for a skilled Senior Database Administrator to join our team.",
        "required_skills": [
            "Oracle",
            "Linux",
            "PostgreSQL",
            "SQL",
            "MySQL",
            "Performance Tuning"
        ]
    },
    {
        "job_id": "JOB033",
        "title": "Principal Full Stack Developer",
        "company": "DataWorks",
        "location": "San Francisco, CA",
        "work_mode": "On-site",
        "experience": "Senior",
        "salary": "$93k - $120k",
        "description": "We are looking for a skilled Principal Full Stack Developer to join our team.",
        "required_skills": [
            "HTML",
            "CSS",
            "Node.js",
            "TypeScript",
            "JavaScript",
            "Git"
        ]
    },
    {
        "job_id": "JOB034",
        "title": "Lead UX/UI Designer",
        "company": "StartUp Inc",
        "location": "Seattle, WA",
        "work_mode": "On-site",
        "experience": "5+ years",
        "salary": "$104k - $162k",
        "description": "We are looking for a skilled Lead UX/UI Designer to join our team.",
        "required_skills": [
            "Figma",
            "Wireframing",
            "Prototyping",
            "Sketch",
            "CSS",
            "HTML"
        ]
    },
    {
        "job_id": "JOB035",
        "title": "Data Scientist",
        "company": "EduTech",
        "location": "San Francisco, CA",
        "work_mode": "Hybrid",
        "experience": "2-4 years",
        "salary": "$81k - $130k",
        "description": "We are looking for a skilled Data Scientist to join our team.",
        "required_skills": [
            "Statistics",
            "Deep Learning",
            "SQL",
            "Python",
            "Pandas"
        ]
    },
    {
        "job_id": "JOB036",
        "title": "Lead Machine Learning Engineer",
        "company": "DataWorks",
        "location": "Toronto, CA",
        "work_mode": "Remote",
        "experience": "Senior",
        "salary": "$145k - $180k",
        "description": "We are looking for a skilled Lead Machine Learning Engineer to join our team.",
        "required_skills": [
            "Statistics",
            "Git",
            "Python"
        ]
    },
    {
        "job_id": "JOB037",
        "title": "Junior Game Developer",
        "company": "AI Labs",
        "location": "Austin, TX",
        "work_mode": "Remote",
        "experience": "3-5 years",
        "salary": "$74k - $129k",
        "description": "We are looking for a skilled Junior Game Developer to join our team.",
        "required_skills": [
            "Unreal Engine",
            "C#",
            "Physics"
        ]
    },
    {
        "job_id": "JOB038",
        "title": "Blockchain Developer",
        "company": "EduTech",
        "location": "Austin, TX",
        "work_mode": "Remote",
        "experience": "3-5 years",
        "salary": "$117k - $154k",
        "description": "We are looking for a skilled Blockchain Developer to join our team.",
        "required_skills": [
            "Node.js",
            "Go",
            "Blockchain",
            "Cryptography",
            "JavaScript",
            "Solidity"
        ]
    },
    {
        "job_id": "JOB039",
        "title": "Senior Data Engineer",
        "company": "StartUp Inc",
        "location": "Austin, TX",
        "work_mode": "Hybrid",
        "experience": "Senior",
        "salary": "$137k - $176k",
        "description": "We are looking for a skilled Senior Data Engineer to join our team.",
        "required_skills": [
            "Spark",
            "Airflow",
            "Python"
        ]
    },
    {
        "job_id": "JOB040",
        "title": "Business Analyst",
        "company": "StartUp Inc",
        "location": "Austin, TX",
        "work_mode": "Remote",
        "experience": "2-4 years",
        "salary": "$142k - $164k",
        "description": "We are looking for a skilled Business Analyst to join our team.",
        "required_skills": [
            "SQL",
            "Communication",
            "Tableau",
            "Agile",
            "Requirements Gathering",
            "Excel"
        ]
    },
    {
        "job_id": "JOB041",
        "title": "Cloud Engineer",
        "company": "HealthTech",
        "location": "Austin, TX",
        "work_mode": "Hybrid",
        "experience": "3-5 years",
        "salary": "$115k - $145k",
        "description": "We are looking for a skilled Cloud Engineer to join our team.",
        "required_skills": [
            "Terraform",
            "Networking",
            "Python",
            "AWS",
            "Azure",
            "GCP",
            "Linux",
            "Docker"
        ]
    },
    {
        "job_id": "JOB042",
        "title": "Junior Frontend Developer",
        "company": "Tech Giant",
        "location": "Toronto, CA",
        "work_mode": "Remote",
        "experience": "0-2 years",
        "salary": "$146k - $198k",
        "description": "We are looking for a skilled Junior Frontend Developer to join our team.",
        "required_skills": [
            "Vue.js",
            "React",
            "Git",
            "Figma",
            "CSS",
            "JavaScript"
        ]
    },
    {
        "job_id": "JOB043",
        "title": "Lead Data Analyst",
        "company": "StartUp Inc",
        "location": "Seattle, WA",
        "work_mode": "Hybrid",
        "experience": "2-4 years",
        "salary": "$141k - $199k",
        "description": "We are looking for a skilled Lead Data Analyst to join our team.",
        "required_skills": [
            "Power BI",
            "Pandas",
            "SQL",
            "Excel",
            "Python",
            "Tableau",
            "Statistics",
            "Matplotlib",
            "NumPy"
        ]
    },
    {
        "job_id": "JOB044",
        "title": "Principal Cybersecurity Analyst",
        "company": "AI Labs",
        "location": "Sydney, AU",
        "work_mode": "Remote",
        "experience": "1-3 years",
        "salary": "$145k - $167k",
        "description": "We are looking for a skilled Principal Cybersecurity Analyst to join our team.",
        "required_skills": [
            "Linux",
            "Wireshark",
            "Networking",
            "Bash"
        ]
    },
    {
        "job_id": "JOB045",
        "title": "Lead QA Engineer",
        "company": "Blockchain Inc",
        "location": "San Francisco, CA",
        "work_mode": "Remote",
        "experience": "5+ years",
        "salary": "$83k - $124k",
        "description": "We are looking for a skilled Lead QA Engineer to join our team.",
        "required_skills": [
            "Git",
            "Jira",
            "Testing",
            "Selenium"
        ]
    },
    {
        "job_id": "JOB046",
        "title": "Junior Product Manager",
        "company": "WebNova",
        "location": "Berlin, DE",
        "work_mode": "Remote",
        "experience": "0-2 years",
        "salary": "$99k - $150k",
        "description": "We are looking for a skilled Junior Product Manager to join our team.",
        "required_skills": [
            "UI/UX",
            "Data Analysis",
            "Jira",
            "SQL",
            "Agile"
        ]
    },
    {
        "job_id": "JOB047",
        "title": "Lead Blockchain Developer",
        "company": "WebNova",
        "location": "San Francisco, CA",
        "work_mode": "Remote",
        "experience": "5+ years",
        "salary": "$112k - $167k",
        "description": "We are looking for a skilled Lead Blockchain Developer to join our team.",
        "required_skills": [
            "Go",
            "Node.js",
            "Blockchain"
        ]
    },
    {
        "job_id": "JOB048",
        "title": "Game Developer",
        "company": "HealthTech",
        "location": "Austin, TX",
        "work_mode": "Remote",
        "experience": "Senior",
        "salary": "$102k - $140k",
        "description": "We are looking for a skilled Game Developer to join our team.",
        "required_skills": [
            "Unity",
            "Physics",
            "C++"
        ]
    },
    {
        "job_id": "JOB049",
        "title": "Lead Business Analyst",
        "company": "WebNova",
        "location": "Toronto, CA",
        "work_mode": "On-site",
        "experience": "5+ years",
        "salary": "$131k - $176k",
        "description": "We are looking for a skilled Lead Business Analyst to join our team.",
        "required_skills": [
            "Excel",
            "SQL",
            "Agile"
        ]
    },
    {
        "job_id": "JOB050",
        "title": "Junior Blockchain Developer",
        "company": "StartUp Inc",
        "location": "Bangalore, IN",
        "work_mode": "Hybrid",
        "experience": "5+ years",
        "salary": "$97k - $142k",
        "description": "We are looking for a skilled Junior Blockchain Developer to join our team.",
        "required_skills": [
            "Node.js",
            "Blockchain",
            "JavaScript",
            "Solidity",
            "Go"
        ]
    },
    {
        "job_id": "JOB051",
        "title": "Principal Frontend Developer",
        "company": "Blockchain Inc",
        "location": "London, UK",
        "work_mode": "On-site",
        "experience": "2-4 years",
        "salary": "$137k - $173k",
        "description": "We are looking for a skilled Principal Frontend Developer to join our team.",
        "required_skills": [
            "HTML",
            "Figma",
            "JavaScript",
            "Git",
            "Vue.js",
            "CSS",
            "Tailwind CSS"
        ]
    },
    {
        "job_id": "JOB052",
        "title": "Senior Game Developer",
        "company": "Game Studio",
        "location": "New York, NY",
        "work_mode": "On-site",
        "experience": "5+ years",
        "salary": "$92k - $147k",
        "description": "We are looking for a skilled Senior Game Developer to join our team.",
        "required_skills": [
            "Unreal Engine",
            "Mathematics",
            "Unity",
            "C#",
            "C++"
        ]
    },
    {
        "job_id": "JOB053",
        "title": "Cloud Engineer",
        "company": "DataWorks",
        "location": "New York, NY",
        "work_mode": "Hybrid",
        "experience": "0-2 years",
        "salary": "$89k - $147k",
        "description": "We are looking for a skilled Cloud Engineer to join our team.",
        "required_skills": [
            "Terraform",
            "Networking",
            "GCP"
        ]
    },
    {
        "job_id": "JOB054",
        "title": "Principal Cybersecurity Analyst",
        "company": "Global Solutions",
        "location": "Berlin, DE",
        "work_mode": "Remote",
        "experience": "1-3 years",
        "salary": "$109k - $164k",
        "description": "We are looking for a skilled Principal Cybersecurity Analyst to join our team.",
        "required_skills": [
            "Linux",
            "Wireshark",
            "Bash",
            "Cryptography",
            "Python"
        ]
    },
    {
        "job_id": "JOB055",
        "title": "Full Stack Developer",
        "company": "WebNova",
        "location": "Bangalore, IN",
        "work_mode": "Hybrid",
        "experience": "1-3 years",
        "salary": "$110k - $163k",
        "description": "We are looking for a skilled Full Stack Developer to join our team.",
        "required_skills": [
            "MongoDB",
            "JavaScript",
            "CSS",
            "TypeScript",
            "React",
            "Git",
            "Node.js",
            "HTML",
            "SQL"
        ]
    },
    {
        "job_id": "JOB056",
        "title": "Machine Learning Engineer",
        "company": "E-commerce Giant",
        "location": "Seattle, WA",
        "work_mode": "On-site",
        "experience": "Senior",
        "salary": "$134k - $175k",
        "description": "We are looking for a skilled Machine Learning Engineer to join our team.",
        "required_skills": [
            "Docker",
            "Pandas",
            "Machine Learning",
            "Git"
        ]
    },
    {
        "job_id": "JOB057",
        "title": "Senior Full Stack Developer",
        "company": "Game Studio",
        "location": "Sydney, AU",
        "work_mode": "Hybrid",
        "experience": "5+ years",
        "salary": "$138k - $191k",
        "description": "We are looking for a skilled Senior Full Stack Developer to join our team.",
        "required_skills": [
            "MongoDB",
            "React",
            "HTML",
            "Node.js",
            "TypeScript",
            "SQL",
            "Git",
            "JavaScript",
            "CSS"
        ]
    },
    {
        "job_id": "JOB058",
        "title": "Lead Product Manager",
        "company": "Blockchain Inc",
        "location": "Remote",
        "work_mode": "On-site",
        "experience": "0-2 years",
        "salary": "$67k - $115k",
        "description": "We are looking for a skilled Lead Product Manager to join our team.",
        "required_skills": [
            "Scrum",
            "Agile",
            "Communication",
            "SQL",
            "UI/UX",
            "Jira",
            "Data Analysis"
        ]
    },
    {
        "job_id": "JOB059",
        "title": "Lead AI Engineer",
        "company": "HealthTech",
        "location": "Berlin, DE",
        "work_mode": "Remote",
        "experience": "3-5 years",
        "salary": "$77k - $121k",
        "description": "We are looking for a skilled Lead AI Engineer to join our team.",
        "required_skills": [
            "Machine Learning",
            "TensorFlow",
            "Python",
            "NLP",
            "Mathematics"
        ]
    },
    {
        "job_id": "JOB060",
        "title": "Lead Game Developer",
        "company": "DataWorks",
        "location": "Austin, TX",
        "work_mode": "Remote",
        "experience": "Senior",
        "salary": "$127k - $170k",
        "description": "We are looking for a skilled Lead Game Developer to join our team.",
        "required_skills": [
            "C#",
            "C++",
            "Mathematics",
            "Unreal Engine"
        ]
    },
    {
        "job_id": "JOB061",
        "title": "Senior Product Manager",
        "company": "Global Solutions",
        "location": "San Francisco, CA",
        "work_mode": "On-site",
        "experience": "0-2 years",
        "salary": "$118k - $176k",
        "description": "We are looking for a skilled Senior Product Manager to join our team.",
        "required_skills": [
            "Data Analysis",
            "Communication",
            "Jira",
            "SQL",
            "Agile",
            "Scrum"
        ]
    },
    {
        "job_id": "JOB062",
        "title": "Senior Cybersecurity Analyst",
        "company": "WebNova",
        "location": "Bangalore, IN",
        "work_mode": "On-site",
        "experience": "2-4 years",
        "salary": "$111k - $140k",
        "description": "We are looking for a skilled Senior Cybersecurity Analyst to join our team.",
        "required_skills": [
            "Networking",
            "Python",
            "Linux",
            "Bash"
        ]
    },
    {
        "job_id": "JOB063",
        "title": "DevOps Engineer",
        "company": "Tech Giant",
        "location": "New York, NY",
        "work_mode": "Hybrid",
        "experience": "3-5 years",
        "salary": "$133k - $156k",
        "description": "We are looking for a skilled DevOps Engineer to join our team.",
        "required_skills": [
            "Python",
            "Docker",
            "AWS",
            "CI/CD",
            "Terraform"
        ]
    },
    {
        "job_id": "JOB064",
        "title": "Principal Full Stack Developer",
        "company": "E-commerce Giant",
        "location": "Seattle, WA",
        "work_mode": "On-site",
        "experience": "2-4 years",
        "salary": "$71k - $130k",
        "description": "We are looking for a skilled Principal Full Stack Developer to join our team.",
        "required_skills": [
            "CSS",
            "TypeScript",
            "Node.js",
            "MongoDB"
        ]
    },
    {
        "job_id": "JOB065",
        "title": "Senior Blockchain Developer",
        "company": "CyberSec Corp",
        "location": "Toronto, CA",
        "work_mode": "On-site",
        "experience": "1-3 years",
        "salary": "$115k - $143k",
        "description": "We are looking for a skilled Senior Blockchain Developer to join our team.",
        "required_skills": [
            "Cryptography",
            "Node.js",
            "Blockchain",
            "JavaScript"
        ]
    },
    {
        "job_id": "JOB066",
        "title": "Principal Database Administrator",
        "company": "StartUp Inc",
        "location": "Berlin, DE",
        "work_mode": "Hybrid",
        "experience": "2-4 years",
        "salary": "$65k - $97k",
        "description": "We are looking for a skilled Principal Database Administrator to join our team.",
        "required_skills": [
            "SQL",
            "Oracle",
            "Performance Tuning",
            "Linux",
            "MongoDB",
            "MySQL"
        ]
    },
    {
        "job_id": "JOB067",
        "title": "Lead Full Stack Developer",
        "company": "CyberSec Corp",
        "location": "Seattle, WA",
        "work_mode": "Remote",
        "experience": "2-4 years",
        "salary": "$132k - $184k",
        "description": "We are looking for a skilled Lead Full Stack Developer to join our team.",
        "required_skills": [
            "TypeScript",
            "CSS",
            "React"
        ]
    },
    {
        "job_id": "JOB068",
        "title": "Senior UX/UI Designer",
        "company": "EduTech",
        "location": "Berlin, DE",
        "work_mode": "Hybrid",
        "experience": "Senior",
        "salary": "$89k - $148k",
        "description": "We are looking for a skilled Senior UX/UI Designer to join our team.",
        "required_skills": [
            "Adobe XD",
            "Wireframing",
            "Prototyping",
            "Sketch",
            "CSS"
        ]
    },
    {
        "job_id": "JOB069",
        "title": "Lead QA Engineer",
        "company": "HealthTech",
        "location": "Remote",
        "work_mode": "Remote",
        "experience": "1-3 years",
        "salary": "$93k - $142k",
        "description": "We are looking for a skilled Lead QA Engineer to join our team.",
        "required_skills": [
            "Selenium",
            "Cypress",
            "Jira",
            "Java",
            "Testing",
            "Python"
        ]
    },
    {
        "job_id": "JOB070",
        "title": "Junior Backend Developer",
        "company": "AI Labs",
        "location": "Austin, TX",
        "work_mode": "On-site",
        "experience": "3-5 years",
        "salary": "$140k - $168k",
        "description": "We are looking for a skilled Junior Backend Developer to join our team.",
        "required_skills": [
            "Docker",
            "Node.js",
            "Python",
            "Java",
            "Redis",
            "PostgreSQL",
            "Git"
        ]
    },
    {
        "job_id": "JOB071",
        "title": "Junior AI Engineer",
        "company": "Tech Giant",
        "location": "Seattle, WA",
        "work_mode": "Remote",
        "experience": "0-2 years",
        "salary": "$126k - $170k",
        "description": "We are looking for a skilled Junior AI Engineer to join our team.",
        "required_skills": [
            "Mathematics",
            "NLP",
            "Deep Learning",
            "Python",
            "PyTorch",
            "TensorFlow"
        ]
    },
    {
        "job_id": "JOB072",
        "title": "Principal Backend Developer",
        "company": "Game Studio",
        "location": "London, UK",
        "work_mode": "Remote",
        "experience": "5+ years",
        "salary": "$101k - $122k",
        "description": "We are looking for a skilled Principal Backend Developer to join our team.",
        "required_skills": [
            "Docker",
            "Java",
            "Python",
            "Redis"
        ]
    },
    {
        "job_id": "JOB073",
        "title": "Lead AI Engineer",
        "company": "EduTech",
        "location": "Berlin, DE",
        "work_mode": "On-site",
        "experience": "0-2 years",
        "salary": "$76k - $129k",
        "description": "We are looking for a skilled Lead AI Engineer to join our team.",
        "required_skills": [
            "Machine Learning",
            "Python",
            "PyTorch",
            "Deep Learning"
        ]
    },
    {
        "job_id": "JOB074",
        "title": "Lead Database Administrator",
        "company": "Blockchain Inc",
        "location": "Remote",
        "work_mode": "On-site",
        "experience": "Senior",
        "salary": "$88k - $148k",
        "description": "We are looking for a skilled Lead Database Administrator to join our team.",
        "required_skills": [
            "Performance Tuning",
            "SQL",
            "Oracle"
        ]
    },
    {
        "job_id": "JOB075",
        "title": "Senior DevOps Engineer",
        "company": "HealthTech",
        "location": "Berlin, DE",
        "work_mode": "Hybrid",
        "experience": "0-2 years",
        "salary": "$73k - $103k",
        "description": "We are looking for a skilled Senior DevOps Engineer to join our team.",
        "required_skills": [
            "Python",
            "Kubernetes",
            "CI/CD"
        ]
    },
    {
        "job_id": "JOB076",
        "title": "Senior AI Engineer",
        "company": "WebNova",
        "location": "Bangalore, IN",
        "work_mode": "Hybrid",
        "experience": "1-3 years",
        "salary": "$117k - $143k",
        "description": "We are looking for a skilled Senior AI Engineer to join our team.",
        "required_skills": [
            "PyTorch",
            "TensorFlow",
            "Deep Learning",
            "Mathematics",
            "Machine Learning",
            "NLP",
            "Python"
        ]
    },
    {
        "job_id": "JOB077",
        "title": "Lead Cloud Engineer",
        "company": "Tech Giant",
        "location": "Toronto, CA",
        "work_mode": "On-site",
        "experience": "Senior",
        "salary": "$148k - $183k",
        "description": "We are looking for a skilled Lead Cloud Engineer to join our team.",
        "required_skills": [
            "GCP",
            "Networking",
            "Linux"
        ]
    },
    {
        "job_id": "JOB078",
        "title": "Lead Cybersecurity Analyst",
        "company": "CyberSec Corp",
        "location": "Toronto, CA",
        "work_mode": "Remote",
        "experience": "3-5 years",
        "salary": "$104k - $131k",
        "description": "We are looking for a skilled Lead Cybersecurity Analyst to join our team.",
        "required_skills": [
            "Linux",
            "Networking",
            "Wireshark",
            "Python",
            "Bash",
            "Security"
        ]
    },
    {
        "job_id": "JOB079",
        "title": "Senior Business Analyst",
        "company": "CyberSec Corp",
        "location": "Bangalore, IN",
        "work_mode": "On-site",
        "experience": "5+ years",
        "salary": "$124k - $169k",
        "description": "We are looking for a skilled Senior Business Analyst to join our team.",
        "required_skills": [
            "SQL",
            "Communication",
            "Requirements Gathering",
            "Tableau"
        ]
    },
    {
        "job_id": "JOB080",
        "title": "Junior Mobile Developer",
        "company": "E-commerce Giant",
        "location": "New York, NY",
        "work_mode": "Remote",
        "experience": "Senior",
        "salary": "$142k - $198k",
        "description": "We are looking for a skilled Junior Mobile Developer to join our team.",
        "required_skills": [
            "Git",
            "Java",
            "Swift",
            "Flutter",
            "UI/UX"
        ]
    },
    {
        "job_id": "JOB081",
        "title": "Junior Product Manager",
        "company": "WebNova",
        "location": "London, UK",
        "work_mode": "Hybrid",
        "experience": "Senior",
        "salary": "$145k - $195k",
        "description": "We are looking for a skilled Junior Product Manager to join our team.",
        "required_skills": [
            "Communication",
            "Data Analysis",
            "Agile",
            "Jira"
        ]
    },
    {
        "job_id": "JOB082",
        "title": "Data Scientist",
        "company": "Blockchain Inc",
        "location": "Austin, TX",
        "work_mode": "On-site",
        "experience": "5+ years",
        "salary": "$115k - $148k",
        "description": "We are looking for a skilled Data Scientist to join our team.",
        "required_skills": [
            "Python",
            "SQL",
            "Machine Learning",
            "Statistics",
            "NLP"
        ]
    },
    {
        "job_id": "JOB083",
        "title": "Senior Backend Developer",
        "company": "WebNova",
        "location": "Toronto, CA",
        "work_mode": "Hybrid",
        "experience": "5+ years",
        "salary": "$126k - $178k",
        "description": "We are looking for a skilled Senior Backend Developer to join our team.",
        "required_skills": [
            "Git",
            "PostgreSQL",
            "AWS",
            "Docker",
            "Redis",
            "Node.js",
            "Java",
            "Python"
        ]
    },
    {
        "job_id": "JOB084",
        "title": "Lead Cloud Engineer",
        "company": "DataWorks",
        "location": "Toronto, CA",
        "work_mode": "Remote",
        "experience": "1-3 years",
        "salary": "$107k - $149k",
        "description": "We are looking for a skilled Lead Cloud Engineer to join our team.",
        "required_skills": [
            "Python",
            "AWS",
            "Linux",
            "GCP",
            "Networking"
        ]
    },
    {
        "job_id": "JOB085",
        "title": "Principal Mobile Developer",
        "company": "Game Studio",
        "location": "Seattle, WA",
        "work_mode": "On-site",
        "experience": "1-3 years",
        "salary": "$69k - $96k",
        "description": "We are looking for a skilled Principal Mobile Developer to join our team.",
        "required_skills": [
            "Flutter",
            "UI/UX",
            "Git",
            "Java",
            "Kotlin"
        ]
    },
    {
        "job_id": "JOB086",
        "title": "Principal DevOps Engineer",
        "company": "EduTech",
        "location": "Sydney, AU",
        "work_mode": "Hybrid",
        "experience": "3-5 years",
        "salary": "$137k - $163k",
        "description": "We are looking for a skilled Principal DevOps Engineer to join our team.",
        "required_skills": [
            "Linux",
            "Kubernetes",
            "CI/CD",
            "Docker",
            "Python"
        ]
    },
    {
        "job_id": "JOB087",
        "title": "Senior System Administrator",
        "company": "CyberSec Corp",
        "location": "Seattle, WA",
        "work_mode": "On-site",
        "experience": "Senior",
        "salary": "$80k - $121k",
        "description": "We are looking for a skilled Senior System Administrator to join our team.",
        "required_skills": [
            "Networking",
            "Linux",
            "PowerShell",
            "Windows Server"
        ]
    },
    {
        "job_id": "JOB088",
        "title": "Principal Mobile Developer",
        "company": "WebNova",
        "location": "Austin, TX",
        "work_mode": "Hybrid",
        "experience": "3-5 years",
        "salary": "$137k - $162k",
        "description": "We are looking for a skilled Principal Mobile Developer to join our team.",
        "required_skills": [
            "Swift",
            "Java",
            "UI/UX",
            "Flutter",
            "React Native",
            "Git"
        ]
    },
    {
        "job_id": "JOB089",
        "title": "Principal Product Manager",
        "company": "AI Labs",
        "location": "Austin, TX",
        "work_mode": "On-site",
        "experience": "5+ years",
        "salary": "$88k - $108k",
        "description": "We are looking for a skilled Principal Product Manager to join our team.",
        "required_skills": [
            "Communication",
            "Jira",
            "UI/UX",
            "Agile",
            "Scrum",
            "Data Analysis",
            "SQL"
        ]
    },
    {
        "job_id": "JOB090",
        "title": "Senior Cybersecurity Analyst",
        "company": "FinTech Co",
        "location": "Bangalore, IN",
        "work_mode": "On-site",
        "experience": "1-3 years",
        "salary": "$127k - $163k",
        "description": "We are looking for a skilled Senior Cybersecurity Analyst to join our team.",
        "required_skills": [
            "Python",
            "Wireshark",
            "Linux",
            "Networking"
        ]
    },
    {
        "job_id": "JOB091",
        "title": "Junior AI Engineer",
        "company": "DataWorks",
        "location": "Remote",
        "work_mode": "Hybrid",
        "experience": "Senior",
        "salary": "$108k - $166k",
        "description": "We are looking for a skilled Junior AI Engineer to join our team.",
        "required_skills": [
            "Python",
            "Deep Learning",
            "Mathematics",
            "TensorFlow",
            "PyTorch"
        ]
    },
    {
        "job_id": "JOB092",
        "title": "Lead UX/UI Designer",
        "company": "Game Studio",
        "location": "Bangalore, IN",
        "work_mode": "On-site",
        "experience": "1-3 years",
        "salary": "$70k - $112k",
        "description": "We are looking for a skilled Lead UX/UI Designer to join our team.",
        "required_skills": [
            "HTML",
            "Adobe XD",
            "CSS"
        ]
    },
    {
        "job_id": "JOB093",
        "title": "Lead Full Stack Developer",
        "company": "Global Solutions",
        "location": "London, UK",
        "work_mode": "Hybrid",
        "experience": "1-3 years",
        "salary": "$96k - $116k",
        "description": "We are looking for a skilled Lead Full Stack Developer to join our team.",
        "required_skills": [
            "React",
            "Git",
            "TypeScript",
            "HTML",
            "CSS",
            "SQL",
            "Node.js"
        ]
    },
    {
        "job_id": "JOB094",
        "title": "Junior Cybersecurity Analyst",
        "company": "Global Solutions",
        "location": "Toronto, CA",
        "work_mode": "Remote",
        "experience": "2-4 years",
        "salary": "$80k - $136k",
        "description": "We are looking for a skilled Junior Cybersecurity Analyst to join our team.",
        "required_skills": [
            "Networking",
            "Wireshark",
            "Python",
            "Linux",
            "Cryptography",
            "Bash"
        ]
    },
    {
        "job_id": "JOB095",
        "title": "Junior Full Stack Developer",
        "company": "Tech Giant",
        "location": "Seattle, WA",
        "work_mode": "Remote",
        "experience": "1-3 years",
        "salary": "$122k - $155k",
        "description": "We are looking for a skilled Junior Full Stack Developer to join our team.",
        "required_skills": [
            "Node.js",
            "Git",
            "HTML",
            "React",
            "SQL",
            "JavaScript",
            "TypeScript"
        ]
    },
    {
        "job_id": "JOB096",
        "title": "Lead AI Engineer",
        "company": "AI Labs",
        "location": "Remote",
        "work_mode": "On-site",
        "experience": "3-5 years",
        "salary": "$98k - $142k",
        "description": "We are looking for a skilled Lead AI Engineer to join our team.",
        "required_skills": [
            "Deep Learning",
            "Mathematics",
            "NLP",
            "Python",
            "PyTorch",
            "Machine Learning",
            "TensorFlow"
        ]
    },
    {
        "job_id": "JOB097",
        "title": "Backend Developer",
        "company": "Cloud Systems",
        "location": "Remote",
        "work_mode": "On-site",
        "experience": "1-3 years",
        "salary": "$101k - $132k",
        "description": "We are looking for a skilled Backend Developer to join our team.",
        "required_skills": [
            "Redis",
            "PostgreSQL",
            "Java",
            "Git",
            "Docker"
        ]
    },
    {
        "job_id": "JOB098",
        "title": "Lead Data Scientist",
        "company": "AI Labs",
        "location": "Remote",
        "work_mode": "Hybrid",
        "experience": "0-2 years",
        "salary": "$83k - $114k",
        "description": "We are looking for a skilled Lead Data Scientist to join our team.",
        "required_skills": [
            "NumPy",
            "Pandas",
            "NLP",
            "Statistics",
            "Machine Learning",
            "Python",
            "Deep Learning"
        ]
    },
    {
        "job_id": "JOB099",
        "title": "Backend Developer",
        "company": "Blockchain Inc",
        "location": "New York, NY",
        "work_mode": "On-site",
        "experience": "3-5 years",
        "salary": "$88k - $118k",
        "description": "We are looking for a skilled Backend Developer to join our team.",
        "required_skills": [
            "Redis",
            "Python",
            "Docker",
            "AWS",
            "Git",
            "SQL",
            "Node.js",
            "PostgreSQL",
            "Java"
        ]
    },
    {
        "job_id": "JOB100",
        "title": "Principal QA Engineer",
        "company": "Blockchain Inc",
        "location": "London, UK",
        "work_mode": "On-site",
        "experience": "3-5 years",
        "salary": "$83k - $124k",
        "description": "We are looking for a skilled Principal QA Engineer to join our team.",
        "required_skills": [
            "Java",
            "Cypress",
            "Selenium",
            "Testing"
        ]
    }
]


def seed_database(return_jobs=False, return_roles=False):
    try:
        db = get_db()
        if db.roles.count_documents({}) == 0:
            db.roles.insert_many(ROLES)
        if db.jobs.count_documents({}) == 0:
            db.jobs.insert_many(JOBS)
        
        if return_roles:
            return list(db.roles.find({}, {"_id": 0}))
        if return_jobs:
            return list(db.jobs.find({}, {"_id": 0}))
    except Exception:
        pass
    
    if return_roles:
        return ROLES
    return JOBS
