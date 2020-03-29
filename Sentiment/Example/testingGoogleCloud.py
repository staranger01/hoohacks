'''
simple demo of using Google Api sentiment

https://cloud.google.com/natural-language/docs/sentiment-tutorial


'''




#import matplotlib.pyplot as plt

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


#https://github.com/googleapis/google-cloud-python/issues/5449


'''
you can set your credentials in the terminal, however
i was having problems with that, so seting my credientals in the
script ended up fixing the problem.

below i use the os modul to set the enviroment to the path
the path of the json file that is your api key. you download when you make your account


'''
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\user  1\OneDrive - University of North Carolina at Pembroke\AA_HooHacks\Sentiment\HooHacks-d4edc7bc93e1.json"



client = language.LanguageServiceClient()


text = u"Cows Are So Fucking Godamn Motherfucking AWESOME"

doc = types.Document(
	content=text,
	type=enums.Document.Type.PLAIN_TEXT)
senti = client.analyze_sentiment(document =doc).document_sentiment


print("text: {}".format(text))
print("Sentiment: {}, and {}".format(senti.score, senti.magnitude))