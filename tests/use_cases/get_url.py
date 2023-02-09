import unittest

from src.entities.url import Url
from src.repositories import InMemoryRepository
from src.use_cases.get_url import GetUrlUseCase
from src.use_cases.create_url import CreateUrlUseCase, CreateUrlRequest


class TestUrl(unittest.TestCase):
    def test_get_url(self):
        url_repository = InMemoryRepository()
        create_url = CreateUrlUseCase(url_repository)
        get_url = GetUrlUseCase(url_repository)
        
        data_request = CreateUrlRequest(
            redirect_url='https://google.com.br'
        )
        
        new_url = create_url.execute(data_request)
        get_url = get_url.execute(new_url.object.hash)
        self.assertTrue(isinstance(new_url.object, Url))
        self.assertTrue(isinstance(get_url.object, Url))
        
        