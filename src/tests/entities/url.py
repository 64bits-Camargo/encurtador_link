import uuid

import unittest

from entities import Url, DtoUrl


class TestUrl(unittest.TestCase):
    def test_to_be_instance_of(self):
        hash = uuid.uuid4()
        data =  DtoUrl(
            id=0, 
            short_url='http://127.0.0.1:500/{hash}'.format(hash=hash), 
            redirect_url= 'https://www.google.com',
            hits=1,
            hash=hash
        )
        
        self.assertTrue(isinstance(Url(data), Url))