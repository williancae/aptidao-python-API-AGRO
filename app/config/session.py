import logging
from collections.abc import AsyncGenerator

from sqlalchemy import exc
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import settings

logger = logging.getLogger()

engine = create_async_engine(settings.DATABASE_URL)
factory = async_sessionmaker(engine)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:

    async with factory() as session:
        try:
            yield session
            await session.commit()
        except exc.SQLAlchemyError:
            await session.rollback()
            raise
