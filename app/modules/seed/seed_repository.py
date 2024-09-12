

from datetime import datetime

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.interfaces.repository_interface import RepositoryInterface
from app.modules.seed.seed_model import SeedModel
from app.modules.seed.seed_schema import CreateSeedSchema, UpdateSeedSchema


class SeedRepository(RepositoryInterface):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.model = SeedModel

    async def get_all(self):
        query = (
            select(self.model)
            .where(self.model.deleted_at.is_(None))
        )
        result = await self.session.scalars(query)
        return list(result)

    async def create(self, data: CreateSeedSchema) -> SeedModel:
        instance = SeedModel(**data.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get(self, item_id: int):
        query = (
            select(self.model)
            .where(self.model.id == item_id)
        )
        result = await self.session.scalar(query)
        if result is None:
            raise HTTPException(
                status_code=404, detail="Semente não encontrada")
        return result

    async def filter(self, *expressions):
        query = (
            select(self.model)
            .filter(*expressions)
        )
        result = await self.session.scalars(query)
        return list(result)

    async def update(self, item_id: int, data: UpdateSeedSchema):
        instance = await self.get(item_id)

        data_dict = data.model_dump(exclude_unset=True)
        for field, value in data_dict.items():

            if value is not None:
                setattr(instance, field, value)

        await self.session.commit()
        await self.session.refresh(instance)

        return instance

    async def soft_delete(self, item_id: int) -> SeedModel:
        instance = await self.get(item_id)
        setattr(instance, "deleted_at", datetime.now())
        await self.session.commit()
        await self.session.refresh(instance)
        return instance
