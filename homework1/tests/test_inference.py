from pathlib import Path

import pytest
from inference import load_model, predict_sentiment

BASE_DIR = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def models():
    return load_model(
        BASE_DIR / "sentence_transformer.model",
        BASE_DIR / "classifier.joblib",
    )


def test_load_model_returns_models(models):
    transformer, classifier = models

    assert transformer is not None
    assert classifier is not None


@pytest.mark.parametrize(
    ("text", "expected_prediction"),
    [
        ("I hate this product, it is terrible and disappointing", "negative"),
        ("Sky is blue", "neutral"),
        ("I love this course, it is fantastic and very helpful", "positive"),
    ],
)
def test_predict_sentiment_matches_expected_samples(models, text, expected_prediction):
    transformer, classifier = models

    prediction = predict_sentiment(transformer, classifier, text)
    assert prediction == expected_prediction
