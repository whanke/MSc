# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 10:49:20 2018

@author: Wilm Hanke
"""

# tweets aus corpus filtern, die lediglich ein emoji ( :), :( )

import emoji 
import json
import datetime
import re
from collections import Counter
# um Zeit zu messen wie lange ein Algorithmus brauch
import timeit
# count() vs Counter()
#t1=timeit.Timer('Counter(l)', \
#                'import random;import string;from collections import Counter;n=1000;l=[random.choice(string.ascii_letters) for x in range(n)]'
#                )
#
#t2=timeit.Timer('[[x,l.count(x)] for x in set(l)]',
#                'import random;import string;n=1000;l=[random.choice(string.ascii_letters) for x in range(n)]'
#                )
#
#print("Counter(): ", t1.repeat(repeat=3,number=10000))
#print("count():   ", t2.repeat(repeat=3,number=10000)



# get data corpus
print("Open corpus file...")
start_time = datetime.datetime.now()

with open("tweet_by_ID_25_3_2018__07_04_27.txt", "r", encoding="utf-8") as file: #"tweet_by_ID_25_3_2018__07_04_27.txt"
    print("Strip corpus...")
    data = (line.strip() for line in file)
    data_json = "[{0}]".format(','.join(data))
    print("Load file as json...")
    data = json.loads(data_json)
    
    i = 0
    emojis = []
    while i < len(data):
        # fügt gefundenes emoji(s) einer Liste hinzu
        emojis.append(''.join(c for c in data[i]["text"] if c in emoji.UNICODE_EMOJI))            
        i += 1
    # jedes vorkommende ELement in Liste wird gezählt
    # Counter(emojis)
print("Dauer: ", datetime.datetime.now() - start_time)