from app import app
# import requests
import urllib.request, json

from app.news_article_test import NewsArticle
from app.news_source_test import NewsSource

from .models import news_article, news_source

NewsArticle = news_article.NewsArticle
NewsSource = news_source.NewsSource

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']
articles_url = app.config['ARTICLES_API_BASE_URL']


def get_news_sources(source):
  get_news_url = base_url.format(source, api_key)

  # return sources_results
  with urllib.request.urlopen(get_news_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

    sources_results = None

    if get_sources_response['sources']:
      sources_results_list = get_sources_response['sources']
      sources_results = process_sources_results(sources_results_list)
  
  return sources_results



def process_sources_results(news_list):
  '''
  Function that processes the movie result and transform them to a list of Objects

  Args:
    movie_list: A list of dictionaries that contain the movie details

  Retunrs:
    movie_results: A list of movie ogjects
  '''
  news_sources_results = []
  for news_item in news_list:
    id = news_item.get('id')
    name = news_item.get('name')
    url = news_item.get('url')

    if id:
      source_object = NewsSource(id,name,url)
      news_sources_results.append(source_object)
  
  return news_sources_results


def get_news_articles():
  get_news_articles_url = articles_url.format(api_key)

  # return articles_results
  with urllib.request.urlopen(get_news_articles_url) as url:
    get_articles_data = url.read()
    get_articles_response = json.loads(get_articles_data)

    articles_results = None

    if get_articles_response['articles']:
      articles_results_list = get_articles_response['articles']
      articles_results = process_sources_results(articles_results_list)
  
  return articles_results


def process_sources_results(articles_list):
  news_articles_results = []
  for articles_item in articles_list:
    author = articles_item.get('author')
    title = articles_item.get('title')
    description = articles_item.get('description')
    url = articles_item.get('url')
    urlToImage = articles_item.get('urlToImage')
    publishedAt = articles_item.get('publishedAt')
    content = articles_item.get('content')

    if id:
      article_object = NewsArticle(author,title,description,url,urlToImage,publishedAt,content)
      news_articles_results.append(article_object)
  
  return news_articles_results