import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

load_dotenv()

class Settings(BaseSettings):
    DATASTORE_PATH: Optional[str] = None
    EXTERNAL_API_URL: Optional[str] = None
    MODEL: str
    GOOGLE_API_KEY: str
    GOOGLE_APPLICATION_CREDENTIALS: Optional[str] = None
    GOOGLE_CLOUD_PROJECT: Optional[str] = None
    GOOGLE_CLOUD_LOCATION: Optional[str] = None
    GOOGLE_GENAI_USE_VERTEXAI: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()