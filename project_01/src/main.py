#! /usr/bin/python
import json
import urllib
import re
import nltk
from nltk.tag import pos_tag
from collections import defaultdict
import datetime
from scrape_2013_data import parse_2013_wikipedia_movies, parse_2013_wikipedia_tv, parse_2013_wikipedia_presenters
from scrape_2015_data import parse_2015_wikipedia_movies, parse_2015_wikipedia_tv, parse_2015_wikipedia_presenters
# json file is in utf-8 format
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

'''
Some ideas...
1. Print out a visual of a timeline of the event (the 2013 data is about 4hrs of data) and print popularity of people at given time
points, maybe try and analyze if people's names show up as they are presenting or if the have just won or lost an award?

'''

'''
The 'ignore_list' is a list of words and names to ignore when analyzing the twitter data,
of note, will ferrell and kristen wiig became a trending topic on google and yahoo during the 2013 golden globes
as suggestions of hosts for the following years golden globes.
'''
ignore_list = ['will', 'ferrell', 'kristen', 'wiig', 'golden', 'globes', 'goldenglobes', '#goldenglobes', 'oscars']

''' main function '''
def main():
    ''' Twitter JSON files '''
    tweet_file = open('../data/goldenglobes.json','r')
    #tweet_file = open('../data/gg15trimmed.json','r') # this file doesn't work, because it take up too much memory to read in
    #tweet_file = open('../data/gg15mini.json','r')
    #tweet_file = open('gg15mini_half.json','r')

    ''' Read in JSON file '''
    tweets = read_in_tweets(tweet_file)
    #tweets = read_in_tweets_2015(tweet_file)

    ''' Golden Globe Wikipedia XML files '''
    # xml_file_2013 = '70th_Golden_Globe_Awards.xml'
    # xml_file_2015 = '72nd_Golden_Globe_Awards.xml'

    ''' Lists of terms to search for in tweets by catagory '''
    ''' lot = List of Terms '''
    lot_hosts = ['host']
    lot_best_actor_drama_movie = ['best', 'drama', 'actor']


    ''' Analysis '''
    res = get_bigram_list_match_tweets(tweets,lot_hosts)
    print res[0:25]

''' Read in all twitter data and sort data by co-appearance of bigrams with list of tags'''
def get_bigram_list_match_tweets(tweets, words_to_match):
    d = defaultdict(int)
    for idx in range(0, len(tweets)):
        if match_all_words(tweets[idx][0], words_to_match):
            tagged_tweet = pos_tag(tweets[idx][0].split())
            proper_nouns = [pn.lower() for pn,pos in tagged_tweet if pos == 'NNP']
            bigramsList = list(nltk.bigrams(proper_nouns))

            for j in range(0, len(bigramsList)):
                token = bigramsList[j][0]+" "+bigramsList[j][1]
                d[token] += 1

    for key in ignore_list:
        for dKey in d.keys():
            if key in dKey:
                del d[dKey]

    sorted_vals = sorted(d.iteritems(), key =lambda (k,v): v, reverse=True)
    return sorted_vals

''' Read in all twitter data and sort data by co-appearance with list of tags'''
def get_list_match_tweets(tweets, words_to_match):
    d = defaultdict(int)
    for idx in range(0,len(tweets)):
        if match_all_words(tweets[idx][0], words_to_match):
            tagged_tweet = pos_tag(tweets[idx][0].split())
            proper_nouns = [pn.lower() for pn,pos in tagged_tweet if pos == 'NNP']
            for pnoun in proper_nouns:
                d[pnoun] += 1
    for key in ignore_list:
        if key in d.keys():
            del d[key]
    pos_hosts = sorted(d.iteritems(), key =lambda (k,v): v, reverse=True)
    return pos_hosts

def match_all_words(tweet, words_to_match):
    for word in words_to_match:
        if not findWholeWord(word)(tweet):
            return False
    return True

#################################################################
#####################     OLD     ###############################
#################################################################


''' Read in all twitter data and sort data by co-appearance with best drama actor tags'''
def get_best_drama_actor(tweets):
    d = defaultdict(int)
    for idx in range(0,len(tweets)):
        if 'best' in tweets[idx][0] and 'drama' in tweets[idx][0] and 'actor' in tweets[idx][0]:
            tagged_tweet = pos_tag(tweets[idx][0].split())
            proper_nouns = [pn.lower() for pn,pos in tagged_tweet if pos == 'NNP']
            for pnoun in proper_nouns:
                d[pnoun] += 1
    for key in ignore_list:
        if key in d.keys():
            del d[key]
    sorted_vals = sorted(d.iteritems(), key =lambda (k,v): v, reverse=True)
    return sorted_vals

''' Read in all twitter data and sort data by co-appearance with best comedy or musical actor tags'''
def get_best_musical_or_comedy_actor(tweets):
    d = defaultdict(int)
    for idx in range(0,len(tweets)):
        if 'best' in tweets[idx][0] and 'actor' in tweets[idx][0] and ('com' in tweets[idx][0] or 'mus' in tweets[idx][0]):
            tagged_tweet = pos_tag(tweets[idx][0].split())
            proper_nouns = [pn.lower() for pn,pos in tagged_tweet if pos == 'NNP']
            for pnoun in proper_nouns:
                d[pnoun] += 1
    for key in ignore_list:
        if key in d.keys():
            del d[key]
    sorted_vals = sorted(d.iteritems(), key =lambda (k,v): v, reverse=True)
    return sorted_vals

''' Read in all twitter data and sort data by co-appearance with best drama movie'''
def get_best_drama_movie(tweets):
    d = defaultdict(int)
    for idx in range(0,len(tweets)):
        if 'best' in tweets[idx][0] and 'drama' in tweets[idx][0] and 'motion' in tweets[idx][0] and 'picture' in tweets[idx][0]:
            tagged_tweet = pos_tag(tweets[idx][0].split())
            proper_nouns = [pn.lower() for pn,pos in tagged_tweet if pos == 'NNP']
            for pnoun in proper_nouns:
                d[pnoun] += 1
    for key in ignore_list:
        if key in d.keys():
            del d[key]
    sorted_vals = sorted(d.iteritems(), key =lambda (k,v): v, reverse=True)
    return sorted_vals

''' Read in all twitter data and sort by number of tweets per user '''
def get_user_tweet_counts(tweets):
    d = defaultdict(int)
    for idx in range(0,len(tweets)):
        d[tweets[idx][4]] += 1
    users_sorted = sorted(d.iteritems(), key =lambda (k,v): v, reverse=True)
    return users_sorted

''' Read in all twitter data and print out tweets by a particular user, may not be too helpful '''
def get_gg(tweets):
    d = defaultdict(int)
    for idx in range(0,len(tweets)):
        if tweets[idx][4] == 'TVGuide':
            print tweets[idx]

''' Read in all twitter data and create a human readable time stamp for each tweet '''
def get_user_tweet_time(tweets):
    times = []
    for idx in range(0,len(tweets)):
        val1 = str(tweets[idx][1])
        val = val1[0:-3]
        times.append(datetime.datetime.fromtimestamp(int(val)).strftime('%Y-%m-%d %H:%M:%S'))
    return times

''' Read in all the twitter data and save in python array '''
def read_in_tweets(tweet_file):
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


''' Regular expression to check if full word is in sentence, not just is the word is a substring of the full sentence '''
def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

if __name__ == "__main__":
    main()
