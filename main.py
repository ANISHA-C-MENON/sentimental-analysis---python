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
import requests as HTTP 


os.chdir("/home/kadeeja/Desktop/sample")# changing working directory as required path

with open('sentiment.csv', 'w',encoding='cp1252') as file:
    writer = csv.writer(file, delimiter = ',', lineterminator = '\n',)# create a csv file to store result
    writer.writerow(["text",'sentiment score',"feedback"])

    for item in glob.glob("*.txt"):  # getting all text files from given directory
        print(file)

        with open(item, 'r') as f: # reading text file
            lines = f.read()
            sents = nltk.sent_tokenize(lines)

        sid = SentimentIntensityAnalyzer()
        com = 0
        # sentiment analysis 
        for sentence in sents:
            print(sentence)
            ss = sid.polarity_scores(sentence)
            
            com = com + ss['compound']

        sentiment_score = (float(com) / len(sents))
        rounded = round(sentiment_score, 2)
        print('sentiment score:', rounded)

        if (sentiment_score < 0.0):
            feedback = "negative"
        elif (sentiment_score > 0.1):
            feedback = "positive"
        else:
            feedback = "neutral"

            #  csv file to store result
        writer.writerow([item, rounded, feedback])

if(rounded<=0.8 and rounded>0.6):
	emotion='happy'
elif(rounded<=1.0 and rounded>0.8):
	emotion='enthusiastic'
elif(rounded<=0.6 and rounded>0.4):
	emotion='surprise'
elif(rounded<=0.4 and rounded>0.2):
	emotion='enjoyment'
elif(rounded<=0.2 and rounded>0.0):
	emotion='anticipation'
elif(rounded<=0.0 and rounded>-0.4):
	emotion='fear'
elif(rounded<=-0.4 and rounded>-0.6):
	emotion='sad'
elif(rounded<=-0.6 and rounded>-1.0):
	emotion='anger'
else:
	emotion='happy'
	



def main(emotion): 
	
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
	response = HTTP.get(urlhere) 
	data = response.text 

	# Parsing the data using 
	# BeautifulSoup 
	soup = SOUP(data, "lxml") 

	# Extract movie titles from the 
	# data using regex 
	title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 
	return title 

# Driver Function 
if __name__ == '__main__': 
	
	
	a = main(emotion)
	
	count = 0

	if(emotion == "" ): 

		for i in a: 

			# Splitting each line of the 
			# IMDb data to scrape movies 
			tmp = str(i).split('>;') 

			if(len(tmp) == 3): 
				print(tmp[1][:-3]) 

			if(count > 13): 
				break
			count += 1
	else: 
		for i in a: 
			tmp = str(i).split('>') 

			if(len(tmp) == 3): 
				print(tmp[1][:-3]) 

			if(count > 11): 
				break
			count+=1

