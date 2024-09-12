from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.session import get_db_session
from app.dependencies import get_repository
from app.modules.rural_producer.rural_producer_model import RuralProducerModel
from app.modules.rural_producer.rural_producer_repository import \
    RuralProducerRepository
from app.modules.rural_producer.rural_producer_schema import (
    CreateRuralProducerSchema, UpdateRuralProducerSchema)
from app.modules.rural_producer.rural_producer_service import \
    RuralProducerService

router = APIRouter(
    prefix="/rural-producers",
    tags=["Rural Producers"],
    dependencies=[]
)


@router.post("/")
async def create(
    payload: CreateRuralProducerSchema,
    session: AsyncSession = Depends(get_db_session)
):
    return await RuralProducerService(session).create(payload)


@router.get("/{id}")
async def get_by_id(
    id: int,
    session: AsyncSession = Depends(get_db_session)
):
    return await RuralProducerService(session).get_one(id)


@router.get("/")
async def get_all(
    session: AsyncSession = Depends(get_db_session)
):
    return await RuralProducerService(session).get_all()


@router.put("/{id}")
async def update(
    id: int,
    payload: UpdateRuralProducerSchema,
    session: AsyncSession = Depends(get_db_session)
):
    return await RuralProducerService(session).update(
        id,
        payload
    )


@router.delete("/{id}")
async def delete(
    id: int,
    session: AsyncSession = Depends(get_db_session)
):
    return await RuralProducerService(session).delete(id)

rural_producer_router = router
