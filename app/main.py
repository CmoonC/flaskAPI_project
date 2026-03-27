#app/main.py
from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers import health
import os

#loads environment variables from .env file (kept private)
load_dotenv()

#Access secret keys and database URL from environment
SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

#initialize FastAPI app
app = FastAPI()

#Include health router
app.include_router(health.router, prefix="")


