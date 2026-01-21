Course Completion ML System

An end-to-end MLOps-oriented machine learning system that predicts whether a student will complete an online course, including training, deployment, automation, and retraining.

Project Overview

Online learning platforms face high dropout rates, making it difficult to identify students who may disengage early.
This project addresses the problem by building a production-ready ML system that predicts course completion using student engagement and activity data.

The system is designed following MLOps principles, covering:

Modular ML pipelines

API-based inference

Cloud deployment

Automated retraining

Architecture Diagram (Textual)
                ┌──────────────┐
                │   Dataset    │
                │ (CSV Upload) │
                └──────┬───────┘
                       │
               Upload to AWS S3
                       │
        ┌──────────────▼──────────────┐
        │        AWS Lambda            │
        │  (Model Retraining Trigger)  │
        └──────────────┬──────────────┘
                       │
              Trained Model Stored
                       │
                  AWS S3 Bucket
                       │
        ┌──────────────▼──────────────┐
        │        FastAPI Service       │
        │   (Inference REST API)       │
        └──────────────┬──────────────┘
                       │
              Docker Container
                       │
                AWS ECR → ECS

Tech Stack

Machine Learning

Python

Scikit-learn (Random Forest)

API & Backend

FastAPI

Pydantic

Swagger UI

MLOps & Cloud

Docker

AWS S3 (data & model storage)

AWS Lambda (automated retraining)

AWS ECR & ECS (container registry & deployment)

Development

Git & GitHub

Object-Oriented Programming (OOP)

How to Run API Locally
Option 1: Using Docker (Recommended)
docker build -t course-completion-ml .
docker run -p 8000:8000 course-completion-ml


Open Swagger UI:

http://127.0.0.1:8000/docs

Option 2: Without Docker
pip install -r requirements.txt
uvicorn main:app --reload

API Endpoint

POST /predict

Input:
Student engagement features in JSON format

Output:

Completed

Not Completed

How Retraining Works (S3 → Lambda)

New dataset is uploaded to AWS S3

S3 event triggers AWS Lambda

Lambda:

Loads new data

Retrains the ML model

Evaluates performance

Saves updated model back to S3

FastAPI service loads the latest model for inference

This enables automated, event-driven model retraining, aligning with MLOps best practices.

CI/CD Pipeline Overview

Code pushed to GitHub

Docker image built locally or via pipeline

Image pushed to AWS ECR

Deployed to AWS ECS

FastAPI service updated with minimal downtime

(CI/CD concepts implemented with focus on automation and reproducibility)

Key Learnings

Designing production-ready ML systems

Deploying ML models as scalable APIs

Containerization and cloud deployment

Event-driven retraining pipelines

Applying MLOps principles to real-world ML problems
