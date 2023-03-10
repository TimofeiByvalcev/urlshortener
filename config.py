#urlshortener/config.py

from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shoretener.db"


def get_setting() -> Settings:
    settings = Settings()
    print(f"LOadding setting for: {settings.env_name}")
    return settings

