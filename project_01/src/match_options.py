import nltk
from nltk.tag import pos_tag
from collections import defaultdict
import re

'''
The 'ignore_list' is a list of words and names to ignore when analyzing the twitter data,
of note, will ferrell and kristen wiig became a trending topic on google and yahoo during the 2013 golden globes
as suggestions of hosts for the following years golden globes.
'''
ignore_list = ['will', 'ferrell', 'kristen', 'wiig', 'golden', 'globes', 'globe', 'goldenglobes', '#goldenglobes', 'oscars']

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

''' Read in all twitter data and sort data by co-appearance of bigrams with list of tags'''
def get_bigram_list_match_tweets_lax(tweets, words_to_match):
    d = defaultdict(int)
    for idx in range(0, len(tweets)):
        if match_all_words_lax(tweets[idx][0], words_to_match):
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

def match_all_words_lax(tweet, words_to_match):
    for word in words_to_match:
        if word not in tweet:
            return False
    return True

def match_a_word_lax(tweet, words_to_match):
    for word in words_to_match:
        if word in tweet:
            return True
    return False

''' Regular expression to check if full word is in sentence, not just is the word is a substring of the full sentence '''
def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

'''
def pairAward(award, candidates, tweets, qty=1, parsed_list=[]):
    d = defaultdict(int)

    print(candidates)

    if parsed_list:
        print("Using Augmented Search")
        winner = get_winner(award, tweets, parsed_list)
        for tweet in range(0, len(tweets)):
            for jdx in range(0, len(candidates)):
                candidate = candidates[jdx].lower()
                for element in candidate:
                    splitCandidate = element.split()
                    splitWinner = winner.split()
                    if findAllWords(splitCandidate, tweets[tweet][0].lower()) and findAllWords(award.split(), tweets[tweet][0].lower()):
                        d[element] += 1
                    if findAllWords(splitWinner, tweets[tweet][0].lower()) and findAllWords(award.split(), tweets[tweet][0].lower()):
                        d[element] += 1
    else:
        print("Not using Augmented Search")
        for tweet in range(0, len(tweets)):
            for jdx in range(0, len(candidates)):
                candidate = candidates[jdx].lower()
                for element in candidate:
                    splitCandidate = element.split()
                    if findAllWords(splitCandidate, tweets[tweet][0].lower()) and findAllWords(award.split(), tweets[tweet][0].lower()):
                        d[element] += 1

    for key in ignore_list:
        for dKey in d.keys():
            if key in dKey:
                del d[dKey]

    sorted_vals = sorted(d.iteritems(), key =lambda (k,v): v, reverse=True)
    if qty < 0:
        return sorted_vals
    else:
        return sorted_vals[0:qty]
'''


def pairWinner(query, candidates, tweets, qty=1):
    d = defaultdict(int)
    for tweet in range(0, len(tweets)):
        for jdx in range(0, len(candidates)):
            candidate = candidates[jdx].lower()
            splitCandidate = candidate.split()
            if findAllWords(splitCandidate, tweets[tweet][0].lower()) and findAllWords(query.split(), tweets[tweet][0].lower()):
                d[candidate] += 1

    for key in ignore_list:
        for dKey in d.keys():
            if key in dKey:
                del d[dKey]

    sorted_vals = sorted(d.iteritems(), key =lambda (k,v): v, reverse=True)
    if qty < 0:
        return sorted_vals
    else:
        return sorted_vals[0:qty]


def findAllWords(listIn, strIn):
    for idx in range(0, len(listIn)):
        if not findWholeWord(listIn[idx])(strIn):
            return 0

    return 1

''' Read in all twitter data and sort data by co-appearance of bigrams with list of tags'''
def get_bigram_list_match_tweets_either_or_lax(tweets, words_to_match, options_to_match):
    d = defaultdict(int)
    for idx in range(0, len(tweets)):
        if match_all_words_lax(tweets[idx][0], words_to_match) and match_a_word_lax(tweets[idx][0], options_to_match):
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


''' Read in all twitter data and sort data by co-appearance with best comedy or musical actor tags'''
def get_unigram_list_match_tweets_lax(tweets, words_to_match):
    d = defaultdict(int)
    for idx in range(0,len(tweets)):
        if match_all_words_lax(tweets[idx][0], words_to_match):
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
def get_unigram_list_match_tweets_either_or_lax(tweets, words_to_match, options_to_match):
    d = defaultdict(int)
    for idx in range(0,len(tweets)):
        if match_all_words_lax(tweets[idx][0], words_to_match) and match_a_word_lax(tweets[idx][0], options_to_match):
            tagged_tweet = pos_tag(tweets[idx][0].split())
            proper_nouns = [pn.lower() for pn,pos in tagged_tweet if pos == 'NNP']
            for pnoun in proper_nouns:
                d[pnoun] += 1
    for key in ignore_list:
        if key in d.keys():
            del d[key]
    sorted_vals = sorted(d.iteritems(), key =lambda (k,v): v, reverse=True)
    return sorted_vals

'''
WE DON'T JUST WANT THE BEST MATCH, WE WANT THE BEST MATCH THAT IS HIGHEST IN OUR LIST
'''
def get_best_match(query, candidates):
    d = defaultdict(int)
    for candidate in candidates:
        d[candidate] = nltk.edit_distance(candidate, query)

    sorted_vals = sorted(d.iteritems(), key =lambda (k,v): v)

    return sorted_vals[0]
