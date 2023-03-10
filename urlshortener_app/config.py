# urlshortener/config.py

from pydantic import BaseSettings
from functools import lru_cache


class LocalSettings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shoretener.db"


@lru_cache()
def get_settings() -> LocalSettings:
    settings = LocalSettings()
    print(f"Loading setting for: {settings.env_name}")
    return settings


class Config:
    env_file = ".env"
