
from app import app
import urllib.request,json
from .models import source,news
from .models import news
Source = source.Source
News = news.News

# getting api key
api_key = app.config['SOURCE_API_KEY']
# getting the news base url

base_url = app.config['SOURCE_API_BASE_URL']

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        source_results = get_source_response

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_sources(source_results_list)

    return source_results
def process_sources(source_list):
    '''
    Function that processes the source result and transform them to a list of objects
    
    Args:
       source_list: A list of dictionaries that contain newz details
    Returns:
       source_results:A list of objects
    '''
    source_results =[]
    for source_item in source_list:
       
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        category = source_item.get('category')
        if source:
            source_object = Source(id,name,description,category)
            source_results.append(source_object)
    return source_results

def get_articles(source):
	'''
	Function that gets the json response to our url request
	'''
	get_articles_url = articles_base_url.format(source,api_Key)

	with urllib.request.urlopen(get_articles_url,data=None) as url:
		get_articles_data = url.read()
		get_articles_response = json.loads(get_articles_data)
		articles_results = None

		if get_articles_response['articles']:
			articles_results_list = get_articles_response['articles']
			articles_results = process_articles(articles_results_list)

	return articles_results

def process_articles(articles_results):
	'''
	Function  that processes the articles result and transform them to a list of Objects
	Args:
	    articles_results: A list of dictionaries that contain articles details
	Returns :
	    articles_list: A list of articles objects
	'''
	articles_list = []
	for article_item in articles_results:
		author = article_item.get('author')
		title = article_item.get('title')
		description = article_item.get('description')
		url = article_item.get('url')
		image = article_item.get('urlToImage')
		date = article_item.get('publishedAt')

		if date and author and image:
			article_object = Article(author,title,description,url,image,date)
			articles_list.append(article_object)

	return articles_list