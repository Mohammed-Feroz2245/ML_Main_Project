# Online Course Completion Prediction (ML + FastAPI + Docker + AWS)

## 📌 Project Overview
This project predicts whether a student will complete an online course based on engagement and behavioral features.
It includes data preprocessing, machine learning model training, and a REST API for inference.

---

## 🧠 Machine Learning Pipeline
- Data cleaning and preprocessing
- One-hot encoding of categorical features
- Train/test split
- Random Forest Classifier
- Model serialization using Pickle

---

## 🗂 Project Structure
ML_Main_Project/
│
├── data/
│   └── online_course_completion.csv
│
├── artifacts/
│   └── model.pkl
│
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── train.py
│   └── model_class.py
│
├── api/
│   └── main.py
│
├── Dockerfile
├── requirements.txt
├── .gitignore
├── README.md
└── run_training.py
