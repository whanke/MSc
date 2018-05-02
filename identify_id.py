# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:10:18 2018

@author: Wilm Hanke
"""

import json
import datetime





# get data corpus
print("Open corpus file...")
start_time = datetime.datetime.now()
with open("tweet_by_ID_25_3_2018__07_04_27.txt", "r", encoding="utf-8") as file:
    print("Strip corpus...")
    data = (line.strip() for line in file)
    data_json = "[{0}]".format(','.join(data))
    print("Load file as json...")
    data = json.loads(data_json)
    
    print("Open reply_tweets.txt...")
    with open("reply_tweets.txt", "r", encoding="utf-8") as reply_file:
        reply_data = (line.strip() for line in reply_file)
        tweet_json = "[{0}]".format(','.join(reply_data))
        reply_data = json.loads(tweet_json) 
        
        reply_id = 0
        c = 0
        j = 0
        while j != len(reply_data):        
            for key,value in reply_data[j].items():
                if key == "in_reply_to_status_id":
                    print("reply_data :", c, "von ", len(reply_data))
                    print(key, ": ", value)
                    reply_id = value
                    #print("Name :",reply_data[j]['user']['name'])
                    #print("Screen_Name :",reply_data[j]['user']["screen_name"])
                    c += 1
            i = 0
            while i != len(data):
                #print(i)
                for key,value in data[i]['user'].items():
                    if key == "id":
                        if value == reply_id:
                            #print(data[i]["text"])
                            print("Found: ", value)
                            with open("tweet_conversations.txt", "a", encoding="utf-8") as conv:
                                conv.write(json.dumps(data[i]) + '\n')
                                conv.write(json.dumps(reply_data[j])+ '\n')
                i += 1
            j += 1
        end_time = datetime.datetime.now()
        print('Done.\nDauer: ', (end_time - start_time))
        
        
