'''
https://cloud.google.com/natural-language/docs/sentiment-tutorial


sentiment anaylis with the google sentiment api



'''


import json
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#set path to credenntials
import os 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\user  1\OneDrive - University of North Carolina at Pembroke\AA_HooHacks\Sentiment\HooHacks-d4edc7bc93e1.json"
client = language.LanguageServiceClient()


#change file path to location of comments data
with open(r"C:\Users\user  1\OneDrive - University of North Carolina at Pembroke\AA_HooHacks\Data\Getting_Data\Leaders_Social_Media\twitter_Comments_by_Leaders.json", 'r') as file:
	JSON_Comments=json.loads(file.read())

list_of_just_their_comments = [JSON_Comments[name] for name in JSON_Comments]
list_of_just_handels = [name for name in JSON_Comments]

#print(list_of_just_their_comments)

#mock list with same shape as twitter comments 
play_test = [['cows are very tasty', 'lions are not'],
['zebras are cool', "doggos are nasty"],
["the cats out of the bag", "kill your fungus"]]
print(play_test)


def getSentimentForAPerson(text_list):
	'''
	you give this fuction a list of strings and it outputs their sentiment score and magnitude
	TO-DO:
	Test function to see if produces desired output


	'''
	text_list_Sentiment_Score=list()
	text_list_Sentiment_magnitude=list()

	for persons_comment in text_list:
		for that_persons_comment in persons_comment:
			a_comment = that_persons_comment.encode('utf-8')
			doc = types.Document(
				content=a_comment,
				type=enums.Document.Type.PLAIN_TEXT)
			sentiment = client.analyze_sentiment(document = doc).document_sentiment
			text_list_Sentiment_magnitude.append(sentiment.magnitude)
			text_list_Sentiment_Score.append(sentiment.score)



		

	return None


def cleanTwitterData(text_list):
	"""
	TO-DO:
	clean the twitter data for proccessing.
	figure out

	"""
	return None


getSentimentForAPerson(play_test)