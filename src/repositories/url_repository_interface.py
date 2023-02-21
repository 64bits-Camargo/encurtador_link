from abc import ABC, abstractmethod

from entities import Url


class IUrlRepository(ABC):
    
    @abstractmethod
    def save(self, url: Url) -> Url: ...