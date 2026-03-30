from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.core.config import DATABASE_URL

#1 Creating the engine
engine = create_async_engine(
    DATABASE_URL,
    echo = True,
    )

#2 Creating a session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

#3 Dependency to get DB session in FastAPI routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

