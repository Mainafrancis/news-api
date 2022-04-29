import urllib.request, json
from .models import News_Article

api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = (news_results_list)


    return news_results


def process_rsults(news_list):
    news_results = [] 
    for news_item in news_list:
        title = news_item.get('title')
        publishedAt = news_item.get('publishedAt')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        url = news_item.get('url')   
        if urlToImage:

            news_object = News_Article(title, description, url, urlToImage, publishedAt)
            news_results.append(news_object)

    return news_results            

