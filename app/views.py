from flask import render_template
from app import app
from .request import get_sources



#views

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

# Getting popular movie
    business_sources = get_sources('business')
    print(business_sources)
    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('index.html',title=title, business = business_sources)