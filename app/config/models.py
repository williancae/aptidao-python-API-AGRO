from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Integer, orm

# Classe Base para os modelos SQLAlchemy


class Base(orm.DeclarativeBase):
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default="now()")
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.now())


# Classe HelpModel com Pydantic para validação e serialização
class BaseSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
