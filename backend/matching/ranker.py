from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# 🔹 Domain skill sets

TECH = [
"python","java","c++","javascript","html","css",
"sql","mysql","mongodb",
"machine learning","deep learning","nlp",
"django","flask","react","node",
"aws","docker","kubernetes","git"
]

TEACHING = [
"teaching","education","curriculum","lesson planning",
"classroom","pedagogy"
]

BUSINESS = [
"finance","accounting","marketing","sales","management"
]

HEALTH = [
"nursing","patient care","clinical","medical"
]

# 🔹 Detect domain from resume skills

def detect_domain(skills):


    scores = {
        "IT": sum(1 for s in skills if s in TECH),
        "TEACHING": sum(1 for s in skills if s in TEACHING),
        "BUSINESS": sum(1 for s in skills if s in BUSINESS),
        "HEALTH": sum(1 for s in skills if s in HEALTH)
    }

    return max(scores, key=scores.get)


# 🔹 Filter skills based on detected domain

def filter_skills_by_domain(skills, domain):


    if domain == "IT":
        return [s for s in skills if s in TECH]

    elif domain == "TEACHING":
        return [s for s in skills if s in TEACHING]

    elif domain == "BUSINESS":
        return [s for s in skills if s in BUSINESS]

    elif domain == "HEALTH":
        return [s for s in skills if s in HEALTH]

    return skills


# 🔹 Filter jobs based on domain

def is_relevant_job(job, domain):


    text = (job.get("title","") + job.get("description","")).lower()

    if domain == "IT":
        return any(k in text for k in ["developer","engineer","software","data","ml"])

    elif domain == "TEACHING":
        return any(k in text for k in ["teacher","school","education"])

    elif domain == "BUSINESS":
        return any(k in text for k in ["manager","marketing","sales"])

    elif domain == "HEALTH":
        return any(k in text for k in ["nurse","doctor","clinical"])

    return True


# 🔹 Extract job skills from description

# def extract_job_skills(description, skill_list):


#     description = description.lower()
#     job_skills = []

#     for skill in skill_list:
#         pattern = r"\b" + re.escape(skill) + r"\b"

#         if re.search(pattern, description):
#             job_skills.append(skill)

#     return job_skills


def extract_focus_text(text):
    text = text.lower()

    # remove symbols but keep words
    cleaned = re.sub(r"[^a-zA-Z0-9 ]", " ", text)

    # KEEP MORE CONTEXT (not only keywords)
    words = cleaned.split()

    # take first 100 words + important keywords
    important_part = " ".join(words[:100])

    return important_part


# 🔹 Main ranking function

def rank_jobs(resume_skills, jobs):

    if not resume_skills or not jobs:
        return []

    domain = detect_domain(resume_skills)

    resume_skills = filter_skills_by_domain(resume_skills, domain)

    if not resume_skills:
        return []

    resume_text = " ".join(resume_skills) * 3

    job_texts = []
    valid_jobs = []

    for job in jobs:

        if not is_relevant_job(job, domain):
            continue

        full_text = job.get("description", "").lower()

        # keep important part + context
        focus = extract_focus_text(full_text)

        # combine both (VERY IMPORTANT)
        text = focus + " " + full_text[:200]

        if not text.strip():
            continue

        job_texts.append(text)
        valid_jobs.append(job)

    if not valid_jobs:
        return []

    corpus = [resume_text] + job_texts

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    resume_vec = tfidf_matrix[0]
    job_vecs = tfidf_matrix[1:]

    scores = cosine_similarity(resume_vec, job_vecs)[0]

    results = []

    for i, job in enumerate(valid_jobs):

        score = float(scores[i]) * 100

        matched = [
            s for s in resume_skills
            if re.search(r"\b" + re.escape(s) + r"\b", job_texts[i])
        ]

        if score >= 10:
            results.append({
                "title": job.get("title", ""),
                "company": job.get("company", ""),
                "location": job.get("location", "Not specified"),
                "match_percentage": round(score, 2),
                "matched_skills": matched,
                "url": job.get("url")
            })

    return sorted(results, key=lambda x: x["match_percentage"], reverse=True)[:25]

