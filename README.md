# Online Course Completion Prediction

End-to-end Machine Learning project using:
- Scikit-learn
- FastAPI
- Docker
- AWS ECR & ECS

## Project Overview
Predicts whether a student will complete an online course based on activity and device usage.

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI
- Docker
- AWS (ECR, ECS)

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
