from app import app
import urllib.request,json
from .models import news


News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

base_url = app.config['BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    # get_news_url = "https://newsapi.org/v2/sources?&apiKey=f704406e04b249f7b6e18849f7bb114c"
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results

def process_results(sources_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    sources_results = []
    for source_item in sources_list:
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        # poster = news_item.get('poster_path')
        # vote_average = news_item.get('vote_average')
        # vote_count = news_item.get('vote_count')

        if poster:
           sources_object = Sources(name,description,url)
            sources_results.append(sources_object)

    return sources_results