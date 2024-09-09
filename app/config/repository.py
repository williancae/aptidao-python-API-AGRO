import uuid
from datetime import datetime
from typing import Generic, List, Optional, TypeVar

from sqlalchemy import BinaryExpression, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.models import Base

Model = TypeVar("Model", bound=Base)


class DatabaseRepository(Generic[Model]):
    """Repository for performing basic database operations."""

    def __init__(self, model: type[Model], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def create(self, data: dict) -> Model:
        instance = self.model(**data)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get(self, pk: uuid.UUID) -> Optional[Model]:
        return await self.session.get(self.model, pk)

    async def filter(self, *expressions: BinaryExpression) -> List[Model]:
        query = select(self.model)
        if expressions:
            query = query.where(*expressions)
        query = query.where(self.model.deleted_at.is_(None))
        return list(await self.session.scalars(query))

    async def update(self, instance: Model, data: dict) -> Model:
        for key, value in data.items():
            setattr(instance, key, value)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def soft_delete(self, instance: Model) -> Model:
        setattr(instance, "deleted_at", datetime.now())
        await self.session.commit()
        await self.session.refresh(instance)
        return instance
