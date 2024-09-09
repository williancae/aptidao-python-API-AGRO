from pydantic import BaseModel

from app.config.models import BaseSchema


class SeedSchema(BaseSchema):
    name: str

    class Config:
        from_attributes = True


class CreateSeedSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True


class UpdateSeedSchema(CreateSeedSchema):
    pass

    class Config:
        from_attributes = True
