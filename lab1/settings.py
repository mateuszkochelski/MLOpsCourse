# settings.py
from typing import Literal

import yaml
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: Literal["dev", "test", "prod"]
    APP_NAME: str
    API_KEY: str


def load_settings(secrets_path: str = "secrets.yaml") -> Settings:
    with open(secrets_path) as file:
        secrets = yaml.safe_load(file)

    return Settings(**secrets)
