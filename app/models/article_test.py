import unittest #import the unittest module
from app.models.articles import Article


class NewsTest(unittest.TestCase):
    '''
    test Class to test the behaviour of the calss
    '''


    def setUp(self): #setup method that will run before every test


        self.new_article = Article('12','github','is good','http://abcnews.go.com','people','www.image.com', 'date','feysal')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))


if __name__ == '__main__':
    unittest.main()