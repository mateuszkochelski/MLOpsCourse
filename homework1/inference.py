from pathlib import Path

import joblib
from sentence_transformers import SentenceTransformer

TARGET_NAMES = ["negative", "neutral", "positive"]


def load_model(transformer_path: Path, classifier_path: Path):
    sentence_transformer = SentenceTransformer(str(transformer_path))
    classifier = joblib.load(classifier_path)
    return sentence_transformer, classifier


def predict_sentiment(transformer, classifier, sentence):
    embedding = transformer.encode(sentence)
    return TARGET_NAMES[classifier.predict(embedding.reshape(1, -1))[0]]
