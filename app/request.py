from urllib import response
from app import app
import requests

from app.news_article_test import NewsArticle
from app.news_source_test import NewsSource

from .models import news_article, news_source

NewsArticle = news_article.NewsArticle
NewsSource = news_source.NewsSource

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']


def getNews(source):
  get_news_url = base_url.format(source, api_key)

  response = requests.get(get_news_url)

  print (response.json)

  return (response.json)