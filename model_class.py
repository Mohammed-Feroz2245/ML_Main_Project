import pickle
import pandas as pd

class CourseCompletionModel:
    def __init__(self):
        with open("model.pkl", "rb") as f:
            self.model = pickle.load(f)

    def predict(self, input_data: dict):
        df = pd.DataFrame([input_data])
        prediction = self.model.predict(df)[0]
        return int(prediction)
