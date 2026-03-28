#app/main.py
from fastapi import FastAPI
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware

from app.routers import health
import os

#loads environment variables from .env file (kept private)
load_dotenv()

#Access secret keys and database URL from environment
SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

#initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #Allows all origins from now
    allow_credentials=True,
    allow_methods=["*"], #Allows all methods
    allow_headers=["*"], #Allows all headers
)
#Include health router
app.include_router(health.router, prefix="")


