from typing import Optional

from pydantic import BaseModel


class CreateSeedSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True


class UpdateSeedSchema(BaseModel):
    name: Optional[str] = "Willian Caetano"

    class Config:
        from_attributes = True
