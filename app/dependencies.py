

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import models
from app.config.session import get_db_session


def get_repository(
    model: type[models.Base],
    repository
):
    def func(session: AsyncSession = Depends(get_db_session)):
        return repository(session)

    return func
