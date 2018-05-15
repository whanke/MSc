import sys
import json
import time
import logging
import twitter
import urllib.parse

from os import environ as e


def get_tweets(filename):
    for line in open(filename, encoding='utf-8'):
        yield json.loads(line)
        # yield print(twitter.Status.NewFromJsonDict(json.loads(line)))


def get_full_tweets(filename):
    for line in open(filename, encoding='utf-8'):
        yield json.loads(line)


def check_tweet_has_reply():
    for full_tweets in raw_data:
        for tweet in tweets_w_reply_id:
            if hasattr(tweet, 'in_reply_to_user_id_str'):
                if (tweet.in_reply_to_user_id_str == full_tweets.id_str):
                    replies.append(tweet.text)
                    print(tweet.text)
        #print("Tweet :", full_tweets.text)
        for elements in replies:
            print("Replies :", elements)

# if __name__ == "__main__":
#     logging.basicConfig(filename="replies.log", level=logging.INFO)
#     tweets_file = 'C:/MSc/data_test.txt'  # sys.argv[1]
#     for tweet in get_tweets(tweets_file):
#         for reply in get_replies(tweet):
#             print(reply.AsJsonString())


replies = []

tweets_w_reply_id = get_tweets('C:/MSc/data_tweets_with_emoji_json.txt')
# tweet_by_ID_25_3_2018__07_04_27.txt
raw_data = get_full_tweets('tweet_by_ID_25_3_2018__07_04_27.txt')


# prüft, ob eine reply_id von tweets mit reply_ids in id_str in raw_data existiert --> Ergebnis: kein Fund
def reply_id_equal_id():
    for i in tweets:
        if i['in_reply_to_user_id_str'] != None:
            for t in raw_data:
                if i['in_reply_to_user_id_str'] == t['id_str']:
                    print('original Tweet gefunden')
                    print(t['id_str'], i['in_reply_to_user_id_str'])


def check_str_in_txt(name, reply_id, id):


check_tweet_has_reply()
