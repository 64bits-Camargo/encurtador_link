import uuid

import unittest

from src.entities.url import Url, DtoUrl


class TestUrl(unittest.TestCase):
    def test_to_be_instance_of(self):
        data =  DtoUrl(
            id=0, 
            short_url='http://127.0.0.1:500/{hash}'.format(hash=uuid.uuid4()), 
            redirect_url= 'https://www.google.com',
            hits=1
        )
        
        self.assertTrue(isinstance(Url(data), Url))