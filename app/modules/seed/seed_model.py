from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.config.models import Base


class SeedModel(Base):
    __tablename__ = "seed"
    __table_args__ = {"extend_existing": True}

    name = Column("name", String, nullable=False)

    planting_areas = relationship("PlantingAreaModel", back_populates="seed")
