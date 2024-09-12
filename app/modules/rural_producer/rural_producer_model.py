
from typing import ForwardRef

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.config.models import Base

PlantingAreaModel = ForwardRef(
    "app.modules.planting_area.planting_area_model.PlantingAreaModel")


class RuralProducerModel(Base):
    __tablename__ = "rural_producer"
    __table_args__ = {"extend_existing": True}

    document_number = Column("document_number", String, nullable=False)
    name = Column("name", String, nullable=False)
    farm_name = Column("farm_name", String, nullable=False)
    city = Column("city", String, nullable=False)
    state = Column("state", String, nullable=False)

    planting_areas = relationship(
        "PlantingAreaModel", back_populates="rural_producer")
