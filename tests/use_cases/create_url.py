import unittest

from src.entities.url import Url
from src.repositories import InMemoryRepository
from src.use_cases.create_url import CreateUrlUseCase, CreateUrlRequest


class TestUrl(unittest.TestCase):
    def test_create_url(self):
        url_repository = InMemoryRepository()
        create_url = CreateUrlUseCase(url_repository)
        
        data_request = CreateUrlRequest(
            redirect_url='https://google.com.br'
        )
        
        new_url = create_url.execute(data_request)
        
        
        self.assertTrue(isinstance(new_url.object, Url))