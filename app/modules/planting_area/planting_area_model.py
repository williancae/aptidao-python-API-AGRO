

from typing import ForwardRef

from pydantic import BaseModel
from sqlalchemy import Column, Float, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from app.config.models import Base

SeedModel = ForwardRef("SeedModel")
RuralProducerModel = ForwardRef(
    "RuralProducerModel"
)


class PlantingAreaModel(Base):
    __tablename__ = "planting_area"
    __table_args__ = {"extend_existing": True}

    total_area = Column("total_area", Float, nullable=False)
    cultivable_area = Column("cultivable_area", Float, nullable=False)
    vegetation_area = Column("vegetation_area", Float, nullable=False)

    rural_producer_id = mapped_column(ForeignKey("rural_producer.id"))
    rural_producer = relationship(
        "RuralProducerModel", back_populates="planting_areas")

    seed_id = mapped_column(ForeignKey("seed.id"))
    seed = relationship("SeedModel", back_populates="planting_areas")
