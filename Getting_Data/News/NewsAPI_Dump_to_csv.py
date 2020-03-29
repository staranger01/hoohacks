import requests
import json
import pandas as pd
'''
Getting news articles regarding corona from NewsAPI.com


'''

def getArticlesFromNewsAPI(searchFor="corona"):
	'''
	gets and dumps news paper articles related to corona into a json file
	the searchFor is what youd like to search for. default is set to corona
	'''
	page = requests.get("http://newsapi.org/v2/everything?q="+searchFor+"&from=2020-02-28&sortBy=publishedAt&apiKey=2b683fa275da4e7ead86f9e54116aef0").text
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

'''
0	 1		2....
title
authors
descriptions
urls
content

'''





file = json.loads(open("NEWS_ARTICALS.json", 'r').read())
auth, titl, des, urls, cont = sortNewsAPI(file)


#data is the columns
#index is the index
D = pd.DataFrame(
	data = [titl, auth, des, urls, cont],
	index = ["title", "authors", "descriptions", "URL", "content"]
	)

D.to_csv("NewsAPI.csv")


print(D)