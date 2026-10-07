import pytest
from app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_predict_returns_valid_json_response():
    response = client.post(
        "/predict",
        json={"text": "What a great MLOps lecture, I am very satisfied"},
    )

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.json().keys() == {"prediction"}
    assert isinstance(response.json()["prediction"], str)


@pytest.mark.parametrize(
    "payload",
    [{}, {"text": ""}, {"text": "   "}, {"text": 123}],
)
def test_predict_rejects_invalid_text(payload):
    response = client.post("/predict", json=payload)

    assert response.status_code == 422
    assert response.headers["content-type"].startswith("application/json")
    assert "detail" in response.json()
