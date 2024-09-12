

from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.seed.seed_model import SeedModel
from app.modules.seed.seed_repository import SeedRepository
from app.modules.seed.seed_schema import CreateSeedSchema
from app.config.interfaces.service_interface import ServiceInterface


class SeedService(ServiceInterface):

    def __init__(self, session: AsyncSession):
        self.repository = SeedRepository(session)

    async def create(self, payload: CreateSeedSchema) -> SeedModel:
        response = await self.repository.create(payload)
        return response

    async def update(self, item_id, payload) -> SeedModel | None:
        return await self.repository.update(item_id, payload)

    async def delete(self, item_id) -> None:
        await self.repository.soft_delete(item_id)

    async def get_all(self):
        response = await self.repository.get_all()
        return response

    async def get_one(self, item_id) -> SeedModel | None:
        return await self.repository.get(item_id)
