from pathlib import Path

from api.models.sentiment import SentimentRequest, SentimentResponse
from fastapi import FastAPI
from inference import load_model, predict_sentiment

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

transformer, classifier = load_model(
    BASE_DIR / "sentence_transformer.model", BASE_DIR / "classifier.joblib"
)


@app.post("/predict")
def predict(request: SentimentRequest) -> SentimentResponse:
    prediction = predict_sentiment(transformer, classifier, request.text)
    return SentimentResponse(prediction=prediction)
