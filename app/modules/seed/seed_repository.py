from app.config.repository import DatabaseRepository
from app.modules.seed.seed_model import SeedModel


class SeedRepository(DatabaseRepository[SeedModel]):
    def __init__(self, session):
        super().__init__(SeedModel, session)
    pass
