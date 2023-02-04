from dataclasses import dataclass


@dataclass
class DtoUrl:
    id: int
    short_url: str
    redirect_url: str
    hits: int


class Url:
    
    def __init__(self, props: DtoUrl):
        self._props = props
        
    @property
    def id(self) -> int:
        return self._props.id
    
    @property
    def short_url(self) -> str:
        return self._props.short_url
    
    @property
    def redirect_url(self) -> str:
        return self._props.redirect_url

    @property
    def hits(self) -> int:
        return self._props.hits
