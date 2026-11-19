
CAREER_SKILLS = {
    "Cloud Engineer": [
        "AWS",
        "Azure",
        "Linux",
        "Networking",
        "Terraform",
        "Python",
        "Docker"
    ],
    "DevOps Engineer": [
        "Linux",
        "Docker",
        "Kubernetes",
        "AWS",
        "Git",
        "Terraform",
        "Python"
    ],
    "Cybersecurity Analyst": [
        "Networking",
        "Linux",
        "Security",
        "Python",
        "Firewalls",
        "Risk Analysis"
    ],
    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Statistics"
    ],
    "Software Developer": [
        "Python",
        "Java",
        "JavaScript",
        "SQL",
        "APIs"
    ],
    "IT Support Specialist": [
        "Windows",
        "Networking",
        "Troubleshooting",
        "Hardware",
        "Customer Support"
    ]
}


def analyze_skill_gap(career, user_skills):

    required = CAREER_SKILLS.get(career, [])

    user_skills = [
        skill.strip().lower()
        for skill in user_skills.split(",")
    ]

    existing = []
    missing = []

    for skill in required:
        if skill.lower() in user_skills:
            existing.append(skill)
        else:
            missing.append(skill)

    return existing, missing
