
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.session import get_db_session
from app.modules.planting_area.planting_area_schema import (
    CreatePlantingAreaSchema, UpdatePlantingAreaSchema)
from app.modules.planting_area.planting_area_service import PlantingAreaService

router = APIRouter(
    prefix="/planting-area",
    tags=["Planting Area"],
    dependencies=[]
)


@router.get("/")
async def get_all(
    session: AsyncSession = Depends(get_db_session)
):
    return await PlantingAreaService(session).get_all()


@router.post("/")
async def create(
    data: CreatePlantingAreaSchema,
    session: AsyncSession = Depends(get_db_session)
):
    return await PlantingAreaService(session).create(data)


@router.get("/{id}")
async def get_by_id(
    id: int,
    session: AsyncSession = Depends(get_db_session)
):
    return await PlantingAreaService(session).get_by_id(id)


@router.put("/{id}")
async def update(
    id: int,
    data: UpdatePlantingAreaSchema,
    session: AsyncSession = Depends(get_db_session)
):
    return await PlantingAreaService(session).update(id, data)


@router.delete("/{id}")
async def delete(
    id: int,
    session: AsyncSession = Depends(get_db_session)
):
    return await PlantingAreaService(session).delete(id)


planting_area_router = router
