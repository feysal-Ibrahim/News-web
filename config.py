import os
class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?&apiKey={}'
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SECRET_KEY = os.environ.get ( 'SECRET_KEY' )
    KEY =os.environ.get('NEWS_API_KEY')

'''
store the news base url inside app.config file.
NB/we use {} to rep sections in the url that will be replaced with actual values.
'''


class ProdConfig(Config):
    pass


class DevConfig( Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
