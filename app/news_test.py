import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,'Sys-con.com','Cryptohopper Just Hit 100k Users on Their Trading Platform',"http://businesswire.sys-con.com/node/4376242",'Cryptohopper just announced that it hit 100k users on their trading platform. In little over a year and a half, this staggering amount of people have joined the platform, enticed by the promise to invest completely automatically. When you sign up and configur…',null,2019-02-15T14:03:04Z,'Cryptohopper just announced that it hit 100k users on their trading \r\n platform. In little over a year and a half, this staggering amount of \r\n people have joined the platform, enticed by the promise to invest \r\n completely automatically. When you sign up and… ')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,news))


if __name__ == '__main__':
    unittest.main()