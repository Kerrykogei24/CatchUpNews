from flask import render_template,redirect,url_for
from . import main
from ..request import get_sources


#Views 
@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    source = get_source()
    headlines = get_headlines()
    return render_template('index.html',sources=source, headlines = headlines)
