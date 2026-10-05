# settings.py
from typing import Literal

import yaml
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: Literal["dev", "test", "prod"]
    APP_NAME: str
    API_KEY: str


def load_settings() -> Settings:
    with open("secrets.yaml") as file:
        secrets = yaml.safe_load(file)

    return Settings(**secrets)
