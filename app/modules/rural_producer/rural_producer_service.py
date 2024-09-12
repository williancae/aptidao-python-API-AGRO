

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.rural_producer.rural_producer_model import RuralProducerModel
from app.modules.rural_producer.rural_producer_repository import \
    RuralProducerRepository
from app.modules.rural_producer.rural_producer_schema import (
    CreateRuralProducerSchema, UpdateRuralProducerSchema)
from app.config.interfaces.service_interface import ServiceInterface


class RuralProducerService(ServiceInterface):
    def __init__(self, session: AsyncSession):
        self.repository = RuralProducerRepository(session)

    async def create(self,
                     payload: CreateRuralProducerSchema
                     ) -> RuralProducerModel:
        response = await self.repository.create(payload)
        return response

    async def update(self, item_id: int, payload: UpdateRuralProducerSchema
                     ) -> RuralProducerModel | None:
        return await self.repository.update(item_id, payload)

    async def delete(self, item_id: int) -> None:
        return await self.repository.soft_delete(item_id)

    async def get_all(self):
        return await self.repository.get_all()

    async def get_one(self, item_id: int) -> RuralProducerModel | None:
        return await self.repository.get(item_id)
