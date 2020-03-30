'''
version Final Submision
https://cloud.google.com/natural-language/docs/sentiment-tutorial


sentiment anaylis with the google sentiment api

TO_DO / notes:

correctly match timestamps with tweets and their sentiment scores
Does not log properly
in preprocessing; remove any languages not supported by google API to speed up run time
!! Run time currently ~50 mins



'''


import json
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#set path to credenntials
'''
Important:
set the path to your own API JSON File. 

'''
import os 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\user  1\OneDrive - University of North Carolina at Pembroke\AA_HooHacks\Sentiment\HooHacks-d4edc7bc93e1.json"
client = language.LanguageServiceClient()





def getSentimentForAPerson(text_list):
	'''
	You feed in this function a list of strings
	it outputs their sentiment values. Here is a run:

	mock list with same shape as twitter comments 
	play_test = [['cows are very tasty', 'lions are not'],
	['zebras are cool', "doggos are nasty"],
	["the cats out of the bag", "kill your fungus"]]
	print(play_t est)


	f(list):
	Output of mock test
	{'cows are very tasty': (0.8999999761581421, 0.8999999761581421), 
	'lions are not': (-0.30000001192092896, 0.30000001192092896), 
	'zebras are cool': (0.699999988079071, 0.699999988079071), 
	'doggos are nasty': (-0.699999988079071, 0.699999988079071), 
	'the cats out of the bag': (0.0, 0.0), 
	'kill your fungus': (-0.10000000149011612, 0.10000000149011612)}


	TO-DO:
	'''
	text_list_Sentiment=dict()

	for persons_comment in text_list:
		#a_comment = a tweet

		a_comment = str(persons_comment)
		doc = types.Document(
			content=a_comment,
			type=enums.Document.Type.PLAIN_TEXT)
		try:
			sentiment = client.analyze_sentiment(document = doc, encoding_type = "UTF8").document_sentiment
		except:
			# set equal to zero if you run into problems
			# some languages are not supported. 
			# if language is not supported. return value will be integer 0
			# if sentiment is neutral, return value will be 0.0
			class sentiment():
				pass
			sentiment.magnitude = 0
			sentiment.score = 0

		#printing to screen to see
		print(a_comment)
		print(sentiment.magnitude)
		print(sentiment.score)

		#packaging
		text_list_Sentiment.update(
			{a_comment : (sentiment.score, sentiment.magnitude)}
			)
	
	return text_list_Sentiment
				
	





def cleanTwitterData(text_list):
	"""
	text_list in goes the shape {name:[[],[]]......}
	each name mapped to a list of their tweets

	TO-DO:
	clean the twitter data for proccessing.
	figure out

	"""


	list_of_just_handels = [name for name in text_list]
	list_of_just_their_comments = [text_list[name] for name in text_list]


	#test cleaning


	#should remove empty list
	list_of_just_their_comments =[comment for comment in list_of_just_their_comments if not None ] 

	#should remove None from each element
	list_of_just_their_comments = list(map(
		lambda some_list: list(filter(None, some_list)), list_of_just_their_comments
	))

	return list_of_just_handels, list_of_just_their_comments



'''
Return file = {person: {Date:[mag, score], Date:[mag, score]......}}
'''


def analyizeAllThePeopleAndDumpToJSON(file_in, file_out="Names_Matched_with_Sentiment.json"):
	#change file path to location of comments data

	with open(file_in, 'r') as file:
		JSON_Comments=json.loads(file.read())

	list_of_just_handels, list_of_just_their_comments = cleanTwitterData(JSON_Comments)

	person_matched_with_sentiment = dict()

	#loop through each person
	for people in list_of_just_handels:
		sentiments_list =list()
		for comments in list_of_just_their_comments:
			sentiment_for_that_person = getSentimentForAPerson(comments)
			sentiments_list.append(sentiment_for_that_person)
		person_matched_with_sentiment.update({people: sentiments_list})

	#log
	with open(file_out, "w") as file:
		json.dump(person_matched_with_sentiment, file, indent=2)
	return person_matched_with_sentiment








# takes about 50 mins to compile 
# set to true to run
if True:
	print(analyizeAllThePeopleAndDumpToJSON("twitter_Comments_by_Leaders.json", file_out ="v4twitter_Comments_by_Leaders.json"))






def testing_just_ignore():
	#test cleaning
	if False:
		file_in="twitter_Comments_by_Leaders.json"
		with open(file_in, 'r') as file:
			JSON_Comments=json.loads(file.read())

		list_of_just_handels = [name for name in JSON_Comments]
		list_of_just_their_comments = [JSON_Comments[name] for name in JSON_Comments]


		


		#should remove empty list
		list_of_just_their_comments =[comment for comment in list_of_just_their_comments if not None ] 

		#should remove None from each element
		list_of_just_their_comments = list(map(
			lambda some_list: list(filter(None, some_list)), list_of_just_their_comments
		))

		print(list_of_just_their_comments)






	#testing
	file_in = "twitter_Comments_by_Leaders.json"
	with open(file_in, 'r') as file:
		JSON_Comments=json.loads(file.read())

	list_of_just_handels, list_of_just_their_comments = cleanTwitterData(JSON_Comments)
	print(JSON_Comments if False else None)

	if False:
		#Testing with mock entry
		#mock entry
		mock = {
			"person1":[["cow", "i pig", None], ["rooster eats nothing",None, "more cal"], ["nooooo a the fridge",None, "zero cal"]],
			"person2":[["zebras eat nothing", "lll", "kdkd"], [None, "doonouts", "coo doo"]]
		}
		names, sentances = cleanTwitterData(mock)


		print(names)
		print(sentances)

		json.dump(mock, open("mock.json", 'w'))

		print(analyizeAllThePeopleAndDumpToJSON("mock.json", file_out="mock_test_file.json"))

	mock_time_stamps= [
	[.5,.3,.6],[.3,4,6],[33,45,6],
	[5,2,3],[3,5,6]

	]



	if False:
		with open("mock_test_file.json", 'r') as file:
			mock_results = json.loads(file.read())
			print(mock_results)
			masterMatch = dict()

			print("\n\nMathces\n\n")
			for person in mock_results:
				for i in range(len(person)):
					match = dict(zip(
						mock_time_stamps[i],
						mock_results[person][i]))
					print(match, "\n\n")
					masterMatch.update(match)
			print("master Match\n\n",masterMatch)


	print("test")


