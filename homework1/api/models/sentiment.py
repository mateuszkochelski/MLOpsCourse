from typing import Annotated

from pydantic import BaseModel, StringConstraints


class SentimentRequest(BaseModel):
    text: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class SentimentResponse(BaseModel):
    prediction: str
