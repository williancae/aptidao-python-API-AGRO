import re
from datetime import datetime

from fastapi import HTTPException
from fastapi.background import P
from sqlalchemy import event, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.config.interfaces.repository_interface import RepositoryInterface
from app.modules.planting_area.planting_area_model import PlantingAreaModel
from app.modules.rural_producer.rural_producer_model import RuralProducerModel
from app.modules.rural_producer.rural_producer_schema import (
    CreateRuralProducerSchema, UpdateRuralProducerSchema)


class RuralProducerRepository(RepositoryInterface):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.model = RuralProducerModel

    async def get_all(self):
        query = (
            select(self.model)
            .where(self.model.deleted_at.is_(None))
        )
        result = await self.session.scalars(query)
        return list(result)

    async def create(self,
                     data: CreateRuralProducerSchema
                     ) -> RuralProducerModel:
        instance = RuralProducerModel(**data.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get(self, item_id: int):
        query = (
            select(self.model)
            .options(
                selectinload(RuralProducerModel.planting_areas).selectinload(
                    PlantingAreaModel.seed
                )
            )
            .where(self.model.id == item_id)
        )

        result = await self.session.scalar(query)
        if result is None:
            raise HTTPException(
                status_code=404, detail="Produtor rural não encontrado")
        return result

    async def filter(self, *expressions):
        query = (
            select(self.model)
            .filter(*expressions)
        )
        result = await self.session.scalars(query)
        return list(result)

    async def update(self, item_id: int, data: UpdateRuralProducerSchema):
        instance = await self.get(item_id)

        data_dict = data.model_dump(exclude_unset=True)
        for field, value in data_dict.items():

            if value is not None:
                setattr(instance, field, value)

        await self.session.commit()
        await self.session.refresh(instance)

        return instance

    async def soft_delete(self, item_id: int):
        instance = await self.get(item_id)
        instance.deleted_at = datetime.now()
        await self.session.commit()
        return instance

    @staticmethod
    def before_update_and_insert(mapper, connection, target):
        target.document_number = re.sub(r'\D', '', target.document_number)


event.listen(RuralProducerModel, 'before_insert',
             RuralProducerRepository.before_update_and_insert)
event.listen(RuralProducerModel, 'before_update',
             RuralProducerRepository.before_update_and_insert)
