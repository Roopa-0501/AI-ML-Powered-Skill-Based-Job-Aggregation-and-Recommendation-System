import pickle
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 🔹 Load models correctly

cat_model = pickle.load(open(os.path.join(BASE_DIR, "models/rf_classifier_categorization.pkl"), "rb"))
tfidf_cat = pickle.load(open(os.path.join(BASE_DIR, "models/tfidf_vectorizer_categorization.pkl"), "rb"))

role_model = pickle.load(open(os.path.join(BASE_DIR, "models/rf_classifier_job_recommendation.pkl"), "rb"))
tfidf_role = pickle.load(open(os.path.join(BASE_DIR, "models/tfidf_vectorizer_job_recommendation.pkl"), "rb"))

def clean(text):
    text = re.sub(r"http\S+|@\S+|#\S+", " ", text)
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    return re.sub(r"\s+", " ", text)

def predict_category(text):
    text = clean(text)
    vec = tfidf_cat.transform([text])
    return cat_model.predict(vec)[0]

def predict_role(text):
    text = clean(text)
    vec = tfidf_role.transform([text])
    return role_model.predict(vec)[0]
