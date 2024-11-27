import os

from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    TITTLE: str = "Bus Location API"
    VERSION: str = "1.0.0"

    IS_DEV: bool = os.getenv("IS_DEV", True)
    MONGO_USER: str = os.getenv("MONGO_USER")
    MONGO_PASSWORD: str = os.getenv("MONGO_PASSWORD")
    MONGO_HOST: str = os.getenv("MONGO_HOST")
    MONGO_PORT: str = os.getenv("MONGO_PORT")
    DB_URL = "mongodb://localhost:27017" if IS_DEV else f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"


settings = Settings()