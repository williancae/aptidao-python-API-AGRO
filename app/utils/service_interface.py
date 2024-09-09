from abc import ABC, abstractmethod
from typing import Any, List, Optional


class ServiceInterface(ABC):
    @abstractmethod
    def create(self, params):
        pass

    @abstractmethod
    def update(self, item_id, params):
        pass

    @abstractmethod
    def delete(self, item_id):
        pass

    @abstractmethod
    def get_all(self) -> List:
        pass

    @abstractmethod
    def get_one(self, item_id) -> Optional[Any]:
        pass
