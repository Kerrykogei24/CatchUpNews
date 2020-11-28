from flask import render_template
from app import app



#views

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title)