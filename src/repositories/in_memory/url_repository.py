from entities import Url
from repositories import IUrlRepository


class InMemoryRepository(IUrlRepository):
    
    table = {}
    id = 0
    
    def set_id(self, url) -> Url:
        url._props.id = self.id
        self.id += 1
        return url

    def save(self, url: Url) -> Url:
        self.table[self.id] = self.set_id(url)
        
        return self.table[self.id]
    

    def get(self, hash: str) -> Url:
        
        for url in self.table.values():
            if url.hash == hash:
                return url