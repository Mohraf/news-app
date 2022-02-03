import unittest
from ..app.models import news_article
NewsArticle = news_article.NewsArticle


class NewsArticleTest(unittest.TestCase):
  def setUp(self):
    self.news_article = NewsArticle(
      "Amos",
      "Progmamers Life",
      "day to day life of a coder",
      "https://codetolife.com",
      "https://urltoimage.com",
      "2022-01-30T08:25:00Z",
      "TAIPEI, Jan 30 (Reuters) - Taiwan Vice President William Lai used his final day in the United States to repeat an accusation that China blocked the island from obtaining COVID-19 vaccines last year"
    )
  

  def test_instance(self):
    self.assertTrue(isinstance(self.news_article, NewsArticle))


if __name__ == '__main__':
  unittest.main()