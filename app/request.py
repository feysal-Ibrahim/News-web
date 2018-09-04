import urllib.request, json  # this help us create a connection to our API URL and send a request and json modules that will format the JSON response to a Python dictionary.
from .models import News, Article



# Getting api key
api_key = None
# Getting the source base url
base_url = None

def configure_request(app):
    global api_key, news_url,source_url
    api_key = app.config['KEY']
    news_url = app.config['NEWS_API_BASE_URL']
    source_url=app.config['ARTICLE_API_BASE_URL']


# sources_base_url = 'https://newsapi.org/v2/sources&{}?&apiKey={}'
article_base_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
news_base_url = 'https://newsapi.org/v2/sources?&apiKey={}'
api_key = '32af9c23bb824ff68655f516b53d7e6d'  # accessing our api key by accessing our config object


# base_url = app.config["NEWS_API_BASE_URL"]


def get_news():
    # get_news_url = base_url.format(sources,api_key)

    # wtf_url = 'https://newsapi.org/v2/' + sources + '?&apiKey=32af9c23bb824ff68655f516b53d7e6d'
    # https: // newsapi.org / v2 / everything?& apiKey =
    get_news_details_url = news_url.format (api_key)
    with urllib.request.urlopen(get_news_details_url) as url:
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
        id = news_item.get ( 'id' )
        name = news_item.get ( 'name' )
        description = news_item.get ( 'description' )
        url = news_item.get ( 'url' )
        language = news_item.get ( 'language' )
        category = news_item.get ( 'category' )
        country = news_item.get ( 'country' )
        news_object = News( id, name, description, url, language, category, country )
        news_sources.append ( news_object )
    return news_sources



def get_article(id):
    get_article_details_url = article_base_url.format(id,api_key)
    with urllib.request.urlopen(get_article_details_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        news_articles = None

        if get_article_response['articles']:
            news_articles_list = get_article_response['articles']
            news_articles = process_articles(news_articles_list)

    return news_articles


def process_articles(articles_list):
    news_articles = []
    for article_item in articles_list:
        name = article_item.get ( 'name' )
        description = article_item.get ('description')
        url = article_item.get ('url')
        title = article_item.get ( 'title' )
        urlToImage = article_item.get ( 'urlToImage' )
        date = article_item.get ('publishedAt' )
        author = article_item.get ('author')
        articles_object=Article(name, description, url, title, urlToImage, date, author )
        news_articles.append(articles_object)

    return news_articles
