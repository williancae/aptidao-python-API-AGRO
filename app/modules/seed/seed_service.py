from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from utils.service_interface import ServiceInterface

from app.modules.seed.seed_model import SeedModel
from app.modules.seed.seed_schema import SeedSchema


class SeedService(ServiceInterface):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, params):
        pass

    async def update(self, item_id, params):
        pass

    async def delete(self, item_id):
        pass

    async def get_all(self):
        return await self.db.scalars(select(SeedModel.name))

    async def get_one(self, item_id) -> SeedSchema | None:
        return None
