
from models.job_match import match_job


def analyze_job_match(skills, job_description):

    if not skills.strip():
        raise ValueError("Please enter your skills.")

    if not job_description.strip():
        raise ValueError("Please enter a job description.")

    score = match_job(
        skills,
        job_description
    )

    return {
        "similarity_score": score
    }
