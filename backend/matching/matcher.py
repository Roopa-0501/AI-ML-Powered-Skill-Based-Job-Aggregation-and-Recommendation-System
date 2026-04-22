import re

def match_skills(resume_skills, job):
    text = (job["title"] + " " + job["description"]).lower()
    matched = []

    for skill in resume_skills:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            matched.append(skill)

    return matched

