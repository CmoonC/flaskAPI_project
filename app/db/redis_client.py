import redis.asyncio as redis
from app.core.config import REDIS_URL

async def get_redis():
    client = redis.from_url(REDIS_URL, decode_responses=True)
    return client