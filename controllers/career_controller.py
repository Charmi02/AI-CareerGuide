
from models.career_model import recommend_careers
from models.skill_gap import analyze_skill_gap


def analyze_career_profile(skills, interests):

    if not skills.strip() or not interests.strip():
        raise ValueError("Skills and interests are required.")

    recommendations = recommend_careers(
        skills,
        interests
    )

    if not recommendations:
        return {
            "recommendations": [],
            "target_career": None,
            "existing_skills": [],
            "missing_skills": [],
            "roadmap": []
        }

    target_career = recommendations[0]["career"]

    existing, missing = analyze_skill_gap(
        target_career,
        skills
    )

    return {
        "recommendations": recommendations,
        "target_career": target_career,
        "existing_skills": existing,
        "missing_skills": missing,
        "roadmap": missing
    }
