import uuid

from dataclasses import dataclass

from entities import Url, DtoUrl
from repositories import IUrlRepository


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
        hash = uuid.uuid4()
        data = DtoUrl(
            id=0,
            short_url='http://127.0.0.1:5000/{hash}'.format(hash=hash),
            redirect_url=request.redirect_url,
            hits=0,
            hash=str(hash)
        )
        
        url = Url(data)
        
        return CreateUrlResponse(
            object=self.repository.save(url)
        )