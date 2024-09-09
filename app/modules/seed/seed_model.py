from sqlalchemy import Column, String

from app.config.models import Base


class SeedModel(Base):
    __tablename__ = "seed"

    name = Column("name", String, nullable=False)
