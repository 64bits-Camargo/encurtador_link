import unittest

from entities import Url
from repositories import InMemoryRepository
from use_cases import GetUrlUseCase, GetUrlRequest
from use_cases import CreateUrlUseCase, CreateUrlRequest


class TestUrl(unittest.TestCase):
    def test_get_url(self):
        url_repository = InMemoryRepository()
        create_url = CreateUrlUseCase(url_repository)
        get_url = GetUrlUseCase(url_repository)
        
        data_create_request = CreateUrlRequest(
            redirect_url='https://google.com.br'
        )
        
        new_url = create_url.execute(data_create_request)
        
        data_get_request = GetUrlRequest(
            hash=new_url.object.hash
        )
        
        get_url = get_url.execute(data_get_request)
        self.assertTrue(isinstance(new_url.object, Url))
        self.assertTrue(isinstance(get_url.object, Url))
        
        