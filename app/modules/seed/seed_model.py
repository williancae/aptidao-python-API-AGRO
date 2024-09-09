from sqlalchemy import Column, String

from app.config.models import Base


class SeedModel(Base):
    __tablename__ = "seed"
    __table_args__ = {"extend_existing": True}

    name = Column("name", String, nullable=False)
