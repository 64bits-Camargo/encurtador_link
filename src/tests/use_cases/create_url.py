import unittest

from entities import Url
from repositories import InMemoryRepository
from use_cases import CreateUrlUseCase, CreateUrlRequest


class TestUrl(unittest.TestCase):
    def test_create_url(self):
        url_repository = InMemoryRepository()
        create_url = CreateUrlUseCase(url_repository)
        
        data_request = CreateUrlRequest(
            redirect_url='https://google.com.br'
        )
        
        new_url = create_url.execute(data_request)
        
        self.assertTrue(isinstance(new_url.object, Url))