from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.modules.planting_area.planting_area_model import PlantingAreaModel
from app.modules.planting_area.planting_area_repository import \
    PlantingAreaRepository
from app.modules.planting_area.planting_area_schema import (
    CreatePlantingAreaSchema, UpdatePlantingAreaSchema)


class PlantingAreaService:
    def __init__(self, session: AsyncSession):
        self.repository = PlantingAreaRepository(session)

    async def get_all(self):
        return await self.repository.get_all()

    async def create(self, data: CreatePlantingAreaSchema):
        return await self.repository.create(data)

    async def get_by_id(self, id: int):
        return await self.repository.get(id)

    async def update(self, id: int, data: UpdatePlantingAreaSchema):
        return await self.repository.update(id, data)

    async def delete(self, id: int):
        return await self.repository.soft_delete(id)
