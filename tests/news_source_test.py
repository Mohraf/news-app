import unittest
from ..app.models import news_source
NewsSource = news_source.NewsSource


class NewsSourceTest(unittest.TestCase):
  '''
  Test class to check the behaviour of News Source
  '''

  def setUp(self):
    self.news_source = NewsSource(
      "reuters",
      "Reuters"
    )
  
  def test_instance(self):
    self.assertTrue(isinstance(self.news_source, NewsSource))


if __name__ == '__main__':
  unittest.main()
