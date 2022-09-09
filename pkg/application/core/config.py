import os
from pydantic import BaseSettings


from pathlib import Path

class Settings(BaseSettings):
    PROJECT_NAME:str 
    PROJECT_VERSION: str 

    POSTGRES_USER : str 
    POSTGRES_PASSWORD : str
    POSTGRES_SERVER : str 
    POSTGRES_PORT : str 
    POSTGRES_DB : str 

    class Config:
        case_sensitive = True
        env_file = '.env'
        
settings = Settings()