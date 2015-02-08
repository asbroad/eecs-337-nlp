import json
# json file is in utf-8 format
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

''' Read in all the twitter data and save in python array '''
def read_in_tweets_2013(tweet_file):
    tweets_orig = [json.loads(line) for line in tweet_file]
    tweets = []
    for idx in range(0,len(tweets_orig)):
        tweet = tweets_orig[idx]
        row = (
            tweet['text'],
            tweet['created_at']['$date'],
            tweet['_id']['$oid'],
            tweet['id'],
            tweet['user']['screen_name'],
            tweet['user']['id']
        )
        values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
        tweets.append(values)
    return tweets

''' Read in all the twitter data and save in python array '''
def read_in_tweets_2015(tweet_file):
    tweets_orig = [json.loads(line) for line in tweet_file]
    tweets = []
    for idx in range(0,len(tweets_orig[0])):
        tweet = tweets_orig[0][idx]
        row = (
            tweet['text'],
            tweet['timestamp_ms'],
            tweet['id'],
            tweet['user']['screen_name'],
            tweet['user']['id']
        )
        values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
        tweets.append(values)
    return tweets
