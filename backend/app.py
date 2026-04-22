from flask import Flask, request, jsonify
from flask_cors import CORS

from services.resume_parser import pdf_to_text
from services.skill_extractor import extract_skills
from services.predictor import predict_category
# from services.domain_filter import detect_domain, filter_jobs_by_domain
from services.job_service import get_jobs
from matching.ranker import rank_jobs

def build_query(skills, category):

    if not skills:
        return category.lower()

    # remove useless skills
    ignore = [
        "communication", "teamwork", "leadership",
        "management", "problem solving", "education"
    ]

    filtered = [s for s in skills if s.lower() not in ignore]

    if not filtered:
        filtered = skills

    # important skills priority
    priority = [
        "python","java","machine learning","nlp",
        "flask","django","sql","react"
    ]

    sorted_skills = sorted(
        filtered,
        key=lambda x: x in priority,
        reverse=True
    )

    query_skills = sorted_skills[:3]

    return " ".join(query_skills) + " jobs"

def infer_role_from_skills(skills):

    skills = [s.lower() for s in skills]

    tech = sum(s in skills for s in [
        "python","java","flask","django","sql","mysql",
        "machine learning","nlp"
    ])

    teaching = sum(s in skills for s in [
        "teaching","curriculum","classroom"
    ])

    business = sum(s in skills for s in [
        "marketing","sales","finance","accounting"
    ])

    health = sum(s in skills for s in [
        "nursing","clinical","medical"
    ])

    domain = max({
        "IT": tech,
        "TEACHING": teaching,
        "BUSINESS": business,
        "HEALTH": health
    }, key=lambda x: {
        "IT": tech,
        "TEACHING": teaching,
        "BUSINESS": business,
        "HEALTH": health
    }[x])

    if domain == "IT":
        if sum(s in skills for s in ["flask","django","mysql","sql"]) >= 2:
            return "Backend Developer"
        if sum(s in skills for s in ["machine learning","nlp"]) >= 2:
            return "Data Scientist"
        return "Software Engineer"

    if domain == "TEACHING":
        return "Teacher"

    if domain == "BUSINESS":
        return "Business Analyst"

    if domain == "HEALTH":
        return "Healthcare Professional"

    return "Professional"

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "SkillWeave Backend Running ✅"

@app.route("/predict", methods=["POST"])
def predict():


    file = request.files["resume"]

    text = pdf_to_text(file)

    skills = extract_skills(text)

    skills = [s for s in skills if s not in [
        "communication","teamwork","leadership",
        "management","problem solving","education"
    ]]

    category = predict_category(text)
    role = infer_role_from_skills(skills)

    # domain = detect_domain(skills)

    query = " ".join(skills[:2])

    jobs = get_jobs(query)

    # jobs = filter_jobs_by_domain(jobs, domain)

    ranked_jobs = rank_jobs(skills, jobs)

    return jsonify({
        "category": category,
        "role": role,
        "skills": skills,
        "jobs": ranked_jobs
    })

if __name__ == "__main__":
    app.run(debug=True)
