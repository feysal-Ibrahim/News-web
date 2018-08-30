from flask import render_template
from  app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news/<int:id>')
def news(id):
  return render_template('news.html',id = id) 