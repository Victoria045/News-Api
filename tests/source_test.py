import unittest
from app.models import Source


class SourceArticleTest(unittest.TestCase):
    '''
      Test Class to test the behaviour of the Source class
    '''
    def setUp(self):
        '''
         Set up method that will run before every Test
        '''
        self.new_source = Source('abc-news','Abc News','A world class news channel')
        

    def test_instance(self):

        print(self.new_source.__class__)
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
      unittest.main()
    # manage.run()