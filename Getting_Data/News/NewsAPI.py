import requests
import json
'''
Getting news articles regarding corona from NewsAPI.com


'''

def getArticlesFromNewsAPI():
	'''
	gets and dumps news paper articles related to corona into a json file
	'''
	page = requests.get("http://newsapi.org/v2/everything?q=corona&from=2020-02-28&sortBy=publishedAt&apiKey=2b683fa275da4e7ead86f9e54116aef0").text
	result = json.loads(page)
	with open("NEWS_ARTICALS.json", 'w') as file:
		json.dump(result['articles'], file, indent=2)
	return None

def sortNewsAPI(articles):
	"""
	input a jsonfile named articles where corona related news articles are stored.

	"""
	authors = [art["title"] for art in articles]
	titles = [art["title"] for art in articles]
	descriptions = [art["description"] for art in articles]
	URLs = [art["url"] for art in articles]
	content = [art["content"] for art in articles]
	return authors, titles, descriptions, URLs, content





file = json.loads(open("NEWS_ARTICALS.json", 'r').read())
auth, titl, des, urls, cont = sortNewsAPI(file)
for art in enumerate(titl):
	print(art)
