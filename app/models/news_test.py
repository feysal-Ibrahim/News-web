import unittest #import the unittest module
from app.model import News
News = News.news

class NewsTest(unittest.TestCase):
    '''
    test Class to test the behaviour of the calss
    '''


    def setUp(self): #setup method that will run before every test


        self.new_news = News('abc-news', 'abc news', 'your trusted news', 'http://abcnews.go.com', 'english','us', 'sport')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))


if __name__ == '__main__':
    unittest.main()
