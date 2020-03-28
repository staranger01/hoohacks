from bs4 import * 
import requests
import json

def getListOfLeadersTwitterHandels(output_file = "List_Of_World_Leader_Twitter_Handels.txt"):
	#https://twiplomacy.com/ranking/the-50-most-followed-world-leaders-in-2019/
	'''
	this website give a list of most popular world leaders and their twitter handels.
	can use this to get their responces to corona outbreak


	'''
	try:
		page = requests.get("https://twiplomacy.com/ranking/the-50-most-followed-world-leaders-in-2019/").text
	except:
		getListOfLeadersTwitterHandels()
	soup = BeautifulSoup(page, 'lxml')
	list_Of_handels=soup.find_all("div", class_ = "ranking-user-name")	
	complete_handel_list = list(handle.string.strip("\n").strip() for handle in list_Of_handels)
	del complete_handel_list[0] # "removes the false entry 'Account' from list"
	

	#dump to file
	#format file better
	"""with open(output_file, 'w+') as file:
					file.write(str(complete_handel_list))"""

	return complete_handel_list






def getTwitterComments(userName):
	'''
	function gets their comments from their twitter page

	TODO- 
	Make it go to the next page and get more tweets
	Get timestamp with tweets

	'''
	try: 
		page = requests.get('https://twitter.com/'+userName,
			headers = {'User-Agent': 'Mozilla/5.0'}).text
	except:
		getTwitterComments(userName)
	soup = BeautifulSoup(page, "lxml")



	tweets_unclean = soup.find_all("li", {"data-item-type": "tweet"})
	tweets = list(tweet.p.string for tweet in tweets_unclean) # tweets on this pageO

	#TO-DO: Get date stamp for tweets
	#tweets_unclean[0].find("small", class_ = "time").find()
	#get 
	#next_page = soup.find("div", {"class": "stream-container"})["data-min-position"]



	return tweets




	




	
def getAllMajorTwitterStatements():
	'''
	simple loop through and dump

	'''
	theirNames = getListOfLeadersTwitterHandels()
	theirComments = list()
	
	for name in theirNames:
		comment = getTwitterComments(name)
		theirComments.append(comment)
		print(comment)

	commentData = dict(zip(theirNames, theirComments))
	with open("twitter_Comments_by_Leaders.json", "w") as file:
		json.dump(commentData, file, indent=2)





