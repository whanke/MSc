# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 16:33:09 2018

@author: Wilm Hanke
"""

import pymongo
from pymongo import MongoClient
import datetime

# making a connection to MongoDB
client = pymongo.MongoClient('localhost', 27017)

# getting a database
db = client.test_database

collection = db.test_collection

post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

# insert a document
posts = db.posts
post_id = posts.inster_one(post).inserted_id