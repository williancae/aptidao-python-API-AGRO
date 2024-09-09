import asyncio
import logging

from sqlalchemy.ext.asyncio import create_async_engine

from ..app.config import settings
from ..app.config.models import Base

logger = logging.getLogger()


async def migrate_tables() -> None:
    """
    Migra tabelas no banco de dados.

    Esta função cria tabelas no banco de dados usando o método `create_all` do SQLAlchemy.
    Ela se conecta ao banco de dados usando a `DATABASE_URL` fornecida pelo módulo de configurações.
    O processo de migração é registrado usando o módulo de log.

    Retorna:
        None
    """
    logger.info("Starting to migrate")

    engine = create_async_engine(settings.DATABASE_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logger.info("Done migrating")


if __name__ == "__main__":
    asyncio.run(migrate_tables())


# ! Para executar o script de migração, você pode usar o seguinte comando:
# $ python scripts/migrate.py
