
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_job(user_skills, job_description):

    documents = [user_skills, job_description]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    score = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    return round(float(score) * 100, 1)
