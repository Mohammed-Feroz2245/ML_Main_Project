from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def download_data():
    print("Downloading data from S3")

def preprocess_data():
    print("Cleaning and preparing data")

def train_model():
    print("Training ML model")

def evaluate_model():
    print("Evaluating model accuracy")

def upload_model():
    print("Uploading model to S3")

with DAG(
    dag_id="ml_retraining_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="download_data",
        python_callable=download_data
    )

    t2 = PythonOperator(
        task_id="preprocess_data",
        python_callable=preprocess_data
    )

    t3 = PythonOperator(
        task_id="train_model",
        python_callable=train_model
    )

    t4 = PythonOperator(
        task_id="evaluate_model",
        python_callable=evaluate_model
    )

    t5 = PythonOperator(
        task_id="upload_model",
        python_callable=upload_model
    )

    t1 >> t2 >> t3 >> t4 >> t5
