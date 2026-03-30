# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:password@db:5432/postgres")
REDIS_URL= os.getenv("REDIS_URL", "redis://redis:6379/0")