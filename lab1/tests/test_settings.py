from settings import load_settings


def test_load_settings():

    settings = load_settings("tests/test_secrets.yaml")

    assert settings.ENVIRONMENT == "test"

    assert settings.APP_NAME == "test-app"

    assert settings.API_KEY == "test-api-key"
