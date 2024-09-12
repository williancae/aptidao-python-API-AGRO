from abc import ABC, abstractmethod
from typing import Any, List, Optional


class ServiceInterface(ABC):
    @abstractmethod
    async def create(self, payload):
        raise NotImplementedError

    @abstractmethod
    async def update(self, item_id, payload):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, item_id):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> List:
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, item_id) -> Optional[Any]:
        raise NotImplementedError
