
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

CAREERS = {
    "IT Support Specialist": "troubleshooting windows networking customer support hardware communication",
    "Cloud Engineer": "AWS Azure Linux networking cloud computing terraform python",
    "Data Analyst": "Python SQL Excel Power BI statistics data visualization",
    "Software Developer": "Python Java JavaScript programming APIs SQL problem solving",
    "DevOps Engineer": "Linux Docker Kubernetes AWS Git CI CD Terraform Python",
    "Cybersecurity Analyst": "networking Linux security risk analysis Python firewalls"
}

def recommend_careers(skills, interests):
    profile = skills + " " + interests
    names = list(CAREERS.keys())
    descriptions = list(CAREERS.values())

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([profile] + descriptions)

    scores = cosine_similarity(vectors[0:1], vectors[1:])[0]

    results = []

    for i in range(len(names)):
        results.append({
            "career": names[i],
            "score": round(float(scores[i]) * 100, 1)
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:3]
