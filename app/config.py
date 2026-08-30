from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """App config, read from environment variables."""

    app_name: str = "api-starter"
    debug: bool = False


settings = Settings()
