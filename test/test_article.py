import unittest
from app.models import News_Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = News_Article('title', 'description', 'url', 'urlToImage', 'publishedAt')
        