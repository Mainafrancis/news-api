import unittest
from app.models import News_source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_source = News_source('news_id', 'name')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,News_source))    
