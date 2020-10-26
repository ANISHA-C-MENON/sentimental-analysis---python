import glob, os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('punkt')
import csv
import pandas as pd
# Import library for web 
# scrapping 
from bs4 import BeautifulSoup as SOUP 
import re 
import requests 



def sentiment(text):

	sid = SentimentIntensityAnalyzer()
	com = 0
	sents = nltk.sent_tokenize(text)
	for sentence in sents:
		ss = sid.polarity_scores(sentence)
		com = com + ss['compound']


	sentiment_score = (float(com) / len(sents))
	rounded = round(sentiment_score, 2)
	# print('sentiment score:', rounded)

	if (sentiment_score < 0.0):
		feedback = "negative"
	elif (sentiment_score > 0.1):
		feedback = "positive"
	else:
		feedback = "neutral"


	if(rounded<=0.8 and rounded>0.6):
		emotion='very happy'
	elif(rounded<=1.0 and rounded>0.8):
		emotion='very enthusiastic'
	elif(rounded<=0.6 and rounded>0.4):
		emotion='surprised'
	elif(rounded<=0.4 and rounded>0.2):
		emotion='enjoyments'
	elif(rounded<=0.2 and rounded>0.0):
		emotion='anticipations'
	elif(rounded<=0.0 and rounded>-0.4):
		emotion='feard'
	elif(rounded<=-0.4 and rounded>-0.6):
		emotion='sadness'
	elif(rounded<=-0.6 and rounded>-1.0):
		emotion='anger'
	elif(rounded==0):
		emotion='happy'
	else:
		emotion='not defined'
		

	return rounded, emotion

def get_movie(emotion): 
	details = {}
	
	# IMDb Url for Drama genre of 
	# movie against emotion Sad 
	if(emotion == "sad"): 
		urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

	

	# IMDb Url for Family genre of 
	# movie against emotion Anger 
	elif(emotion == "anger"): 
		urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Thriller genre of 
	# movie against emotion Anticipation 
	elif(emotion == "anticipation"): 
		urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Sport genre of 
	# movie against emotion Fear 
	elif(emotion == "fear"): 
		urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Thriller genre of 
	# movie against emotion Enjoyment 
	elif(emotion == "enjoyment"): 
		urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
	elif(emotion == "enthusiastic"): 
		urlhere = 'https://www.imdb.com/search/title/?genres=comedy&title_type=feature&sort=moviemeter, asc'

	

	# IMDb Url for Film_noir genre of 
	# movie against emotion Surprise 
	elif(emotion == "surprise"): 
		urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
	elif(emotion == "happy"):
		urlhere='https://www.imdb.com/list/ls060352216/,asc'
	# HTTP request to get the data of 
	# the whole page 
	response = requests.get(urlhere) 
	data = response.text 

	# Parsing the data using 
	# BeautifulSoup 
	soup = SOUP(data, "html.parser") 
	# print(soup.prettify())

	# Extract movie titles from the 
	# data using regex 
	data = soup.find_all("div", attrs = {"class": "lister-item-content"}) 
	i = 0
	for d in data:
		results = {}
		results['Name'] = d.a.contents[0]
		results['Genre'] = d.find("span",{"class":"genre"}).contents[0]	
		details[i] = results
		i = i+1
		
	return details




from flask import Flask,request

app = Flask(__name__)

@app.route('/<search>')
def home(search):
	sent = 0
	emotion = ""
	sent,emotion = sentiment(search)
	# print(sent, emotion)
	datas = get_movie(emotion)
	return datas
if __name__ == "__main__":
    app.run()
