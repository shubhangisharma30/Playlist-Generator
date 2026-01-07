"""
Application configuration
"""

import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import List

load_dotenv()


class Settings(BaseSettings):
    """Application settings"""

    # API Settings
    API_V1_PREFIX: str = os.getenv("API_V1_PREFIX", "/api/v1")
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Playlist Generator API")

    # CORS Settings
    CORS_ORIGINS: List[str] = os.getenv(
        "CORS_ORIGINS",
        "http://localhost:3000,http://localhost:5173,http://localhost:8000,http://127.0.0.1:3000,http://127.0.0.1:5173,http://127.0.0.1:8000",
    ).split(",")

    # Database Settings (for future use)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./playlist_generator.db")

    # Security Settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)

    class Config:
        env_file = os.getenv("ENV_FILE", ".env")
        case_sensitive = os.getenv("CASE_SENSITIVE", True)


settings = Settings()
