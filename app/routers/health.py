# app/routers/health.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    """Health check endpoint"""
    return {"status_code": 200, "detail": "ok", "result": "working"}