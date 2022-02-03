class NewsArticle:
  '''
  News article class
  '''
  def __init__(self, author, title, description, url, urlToImage, publishedAt, content):
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.publishedAt = publishedAt
    self.content = content


class NewsSource:
  '''
  News source class
  '''
  def __init__(self, id, name, url):
    self.id = id
    self.name = name
    self.url = url
