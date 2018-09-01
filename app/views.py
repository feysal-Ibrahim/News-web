from flask import render_template
from app import app
from.request import get_news #import get_news function from request module
from .request import get_article

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting  news sources
    news_sources = get_news('sources')
    print(news_sources)
    title ='Home - We Provide the latest News'
    return render_template('index.html', title=title, sources=news_sources)

@app.route('/news/<int:id>')
def news(id):
    articles_list = get_article('article')
    print('article')
    return render_template('article.html', id=id, article=articles_list)