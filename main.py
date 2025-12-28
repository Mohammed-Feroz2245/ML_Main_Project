from fastapi import FastAPI
from pydantic import BaseModel
from model_class import CourseCompletionModel

app = FastAPI()
model = CourseCompletionModel()

class StudentInput(BaseModel):
    age: int
    hours_per_week: int
    assignments_submitted: int
    desktop: int
    mobile: int
    pager: int
    smart_tv: int
    tablet: int

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict_course(data: StudentInput):
    input_data = data.dict()
    result = model.predict(input_data)
    return {"prediction": "Completed" if result == 1 else "Not Completed"}
