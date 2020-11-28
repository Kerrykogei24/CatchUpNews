from flask import render_template,redirect,url_for
from . import main
from ..request import get_sources


#Views 
@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    source = get_sources()
    headlines = get_headlines()
    return render_template('index.html',sources=source, headlines = headlines)
    
@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id )
