# 🚀 SkillWeave – AI & ML Powered Job Recommendation System

## 📌 Overview

SkillWeave is an AI-powered job recommendation system that helps users discover relevant career opportunities based on their skills. Instead of relying on traditional keyword searches, the system analyzes resumes using NLP techniques and recommends jobs through intelligent skill matching.

---

## 🎯 Features

* 📄 Upload resume (PDF format)
* 🧠 Extract skills using NLP
* 🤖 AI-based job matching using TF-IDF & Cosine Similarity
* 🌐 Fetch real-time jobs from APIs
* 📊 Rank and display relevant job recommendations
* ⚡ Fast and responsive UI using React + Vite

---

## 🏗️ Tech Stack

### 🔹 Backend

* Python
* Flask (REST API)

### 🔹 AI / ML

* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity
* NLP Parsing

### 🔹 Frontend

* React (Vite)
* HTML5
* CSS3

### 🔹 Job APIs

* Adzuna
* The Muse
* Arbeitnow

### 🔹 Data Processing

* JSON
* PyPDF2

### 🔹 Tools

* GitHub
* VS Code

---

## ⚙️ How It Works

1. User uploads resume via frontend
2. Resume is sent to Flask backend
3. PyPDF2 extracts text from PDF
4. NLP processes and extracts skills
5. Job data fetched from external APIs
6. TF-IDF converts text into vectors
7. Cosine similarity computes matching scores
8. Jobs are ranked and returned to frontend
9. UI displays recommended jobs

---

## 📁 Project Structure

```
SkillWeave/
│
├── backend/
│   ├── app.py
│   ├── utils/
│   ├── model/
│
├── frontend/
│   ├── index.html
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   └── styles/
│
├── README.md
└── requirements.txt
```

---

## 🚀 Installation & Setup

### 🔹 Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## 📸 Screenshots

* Resume Upload Page
* Processing / Loading Screen
* Job Recommendation Results

---

## ⚠️ Limitations

* Uses TF-IDF (basic NLP, not semantic understanding)
* Similarity scores may appear low but ranking is accurate
* Depends on external job APIs

---

## 🔮 Future Enhancements

* Add user login & profile tracking
* Implement semantic models (BERT)
* Improve skill extraction using advanced NLP
* Add job alerts and notifications
* Implement caching for faster API response
---

## 💡 Conclusion

SkillWeave demonstrates how AI and Machine Learning can be integrated with full-stack development to build a smart job recommendation system that improves job discovery efficiency.

---


* G. Roopa
