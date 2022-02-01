from email import message
from flask import render_template
from app import app
from .request import get_news_sources, get_news_articles

#Views
@app.route('/')
def index():
  '''
  View root page that returns the index page and its data
  '''
  sources = get_news_sources('sources')
  title = 'Home - Welcome to The best News Website Online'
  return render_template('index.html', title = title, sources = sources)


@app.route('/articles')
def articles():
  articles = get_news_articles()
  title = 'Home - Welcome to The best News Website Online'
  return render_template('articles.html', title = title, articles = articles)
