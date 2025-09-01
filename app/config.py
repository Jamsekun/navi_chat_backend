from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    # Database
    database_url: str
    test_database_url: str
    
    # Security
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # External Services
    mapbox_access_token: str
    dialogflow_project_id: str
    dialogflow_private_key_id: str
    dialogflow_private_key: str
    dialogflow_client_email: str
    
    # Firebase
    firebase_project_id: str
    firebase_private_key_id: str
    firebase_private_key: str
    firebase_client_email: str
    
    # Redis
    redis_url: str
    
    # App Settings
    debug: bool = False
    environment: str = "production"
    cors_origins: List[str] = []
    
    class Config:
        env_file = ".env"

settings = Settings()