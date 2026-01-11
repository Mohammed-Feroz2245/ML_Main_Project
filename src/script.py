import pandas as pd
import boto3
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

BUCKET_NAME = "course-completion-ml-artifacts"
DATA_KEY = "data/online_course_completion(3).csv"
MODEL_KEY = "artifacts/model.pkl"

s3 = boto3.client("s3")

def train_and_upload():
    # Lambda writable paths
    data_path = "/tmp/data.csv"
    model_path = "/tmp/model.pkl"

    # STEP 1: DOWNLOAD DATA
    s3.download_file(BUCKET_NAME, DATA_KEY, data_path)
    df = pd.read_csv(data_path)

    # STEP 2: CLEANING
    df.drop_duplicates(inplace=True)

    df.drop(
        [
            'height_cm', 'weight_kg', 'num_siblings', 'has_pet',
            'favorite_color', 'birth_month'
        ],
        axis=1,
        inplace=True,
        errors="ignore"
    )

    df.dropna(inplace=True)

    # STEP 3: ENCODING
    dummies = pd.get_dummies(df["preferred_device"], drop_first=True).astype(int)
    df = pd.concat([df, dummies], axis=1)

    X = df.drop(
        [
            "continent",
            "country",
            "education_level",
            "preferred_device",
            "completed_course"
        ],
        axis=1,
        errors="ignore"
    )

    y = df["completed_course"]

    # STEP 4: TRAIN
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print("Accuracy:", acc)

    # STEP 5: SAVE MODEL
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    # STEP 6: UPLOAD MODEL
    s3.upload_file(model_path, BUCKET_NAME, MODEL_KEY)

    return acc
