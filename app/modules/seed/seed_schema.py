from app.config.models import BaseSchema


class SeedSchema(BaseSchema):
    name: str

    class Config:
        orm_mode = True
