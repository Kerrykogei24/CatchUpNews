from app import app
import urllib.request,json
from .models import news


News = news.News

# Getting api key
api_key = app.config[' NEWS_API_KEY']

base_url = app.config['BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in movie_list:
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        # poster = news_item.get('poster_path')
        # vote_average = news_item.get('vote_average')
        # vote_count = news_item.get('vote_count')

        if poster:
            news_object = Movie(name,description,url)
            news_results.append(news_object)

    return news_results