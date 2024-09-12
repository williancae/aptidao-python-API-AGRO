from datetime import datetime
from typing import List, Optional

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.sql.expression import BinaryExpression

from app.config.interfaces.repository_interface import RepositoryInterface
from app.modules.planting_area.planting_area_model import PlantingAreaModel
from app.modules.planting_area.planting_area_schema import (
    CreatePlantingAreaSchema, UpdatePlantingAreaSchema)


class PlantingAreaRepository(RepositoryInterface):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.model = PlantingAreaModel

    async def get_all(self) -> List[PlantingAreaModel]:
        query = (
            select(self.model)
            .options(
                selectinload(self.model.rural_producer),
                selectinload(self.model.seed)
            )
            .where(self.model.deleted_at.is_(None))
        )
        query_result = await self.session.scalars(query)
        return list(query_result)

    async def create(
        self, data: CreatePlantingAreaSchema
    ) -> PlantingAreaModel:
        instance = PlantingAreaModel(**data.model_dump())
        self.session.add(instance)
        await self.session.commit()

        await self.session.refresh(instance)
        return instance

    async def get(self, item_id: int) -> Optional[PlantingAreaModel] | None:
        query = (
            select(self.model)
            .where(self.model.id == item_id)
            .options(
                selectinload(self.model.rural_producer),
                selectinload(self.model.seed)
            )
        )
        query_result = await self.session.scalar(query)
        if query_result is None:
            raise HTTPException(
                status_code=404, detail="Area de Plantio não encontrada")
        return query_result

    async def filter(self,
                     *expressions: BinaryExpression
                     ) -> List[PlantingAreaModel]:
        query = (
            select(self.model)
            .where(*expressions)
            .options(
                selectinload(self.model.rural_producer),
                selectinload(self.model.seed)
            )
        )
        query_result = await self.session.scalars(query)
        return list(query_result)

    async def update(self,
                     item_id: int,
                     data: UpdatePlantingAreaSchema
                     ) -> PlantingAreaModel | None:
        instance = await self.get(item_id)
        for field, value in data:
            if value is not None:
                print(field, value)
                setattr(instance, field, value)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def soft_delete(self, item_id: int) -> PlantingAreaModel | None:
        instance = await self.get(item_id)
        setattr(instance, "deleted_at", datetime.now())
        await self.session.commit()
        await self.session.refresh(instance)
        return instance
