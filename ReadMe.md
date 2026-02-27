
# 🧠 HABITSCOPE
## Machine Learning Driven Behavioral Analytics Platform

HABITSCOPE is an end-to-end behavioral analytics system that evaluates daily student activity patterns and transforms them into structured productivity intelligence using machine learning and explainable analytics.

It combines natural language processing, supervised learning, optimized deployment engineering, and full-stack integration to deliver measurable behavioral insights in a scalable cloud-based architecture.

---

## 🚀 Live System

Frontend: https://amarjithanand.github.io/student-productivity-tracker/Frontend

Backend API: https://student-productivity-backend.onrender.com/predict

---

## 📌 Problem Context

Modern students face productivity challenges due to:

- Digital distractions  
- Irregular sleep cycles  
- High stress levels  
- Poor time allocation  

Most productivity tools:
- Provide raw tracking  
- Lack behavioral modeling  
- Do not quantify performance  

HABITSCOPE solves this by transforming behavioral signals into measurable productivity intelligence using machine learning.

---

## 🎯 Core Capabilities

- Predict continuous productivity score  
- Classify daily performance (Productive / Neutral / Distracted)  
- Extract structured features from natural language input  
- Generate explainable behavioral insights  
- Visualize trend progression  
- Deploy full-stack ML system in cloud environment  

---

## 📊 Dataset Overview

Source: Kaggle – Student Productivity & Digital Distraction Dataset  
Records: 20,000  
Features: 18  

Key Inputs:

- Study hours  
- Sleep hours  
- Phone usage  
- Social media usage  
- Gaming hours  
- Stress level  
- Focus score  
- Attendance percentage  
- Exercise minutes  
- Coffee intake  
- Assignments completed  
- Final grade  

Target: Productivity Score  

---

## ⚙️ Methodology

### 1. Data Preprocessing

- Missing value handling  
- Feature scaling using StandardScaler  
- Train-test split (80/20)  
- Feature-target separation  
- Outlier analysis  

---

### 2. Model Development

#### 🔹 Regression Model
Algorithm: Ridge Regression  
Purpose: Predict continuous productivity score  
Reason: Regularized, lightweight, deployment-efficient  

#### 🔹 Classification Model
Algorithm: Logistic Regression  
Purpose: Classify productivity category  

---

### 3. Model Optimization

Initial approach used RandomForest (~300MB model size).

Issues:
- Memory crashes on cloud deployment  
- Slow cold starts  
- Free-tier limitations  

Optimized solution:
- Replaced with linear models  
- Reduced total model size to ~2MB  
- Maintained strong predictive stability  
- Achieved efficient cloud inference  

---

## 📈 Model Evaluation

### Regression Performance

| Metric | Value |
|--------|-------|
| R² Score | NaN |
| MSE | NaN |
| MAE | NaN |

### Classification Performance

| Metric | Value |
|--------|-------|
| Accuracy | NaN |
| Precision | NaN |
| Recall | NaN |
| F1 Score | NaN |

---

## 🔍 Key Observations

- Study hours strongly correlate with productivity score  
- Excessive phone usage negatively impacts classification outcome  
- Balanced sleep improves model confidence  
- High stress frequently maps to distracted classification  
- Behavioral balance yields highest productivity consistency  

---

## 🏗️ System Architecture

User Input (Diary Text)  
        ↓  
Cohere API (NLP Feature Extraction)  
        ↓  
Structured Feature JSON  
        ↓  
FastAPI Backend (Render)  
        ↓  
ML Model Inference  
        ↓  
Rule-Based Explainability Layer  
        ↓  
Frontend Visualization (Chart.js)  

---

## 🌐 Technology Stack

Frontend:
- HTML  
- Tailwind CSS  
- Chart.js  

Backend:
- FastAPI  
- Uvicorn  
- Scikit-learn  
- Joblib  

ML:
- Ridge Regression  
- Logistic Regression  
- StandardScaler  

Deployment:
- Render (Backend)  
- GitHub Pages (Frontend)  
- Hugging Face (Model Hosting)  

NLP:
- Cohere API  

---

## 🧠 Explainability Strategy

Instead of relying on secondary LLM summaries:

- Implemented deterministic rule-based explanation layer  
- Used feature thresholds for insight generation  
- Eliminated latency and rate-limit dependency  
- Ensured fast and stable inference  

---

## 🚧 Engineering Challenges Solved

- Model memory optimization  
- Cloud free-tier constraints  
- API rate limits (429 errors)  
- CORS policy conflicts  
- Cold-start latency  
- Secure API key handling  

---

## 🛠️ Local Setup Guide

### Clone Repository

git clone https://github.com/amarjithanand/student-productivity-tracker.git  
cd student-productivity-tracker

---

### Backend Setup

cd Backend  
python -m venv venv  
venv\Scripts\activate  (Windows)  
pip install -r requirements.txt  
uvicorn app:app --reload  

Backend runs at:  
http://127.0.0.1:8000  

---

### Frontend Setup

cd ../Frontend  
python -m http.server 5500  

Open:  
http://localhost:5500  

Ensure API_URL points to local backend during development.

---

## 📁 Project Structure

student-productivity-tracker/  
│  
├── Backend/  
│   ├── app.py  
│   ├── requirements.txt  
│   ├── pkl_models/  
│  
├── Frontend/  
│   ├── index.html  
│  
└── README.md  

---

## 🔮 Future Enhancements

- SHAP-based explainability  
- Feature importance visualization  
- Persistent database integration  
- User authentication  
- Time-series modeling  
- Model ensemble comparison  
- A/B performance experimentation  

---

## 👤 Author

Amarjith Anand 
MCA Student | Entry Level Data Scientist  

---

## 🏆 Project Highlights

- Full-stack ML deployment  
- Model size optimization from 300MB → 2MB  
- Cloud-ready inference pipeline  
- NLP + ML integration  
- Explainable AI layer  
- Production-aware system design  

HABITSCOPE demonstrates applied machine learning engineering beyond notebook experimentation by integrating modeling, optimization, deployment, and interpretability within a cohesive behavioral analytics platform.
