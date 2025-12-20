import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle


df = pd.read_csv("C:/Users/feroz/MyNew_Notebook/ML_Main_Project/data/online_course_completion(3).csv")


df.drop_duplicates(inplace=True)


df = df.drop([
    'height_cm', 'weight_kg', 'num_siblings', 'has_pet',
    'favorite_color', 'birth_month'
], axis=1)


df = df.dropna()


dummies = pd.get_dummies(df['preferred_device'], drop_first=True).astype(int)


df = pd.concat([df, dummies], axis=1)


X = df.drop([
    'continent', 'country', 'education_level',
    'preferred_device', 'completed_course'
], axis=1)


y = df['completed_course']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))


with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
