from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()   #loads environment variables from .env

SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
app = FastAPI()

#Running a health check
@app.get("/")
def health_check():
    return {"status_code": 200,
            "detail": "ok",
            "result": "working"}


