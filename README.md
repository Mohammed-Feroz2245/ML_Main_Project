# Online-Course-Completion-Prediction-using-Machine-Learning

Machine Learning + FastAPI project to predict whether a student will complete an online course based on engagement and activity data.

Problem Statement

Online learning platforms often face high dropout rates.
Identifying students who are unlikely to complete a course helps platforms improve engagement, provide support, and reduce dropouts.

This project predicts whether a student will complete or not complete an online course using behavioral and usage data.

Dataset

Source: Online course engagement dataset

Number of Features: Multiple student engagement and activity features

Target Variable: completed_course

1 → Completed

0 → Not Completed

Data Preparation Steps

Removed duplicate records

Dropped irrelevant columns (height, weight, pets, etc.)

Removed missing values (~5% of data)

Applied One-Hot Encoding on categorical features (preferred_device)

Model

Algorithm Used: Random Forest Classifier

Why Random Forest?

Handles non-linear relationships well

Robust to overfitting

Performs well without heavy feature scaling

Evaluation Metric: Accuracy Score

Train/Test Split: 80% training, 20% testing

API Endpoint (FastAPI)

The trained model is exposed as a REST API using FastAPI.

Endpoint
POST /predict

Input

Student engagement features in JSON format.

Output
Completed / Not Completed


The API takes student input data, sends it to the trained model, and returns the prediction.

How to Run Locally

1️⃣ Install dependencies

pip install -r requirements.txt


2️⃣ Start FastAPI server

uvicorn main:app --reload


3️⃣ Open API documentation

http://127.0.0.1:8000/docs

Results & Learnings
What Worked Well

Built a complete end-to-end ML pipeline

Implemented Object-Oriented Programming for model inference

Deployed the model using FastAPI

Dockerized the application for deployment

Pushed and deployed the container using AWS (ECR & ECS)
