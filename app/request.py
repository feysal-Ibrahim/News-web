from app import app  # this is the flask app instance
import urllib.request, \
    json  # this help us create a connection to our API URL and send a request and json modules that will format the JSON response to a Python dictionary.
from .models import news

News = news.News

api_key = app.config['NEWS_API_KEY']  # accessing our api key by accessing our config object

base_url = 'https://newsapi.org/v2/sources&{}?&apiKey={}'
# base_url = app.config["NEWS_API_BASE_URL"]


def get_news(sources):
    # get_news_url = base_url.format(sources,api_key)

    dumb_url = 'https://newsapi.org/v2/'+ sources +'?&apiKey=32af9c23bb824ff68655f516b53d7e6d'


    with urllib.request.urlopen(dumb_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources = None

        if get_news_response['sources']:
            news_sources_list = get_news_response['sources']
            news_sources = process_sources(news_sources_list)

    return news_sources


def process_sources(sources_list):
    news_sources = []
    for news_item in sources_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        language = news_item.get('language')
        category = news_item.get('category')
        country = news_item.get('country')
        news_object = News(id,name,description,url,language,category, country)
        news_sources.append(news_object)


    return news_sources


