from email import message
from flask import render_template
from app import app
from .request import get_news_sources

#Views
@app.route('/')
def index():
  '''
  View root page that returns the index page and its data
  '''
  sources = get_news_sources('sources')
  title = 'Home - Welcome to The best News Website Online'
  return render_template('index.html', title = title, sources = sources)
  # return render_template('index.html', title = title)
