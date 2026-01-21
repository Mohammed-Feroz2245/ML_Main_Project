## Course Completion ML System

An end-to-end **MLOps-oriented machine learning system** that predicts whether a student will complete an online course based on engagement and activity data.

The project demonstrates the complete ML lifecycle, including **training, deployment, automation, and retraining**, following production-style practices.

---

## Project Overview

Online learning platforms often face high dropout rates.  
This system helps identify students who are likely to drop out, enabling platforms to take proactive actions such as personalized support and engagement strategies.

The focus of this project is not only model accuracy, but also **deployability, automation, and maintainability**, aligning with real-world MLOps workflows.

---

## Architecture (High-Level)


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


---

## Tech Stack

- **Programming & ML:** Python, Scikit-learn  
- **API & Backend:** FastAPI, Pydantic, Swagger UI  
- **MLOps & Cloud:** Docker, AWS S3, Lambda, ECR, ECS  
- **Development:** Git, GitHub, Object-Oriented Programming (OOP)

---

## Key Features

- End-to-end ML pipeline (data preprocessing → training → evaluation)
- Modular and scalable code structure using OOP
- Model deployment as a REST API using FastAPI
- Input validation using Pydantic
- Containerized deployment using Docker
- Cloud deployment on AWS ECS
- Event-driven model retraining using S3 and Lambda

---

## How to Run the API Locally

### Using Docker (Recommended)


docker build -t course-completion-ml .
docker run -p 8000:8000 course-completion-ml

#Open API documentation:
http://127.0.0.1:8000/docs

#Without Docker:
pip install -r requirements.txt
uvicorn main:app --reload

---

#API Endpoint

POST /predict

Input:
Student engagement features in JSON format

Output:

-Completed

-Not Completed

---

Automated Retraining (S3 → Lambda)

New datasets uploaded to AWS S3 trigger an AWS Lambda function

Lambda retrains the model and stores the updated version back to S3

The FastAPI service loads the latest model for inference

---

#CI/CD Overview

Code versioned using GitHub

Docker images built and pushed to AWS ECR

Services deployed to AWS ECS

Focus on automation, reproducibility, and scalability

---

#Key Learnings

Building production-ready ML systems

Deploying ML models as scalable APIs

Containerization and cloud deployment

Event-driven model retraining

Applying MLOps best practices in practice


