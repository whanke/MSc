# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 12:47:56 2018

@author: Wilm Hanke
"""

import json
from pprint import pprint
import emoji
import datetime


start_time = datetime.datetime.now()
print("Lade JSON... - ", datetime.datetime.now())
with open("tweet_by_ID_25_3_2018__07_04_27.txt", "r", encoding='utf-8') as file:
    data = (line.strip() for line in file)
    data_json = "[{0}]".format(','.join(data))
    
    data = json.loads(data_json)

   #entspricht der 1. JSON Datei       
#data[0]
    
  
  # bekommt key-value Paar aus einzelnem JSON
#    for key, value in data[0].items():
#    if key == "in_reply_to_status_id":
#        print(key,value)
  
  
  # wie man an die reply tweets kommt
#i = 0
#while i != len(data):
#    print(i)
#    for key,value in data[i].items():
#        if key == "in_reply_to_status_id":
#            if value != None:
#                print(data[i]["text"])
#                with open("reply_tweets.txt", "a", encoding="utf-8") as f:
#                    f.write(json.dumps(data[i])+ '\n')
#    i += 1
    
# checking if in tweet only one emoji 
print("Checke Tweets nach Emoji...")
j = 0
#json_with_one_emoji = [] # Hilfskonstruktion mit Liste
while j<len(data):
    count_emoji_in_tweet = 0
    for char in data[j]["text"]:
        if char in emoji.UNICODE_EMOJI:
            count_emoji_in_tweet += 1
    if count_emoji_in_tweet == 1:
        print("Schreibe Tweet in Datei.")
        #json_with_one_emoji.append(data[j]) # Hilfskonstruktion mit Liste
        with open("tweets_with_emoji.txt","a", encoding="utf-8") as file:
           file.write(json.dumps(data[j]) + '\n')
        #print("Emojis im Tweet: ", count)
        #print(data[j]["text"])
        #print(data[j]["id"])
    j += 1
    
print("Checke Tweets nach Emoji: Fertig.")
end_time = datetime.datetime.now()
print("Dauer: ", end_time - start_time)
