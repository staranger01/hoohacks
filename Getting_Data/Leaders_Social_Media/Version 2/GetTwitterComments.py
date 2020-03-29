from bs4 import * 
import requests
import json
import pandas as pd

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
	
	Had trouble combining the timestamps with its tweets

	the function returns a list of tweets and timestamps
	each index should match

	'''
	try: 
		page = requests.get('https://twitter.com/'+userName,
			headers = {'User-Agent': 'Mozilla/5.0'}).text
	except:
		getTwitterComments(userName)
	soup = BeautifulSoup(page, "lxml")
	tweets_unclean = soup.find_all("li", {"data-item-type": "tweet"})
	tweets = list(tweet.p.string for tweet in tweets_unclean) # tweets on this pageO
	tweets_timeStamps = [
	tweet.find("small", class_ ="time").a.attrs['title'].split("-")[1].strip() for tweet in tweets_unclean]

	#TO-DO: Get date stamp for tweets
	#tweets_unclean[0].find("small", class_ = "time").find()
	#get 
	#next_page = soup.find("div", {"class": "stream-container"})["data-min-position"]



	return tweets, tweets_timeStamps





	
def getAllMajorTwitterStatements():
	'''
	simple loop through and dump

	'''
	theirNames = getListOfLeadersTwitterHandels()
	theirComments = list()
	theirComments_timeStamp=list()
	
	for name in theirNames:
		try:
			comment, timeStamp = getTwitterComments(name)
			if comment == None:
				pass
			theirComments.append(comment)
			theirComments_timeStamp.append(timeStamp)
			print(comment)
		except:
			pass

		commentData = dict(zip(theirNames, theirComments))
		with open("twitter_Comments_by_Leaders.json", "w") as file:
			json.dump(commentData, file, indent=2)
		with open("Just_The_timestamps.json", "w") as file:
			json.dump(theirComments_timeStamp, file, indent=2)

getAllMajorTwitterStatements()
def dumpToCSV():

	with pd.ExcelWriter("LeaderTweets.xlsx") as writer:
		for people in getListOfLeadersTwitterHandels():
			t, ts = getTwitterComments(people)
			D = pd.DataFrame(data = [ts, t])
			D.to_excel(writer, people)


def getTwitterCommentsVersionTwo(userName, n_of_pages):
	'''
	userName= "@realDonaldTrump" # Example 

	This fuction does not seem to work properly. i quit on it
	the diffrence between version one and versoin two is that 
	version two will try and retrive ten more pages of tweets

	'''

	# shape = {time: tweet, ........ time: tweet}
	return_dictionary = dict()


	try: 
		page = requests.get('https://twitter.com/'+userName,
			headers = {'User-Agent': 'Mozilla/5.0'}).text
	except:
		getTwitterComments(userName)
	soup = BeautifulSoup(page, "lxml")



	tweets_unclean = soup.find_all("li", {"data-item-type": "tweet"})
	tweets = list(tweet.p.string for tweet in tweets_unclean) # tweets on this pageO

	print("tweets1:\n\n",tweets)


	#users_Full_name = examp.find_all('b')[0].string doesnt work!


	tweets_timeStamp = [
	tweet.find("small", class_ ="time").a.attrs['title'].split("-")[1].strip() for tweet in tweets_unclean
	]



	return_dictionary.update(
		dict(zip(tweets_timeStamp, tweets))
		)

	#testing
	print("First Dict: \n\n")
	print(return_dictionary)



	#get more tweets from the user
	for i in range(n_of_pages):

		further_down_the_page = soup.find("div", {"class": "stream-container"})["data-min-position"]
		try:
			link = "https://twitter.com/i/profiles/show/"+userName+"/timeline/tweets?include_available_features=1&include_entities=1&max_position="+further_down_the_page+"&reset_error_state=false"
			resp = requests.get(link).text
			what_it_gives_you = json.loads(resp)

			if(what_it_gives_you["has_more_items"] == False):
				pass
				break

			#add new stuff to previous list of tweets
			#essentially just a copy and paste of above format
			new_stuff = what_it_gives_you["items_html"]
			new_soup = BeautifulSoup(new_stuff, 'lxml')
			new_tweets_unclean = new_soup.find_all("li", {"data-item-type": "tweet"})
			new_tweets = [tweet.p.string for tweet in tweets_unclean]
			new_tweets_timeStamps = [
			tweet.find("small", class_ ="time").a.attrs['title'].split("-")[1].strip() for tweet in new_tweets_unclean]
			print("NewSets of tweets\n\n",new_tweets)
			print("newtimestamps", new_tweets_timeStamps)
			return_dictionary.update(
				dict(zip(new_tweets_timeStamps, new_tweets)))

		except Exception:
			pass
		print(i)


	print("2nd  Dict: \n\n")
	print(return_dictionary )	













#Testing


'''
Issues:
The version2 to get more does not work






'''

'''
import threading

def f1():
	t1, ts1, rd1 = getTwitterComments("@realDonaldTrump")
	print("Tweets:", t1)
	print("\n\n")
	print("Tweets times :", ts1)
	print("\n\n")
	print("the dictionary:", rd1)
	print("\n\n")
	print(len(t1), len(ts1))
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

#getTwitterCommentsVersionTwo("@realDonaldTrump", 10)

if __name__ == '__main__':
	thrd_1 = threading.Thread(target=f1)
	thrd_2 = threading.Thread(target = getTwitterCommentsVersionTwo,
		args = ("@realDonaldTrump", 10))
	thrd_1.start()
	thrd_2.start()
	thrd_1.join()
	thrd_2.join()

'''
