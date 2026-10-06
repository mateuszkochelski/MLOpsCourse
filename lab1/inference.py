import joblib
import numpy as np

FEATURE_NAMES = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
TARGET_NAMES = ["setosa", "versicolor", "virginica"]


def load_model(path: str):
    return joblib.load(path)


def predict_iris(model, data: dict) -> str:
    row = np.array([[data[name] for name in FEATURE_NAMES]])
    prediction = model.predict(row)[0]
    return TARGET_NAMES[int(prediction)]
