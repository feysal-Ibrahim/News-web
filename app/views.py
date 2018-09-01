from flask import render_template
from app import app
from.request import get_news,get_article #import get_news function from request module

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

@app.route('/news/<id>')
def news(id):
    '''
       View movie page function that returns the movie details page and its data
       '''
    articles_list = get_article('article')
    print('article')
    return render_template('article.html', id=id, article=articles_list)