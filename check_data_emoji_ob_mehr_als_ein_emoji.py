# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:42:41 2018

@author: Wilm Hanke
"""

import emoji 
import json
import datetime
import pandas as pd


### funktioniert und wurde ausgeführt

### hat aus raw_data alle tweets mit nur 1 emoji genommen (egal ob mit oder ohne reply)

start_time = datetime.datetime.now()
#liest Datei mit Tweets (mit nur einem Emoji) ein
with open("data_tweets_with_emoji_json.txt", "r", encoding="utf-8") as file: 
    print("Strip corpus...")
    data = (line.strip() for line in file)
    data_json = "[{0}]".format(','.join(data))
    print("Load file as json...")
    data = json.loads(data_json)
    
df = pd.DataFrame(data, columns=['id_str','text','in_reply_to_user_id_str'])
    
tweets_mit_mehr_als_ein_emoji = 0  
i = 0
while i < len(data):
        emoj = []
        # Iteration über Tweet
        for char in df['text'].loc[i]:
            # Wenn char ein Emoji ist: zu list(emoj) hinzufügen
            if char in emoji.UNICODE_EMOJI:
                emoj.append(char)
        # Wenn Tweet mehr als ein Emoji beinhaltet:
        if len(emoj) > 1:            
            print('Tweet hat mehr als ein Emoji')
            tweets_mit_mehr_als_ein_emoji += tweets_mit_mehr_als_ein_emoji
        i += 1
print('tweets_mit_mehr_als_ein_emoji ', tweets_mit_mehr_als_ein_emoji)
print("Dauer: ", datetime.datetime.now() - start_time)