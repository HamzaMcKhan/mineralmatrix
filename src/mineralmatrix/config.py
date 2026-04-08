import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://mineralmatrix:mineralmatrix@localhost:5432/mineralmatrix",
    )
    app_env: str = os.getenv("APP_ENV", "development")

settings = Settings()
