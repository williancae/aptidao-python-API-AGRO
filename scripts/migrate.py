import asyncio
import os
import sys

from sqlalchemy.ext.asyncio import create_async_engine

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from app.config.models import Base, import_models_from_modules

import_models_from_modules()


async def migrate_tables() -> None:
    try:
        print("Creating tables...")
        engine = create_async_engine("postgresql+asyncpg://postgres:postgres@db:5432/api-agro")
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    except Exception as e:
        print("Error message: ", e)


if __name__ == "__main__":
    asyncio.run(migrate_tables())


# ! Para executar o script de migração, você pode usar o seguinte comando:
# $ python scripts/migrate.py
