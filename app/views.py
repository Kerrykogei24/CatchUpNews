from flask import render_template
from app import app



#views

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

# Getting popular movie
    popular_news = get_news('popular news')
    print(popular_news)
    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('index.html',title=title, sources = popular_news)