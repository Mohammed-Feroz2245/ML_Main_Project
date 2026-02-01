# Course Completion ML System

An end-to-end **MLOps-oriented machine learning system** that predicts whether a student will complete an online course based on engagement and activity data.

This project demonstrates the complete ML lifecycle, including **data preprocessing, model training, evaluation, deployment, automation, and retraining**, following production-style practices.

---

## Project Overview

Online learning platforms often face high dropout rates.  
This system identifies students who are likely to drop out, enabling proactive interventions such as personalized support and engagement strategies.

The focus is not only on model accuracy but also on **deployability, automation, maintainability, and reproducibility**, reflecting real-world MLOps workflows.

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
    │        AWS Lambda           │
    │  (Model Retraining Trigger) │
    └──────────────┬──────────────┘
                   │
          Trained Model Stored
                   │
              AWS S3 Bucket
                   │
    ┌──────────────▼──────────────┐
    │        FastAPI Service      │
    │   (Inference REST API)      │
    └──────────────┬──────────────┘
                   │
          Docker Container
                   │
            AWS ECR → ECS


---

## Tech Stack

- **Programming & ML:** Python, Scikit-learn, Pandas  
- **API & Backend:** FastAPI, Pydantic, Swagger UI  
- **MLOps & Cloud:** Docker, AWS S3, Lambda, ECR, ECS  
- **Development & Testing:** Git, GitHub Actions, Pytest, Object-Oriented Programming (OOP)

---

## Key Features

- End-to-end ML pipeline: data preprocessing → training → evaluation
- Modular and scalable code structure using OOP
- REST API deployment with FastAPI
- Input validation using Pydantic
- Containerized deployment with Docker
- Cloud deployment on AWS ECS
- Event-driven model retraining via AWS Lambda
- CI/CD pipeline with GitHub Actions for automated testing and deployment

---

## How to Run the API Locally

### Using Docker (Recommended)

```bash
docker build -t course-completion-ml -f docker/Dockerfile.api .
docker run -p 8000:8000 course-completion-ml
```

Open API documentation: http://127.0.0.1:8000/docs


##API Endpoint

POST /predict

Input: JSON containing student engagement features

Output: "Completed" or "Not Completed"

{
  "age": 25,
  "hours_per_week": 10,
  "assignments_submitted": 5,
  "desktop": 1,
  "mobile": 0,
  "pager": 0,
  "smart_tv": 0,
  "tablet": 0
}

Automated Retraining (S3 → Lambda)

New datasets uploaded to AWS S3 trigger an AWS Lambda function.

Lambda retrains the model and stores the updated version back to S3.

FastAPI service automatically loads the latest model for inference.


CI/CD Overview

GitHub Actions pipeline:

Installs dependencies

Runs tests

Builds Docker image

Pushes image to AWS ECR

Ensures automation, reproducibility, and scalability for deployments.



Key Learnings

Building production-ready ML systems

Deploying ML models as scalable APIs

Containerization and cloud deployment (Docker + ECS)

Event-driven model retraining with AWS Lambda

Applying MLOps best practices in practice
