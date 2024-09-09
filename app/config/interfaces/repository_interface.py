import uuid
from abc import abstractmethod
from typing import Generic, TypeVar

from sqlalchemy import BinaryExpression

from app.config import models

Model = TypeVar("Model", bound=models.Base)


class RepositoryInterface(Generic[Model]):
    """Repository interface for performing database queries."""
    @abstractmethod
    async def create(self, data: dict) -> Model:
        raise NotImplementedError

    @abstractmethod
    async def get(self, pk: uuid.UUID) -> Model | None:
        raise NotImplementedError

    @abstractmethod
    async def filter(
        self,
        *expressions: BinaryExpression,
    ) -> list[Model]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, instance: Model, data: dict) -> Model:
        raise NotImplementedError

    @abstractmethod
    async def soft_delete(self, instance: Model) -> Model:
        raise NotImplementedError
