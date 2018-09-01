class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?{}&apiKey={}'
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'


'''
store the news base url inside app.config file.
NB/we use {} to rep sections in the url that will be replaced with actual values.
'''


class ProdConfig(Config):
    pass


class DevConfig( Config):
    Debug = True
