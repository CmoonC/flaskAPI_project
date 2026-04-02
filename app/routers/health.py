# app/routers/health.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.db.session import get_db
from app.db.redis_client import get_redis
from app.utils.logging import logger

router = APIRouter()

@router.get("/")
async def health_check(
        db: AsyncSession = Depends(get_db),
        redis = Depends(get_redis)
):
    """Health check endpoint with database pings"""
    logger.info("Health check requested")
    # Check PostgreSQL
    try:
        await db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        db_status = f"disconnected: {str(e)}"

    # Check Redis
    try:
        await redis.ping()
        redis_status = "connected"
    except Exception as e:
        redis_status = f"disconnected: {str(e)}"

    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working",
        "systems": {
            "database": db_status,
            "redis": redis_status
        }
    }