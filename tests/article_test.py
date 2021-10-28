import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
      Test Class to test the behaviour of the Article class
    '''
    def setUp(self):
        '''
         Set up method that will run before every Test
        '''
        self.new_article = Article('dummy_article','jane doe','https://s.image.com','2019-10-12T03:11:28Z',"http://abc.com",'abc-news')


    def test_article_instance(self):
        print(self.new_article.__class__)
        self.assertTrue((isinstance(self.new_article,Article)))

if __name__ == '__main__':
      unittest.run()
    # manage.run()