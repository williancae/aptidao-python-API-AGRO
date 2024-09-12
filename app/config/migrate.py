from sqlalchemy.ext.asyncio import create_async_engine

from app.config.models import Base
from app.config.settings import DATABASE_URL

engine = create_async_engine(DATABASE_URL)


async def migrate_tables() -> None:
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    except Exception as e:
        print("Error message: ", e)
