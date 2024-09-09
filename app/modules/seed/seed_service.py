

from typing import List

from fastapi import HTTPException

from app.modules.seed.seed_model import SeedModel
from app.modules.seed.seed_repository import SeedRepository
from app.utils.service_interface import ServiceInterface


class SeedService(ServiceInterface):

    def __init__(self, repository: SeedRepository):
        self.repository = repository

    async def create(self, payload: dict) -> SeedModel | None:
        response = await self.repository.create(payload)
        return response

    async def update(self, item_id, payload) -> SeedModel | None:
        seed = await self.get_one(item_id)
        if seed:
            response = await self.repository.update(seed, payload)
            return response
        return None

    async def delete(self, item_id) -> None:
        model = await self.get_one(item_id)
        if model:
            await self.repository.soft_delete(model)

    async def get_all(self):
        response = await self.repository.filter()
        return response

    async def get_one(self, item_id) -> SeedModel | None:
        response = await self.repository.get(item_id)

        if not response:
            raise HTTPException(
                status_code=404, detail="Semente não encontrada pelo ID")
        return response
