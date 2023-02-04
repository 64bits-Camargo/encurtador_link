from abc import ABC, abstractmethod

from src.entities.url import Url


class IUrlRepository(ABC):
    
    @abstractmethod
    def save(self, url: Url) -> Url: ...