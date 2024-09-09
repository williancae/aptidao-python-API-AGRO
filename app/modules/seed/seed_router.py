from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import Update

from app.dependencies import get_repository
from app.modules.seed.seed_model import SeedModel
from app.modules.seed.seed_repository import SeedRepository
from app.modules.seed.seed_schema import CreateSeedSchema, UpdateSeedSchema
from app.modules.seed.seed_service import SeedService

router = APIRouter(prefix="/seeds", tags=["seeds"], dependencies=[])

Repository = Annotated[
    SeedRepository,
    Depends(get_repository(SeedModel))
]


@router.post("/",)
async def create(
    body: CreateSeedSchema,
    repository: Repository
):
    return await SeedService(repository).create(body.model_dump())


@router.get("/{item_id}",)
async def get_one(
    item_id: int,
    repository: Repository
):
    return await SeedService(repository).get_one(item_id)


@router.get("/",)
async def get_all(
    repository: Repository
):
    return await SeedService(repository).get_all()


@router.put("/{item_id}",)
async def update(
    item_id: int,
    body: UpdateSeedSchema,
    repository: Repository
):
    return await SeedService(repository).update(item_id, body.model_dump())


@router.delete("/{item_id}",)
async def delete(
    item_id: int,
    repository: Repository
):
    return await SeedService(repository).delete(item_id)

seed_router = router
