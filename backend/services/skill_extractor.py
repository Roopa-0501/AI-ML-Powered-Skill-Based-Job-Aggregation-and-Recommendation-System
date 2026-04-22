import re

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

SOFT = [
"communication","teamwork","leadership","problem solving"
]

ALL_SKILLS = TECH + TEACHING + BUSINESS + HEALTH + SOFT

def extract_skills(text):
    text = text.lower()
    found = []


    for skill in ALL_SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", text):
            found.append(skill)

    return list(set(found))

