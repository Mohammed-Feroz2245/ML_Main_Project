import boto3
import pickle
import os
import pandas as pd

class CourseCompletionModel:
    def __init__(self):
        # S3 details
        self.bucket_name = "course-completion-ml-artifacts"
        self.model_key = "artifacts/model.pkl"
        self.local_model_path = "/tmp/model.pkl"

        # Create S3 client
        s3 = boto3.client("s3")

        # Download model from S3 (only once at startup)
        if not os.path.exists(self.local_model_path):
            s3.download_file(
                self.bucket_name,
                self.model_key,
                self.local_model_path
            )

        # Load model into memory
        with open(self.local_model_path, "rb") as f:
            self.model = pickle.load(f)

    def predict(self, input_data: dict):
        df = pd.DataFrame([input_data])
        prediction = self.model.predict(df)[0]
        return int(prediction)