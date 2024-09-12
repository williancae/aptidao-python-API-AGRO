

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.session import get_db_session
from app.modules.seed.seed_schema import CreateSeedSchema, UpdateSeedSchema
from app.modules.seed.seed_service import SeedService

router = APIRouter(prefix="/seeds", tags=["Seeds"], dependencies=[])


@router.post("/",)
async def create(
    body: CreateSeedSchema,
    session: AsyncSession = Depends(get_db_session)
):
    return await SeedService(session).create(body)


@router.get("/{item_id}",)
async def get_one(
    item_id: int,
    session: AsyncSession = Depends(get_db_session)
):
    return await SeedService(session).get_one(item_id)


@router.get("/",)
async def get_all(
    session: AsyncSession = Depends(get_db_session)
):
    return await SeedService(session).get_all()


@router.put("/{item_id}",)
async def update(
    item_id: int,
    body: UpdateSeedSchema,
    session: AsyncSession = Depends(get_db_session),
):
    return await SeedService(session).update(item_id, body)


@router.delete("/{item_id}",)
async def delete(
    item_id: int,
    session: AsyncSession = Depends(get_db_session)
):
    return await SeedService(session).delete(item_id)

seed_router = router
