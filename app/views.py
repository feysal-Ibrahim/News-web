from flask import render_template
from  app import app
from.request import get_news #import get_news function from request module

@app.route('/')
def index():
    #getting  news sources
    news_sources = get_news('sources')
    print(news_sources)
    title ='Home - We Provide the latest News'
    return render_template('index.html', title=title, sources=news_sources)

@app.route('/news/<int:id>')
def news(id):
  return render_template('news.html', id=id)