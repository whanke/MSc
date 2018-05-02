# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 12:25:55 2018

@author: Wilm Hanke
"""
import emoji 
import json
import datetime
import pandas as pd




# schreibt tweet mit nur einem emoji in txt

def one_emoji_in_tweet():
    i = 0
    
    
    # Iteration über alle Tweets
    while i < len(df):
        emoj = []
        # Iteration über Tweet
        for char in df['text'].loc[i]:
            # Wenn char ein Emoji ist: zu list(emoj) hinzufügen
            if char in emoji.UNICODE_EMOJI:
                emoj.append(char)
        # Wenn Tweet nur ein Emoji beiinhaltet:
        if len(emoj) == 1:
            return(df['text'].loc[i])
        i += 1 

start_time = datetime.datetime.now()
with open("tweet_by_ID_25_3_2018__07_04_27.txt", "r", encoding="utf-8") as file: #"tweet_by_ID_25_3_2018__07_04_27.txt"
    print("Strip corpus...")
    data = (line.strip() for line in file)
    data_json = "[{0}]".format(','.join(data))
    print("Load file as json...")
    data = json.loads(data_json)

df = pd.DataFrame(data, columns=['id_str','text','in_reply_to_user_id_str'])

with open("data_tweets_with_emoji_json.txt", "a", encoding="utf-8") as file:
    i = 101544 # so hohe Zahl, weil bei der ersten Berechnung der Strom ausfiel
    
    
    # Iteration über alle Tweets
    while i < len(data):
        emoj = []
        # Iteration über Tweet
        for char in df['text'].loc[i]:
            # Wenn char ein Emoji ist: zu list(emoj) hinzufügen
            if char in emoji.UNICODE_EMOJI:
                emoj.append(char)
        # Wenn Tweet nur ein Emoji beinhaltet:
        if len(emoj) == 1:            
            # Json in Datei schreiben
            file.write(json.dumps(data[i]) + '\n')
        i += 1

print("Dauer: ", datetime.datetime.now() - start_time)