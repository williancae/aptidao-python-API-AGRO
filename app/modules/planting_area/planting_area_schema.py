from typing import Optional

from pydantic import BaseModel, Field, model_validator


class CreatePlantingAreaSchema(BaseModel):
    total_area: float = Field(..., gt=0)
    cultivable_area: float = Field(..., gt=0)
    vegetation_area: float = Field(..., gt=0)
    seed_id: int
    rural_producer_id: int

    class Config:
        from_attributes = True


class UpdatePlantingAreaSchema(BaseModel):
    total_area: Optional[float] = None
    cultivable_area: Optional[float] = None
    vegetation_area: Optional[float] = None
    seed_id: Optional[int] = None
    rural_producer_id: Optional[int] = None

    class Config:
        from_attributes = True
