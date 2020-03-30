'''
https://cloud.google.com/natural-language/docs/sentiment-tutorial


sentiment anaylis with the google sentiment api
TO_DO:
Clean the input data;
the google api does not accept 'Null'/None data types. Remove these from the list
correctly match timestamps with tweets and their sentiment scores


'''


import json
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#set path to credenntials
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
		for that_persons_comment in persons_comment:
			
			a_comment = that_persons_comment.encode('utf-8')
			doc = types.Document(
				content=a_comment,
				type=enums.Document.Type.PLAIN_TEXT)
			sentiment = client.analyze_sentiment(document = doc).document_sentiment

			#testing
			print(that_persons_comment)
			print(sentiment.magnitude)
			print(sentiment.score)

			#packaging
			text_list_Sentiment.update(
				{that_persons_comment : (sentiment.score, sentiment.magnitude)}
				)
	
	return text_list_Sentiment
				



def analyizeAllThePeopleAndDumpToJSON(file_in):
	#change file path to location of comments data

	with open(file_in, 'r') as file:
		JSON_Comments=json.loads(file.read())

	list_of_just_their_comments = [JSON_Comments[name] for name in JSON_Comments]
	list_of_just_handels = [name for name in JSON_Comments]

	person_matched_with_sentiment = dict()

	#loop through each person
	for people in list_of_just_handels:
		sentiments_list =list()
		for comments in list_of_just_their_comments:
			sentiment_for_that_person = getSentimentForAPerson(comments)
			sentiments_list.append(sentiment_for_that_person)
		person_matched_with_sentiment.update({people: sentiments_list})

	#log
	with open("The_People_with_sentiment.json", "w") as file:
		json.dump(person_matched_with_sentiment, file, indent=2)
	return person_matched_with_sentiment


	

		




print(analyizeAllThePeopleAndDumpToJSON("twitter_Comments_by_Leaders.json"))





def cleanTwitterData(text_list):
	"""
	TO-DO:
	clean the twitter data for proccessing.
	figure out

	"""
	return None



'''
Return file = {person: {Date:[mag, score], Date:[mag, score]......}}
'''
