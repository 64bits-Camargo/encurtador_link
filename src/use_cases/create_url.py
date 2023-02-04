import uuid

from dataclasses import dataclass

from src.entities.url import Url, DtoUrl
from src.repositories import IUrlRepository


@dataclass
class CreateUrlRequest:
    redirect_url: str


@dataclass
class CreateUrlResponse:
    object: Url


class CreateUrlUseCase:
    
    def __init__(self, repository: IUrlRepository):
        self.repository = repository
        
    def execute(self, request: CreateUrlRequest) -> CreateUrlResponse:
        data = DtoUrl(
            id=0,
            short_url='http://127.0.0.1:5000/{hash}'.format(hash=uuid.uuid4()),
            redirect_url=request.redirect_url,
            hits=0
        )
        
        url = Url(data)
        
        return CreateUrlResponse(
            object=self.repository.save(url)
        )