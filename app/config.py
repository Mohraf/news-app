from distutils.debug import DEBUG

from instance.config import NEWS_API_KEY


class Config:
  '''
  General configuration parent class
  '''
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/{}?apiKey={}'


class DevConfig(Config):
  '''
  Development configuration child class
  
  Args:
    Config: The Parent configuration class with general config settings
  '''
  DEBUG = True


class ProdConfig(Config):
  '''
  Production configuration child class

  Args:
    Config: The Parent configuration class with general config settings
  '''
  pass
