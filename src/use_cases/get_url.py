from dataclasses import dataclass

from entities import Url, DtoUrl
from repositories import IUrlRepository


@dataclass
class GetUrlRequest:
    hash: str


@dataclass
class GetUrlResponse:
    object: Url


class GetUrlUseCase:
    
    def __init__(self, repository: IUrlRepository):
        self.repository = repository
        
    def execute(self, request: GetUrlRequest) -> GetUrlResponse:
        return GetUrlResponse(
            object=self.repository.get(str(request.hash))
        )