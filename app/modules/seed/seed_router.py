from fastapi import APIRouter, Depends
from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.session import get_db_session
from app.modules.seed.seed_model import SeedModel

router = APIRouter(prefix="/seeds", tags=["seeds"])


@router.get(
    "/",
)
async def get_all(session: AsyncSession = Depends(get_db_session)):
    return await session.scalar(Select(SeedModel.name))


seed_router = router
