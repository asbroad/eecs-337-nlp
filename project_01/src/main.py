#! /usr/bin/python
import json
import urllib
import re
import nltk
from nltk.tag import pos_tag
from collections import defaultdict
import datetime
from scrape_2013_data import parse_2013_wikipedia_movies, parse_2013_wikipedia_tv
from scrape_2015_data import parse_2015_wikipedia_movies, parse_2015_wikipedia_tv, parse_2015_wikipedia_presenters
# json file is in utf-8 format
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

'''
Notes for our group...

 - The first approach that I tried does not work well with 'nominees' because it doesn't seem like people tweet about that too much
 - Does anyone know how to make GUI's with Python?
 - Does anyone have experience scraping web-pages?

Some ideas...
1. Right now, we only look for single proper nouns, it may be good to look at pairs of them (try and get full names)
2. Print out a visual of a timeline of the event (the 2013 data is about 4hrs of data) and print popularity of people at given time
points, maybe try and analyze if people's names show up as they are presenting or if the have just won or lost an award?
3. Use ideas from Named Entity Recognition  (http://en.wikipedia.org/wiki/Named-entity_recognition)
4. Use Golden Globes wiki page as a resource that we can scrape (http://en.wikipedia.org/wiki/70th_Golden_Globe_Awards)
5. Maybe use other preprocessing techniques (stem words, remove punctuation, etc...)

'''

'''
The 'ignore_list' is a list of words and names to ignore when analyzing the twitter data,
of note, will ferrell and kristen wiig became a trending topic on google and yahoo during the 2013 golden globes
as suggestions of hosts for the following years golden globes.
'''
ignore_list = ['will', 'ferrell', 'kristen', 'wiig', 'golden', 'globes', 'goldenglobes', '#goldenglobes', 'oscars']

''' main function '''
def main():
    #print urllib.urlopen("http://en.wikipedia.org/wiki/70th_Golden_Globe_Awards").read()
    #tweet_file = open('../data/gg15trimmed.json','r')
    #tweet_file = open('../data/gg15mini.json','r')
    # the below file doesn't work because it takes up too much memory to read in
    #tweets = read_in_tweets_2015(tweet_file)
    #res = get_best_drama_actor(tweets)
    #print(res[0:25])
    #xml_file = '70th_Golden_Globe_Awards.xml'
    #movie_response = parse_2013_wikipedia_movies(xml_file)
    #for itm in movie_response:
    #    print(itm)
    #tv_response = parse_2013_wikipedia_tv(xml_file)
    #for itm in tv_response:
    #    print(itm)
    xml_file_2015 = '72nd_Golden_Globe_Awards.xml'
    #movie_response_2015 = parse_2015_wikipedia_movies(xml_file_2015)
    #for itm in movie_response_2015:
    #    print(itm)
    #tv_response_2015 = parse_2015_wikipedia_tv(xml_file_2015)
    #for itm in tv_response_2015:
    #    print(itm)
    parse_2015_wikipedia_presenters(xml_file_2015)
    #vals = bigramNameFind(tweets)
    #print(vals)

def bigramNameFind(tweets):

    d = defaultdict(int)
    for idx in range(0, len(tweets)):
        if findWholeWord('host')(tweets[idx][0]):
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


''' Read in all twitter data and sort data by co-appearance with host tags'''
def get_hosts(tweets):
    d = defaultdict(int)
    for idx in range(0,len(tweets)):
        if findWholeWord('host')(tweets[idx][0]):
            tagged_tweet = pos_tag(tweets[idx][0].split())
            proper_nouns = [pn.lower() for pn,pos in tagged_tweet if pos == 'NNP']
            for pnoun in proper_nouns:
                d[pnoun] += 1
    for key in ignore_list:
        if key in d.keys():
            del d[key]
    pos_hosts = sorted(d.iteritems(), key =lambda (k,v): v, reverse=True)
    return pos_hosts

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


''' Hand coded 2015 data, the first value in each array is the winner '''
def get_academy_info():
    truth_data = {}
    performer_movie = {}

    truth_data['best movie drama'] = ['boyhood', 'foxcatcher', 'the imitation game', 'selma', 'the theory of everything']
    truth_data['best actress drama'] = ['julianne moore', 'rosamund pike', 'reese witherspoon', 'felicity jones', 'jenifer aniston']
    truth_data['best actor drama']  = ['eddie redmayne', 'steve carell', 'benedict cumberbatch', 'david oyelowo', 'jake gyllenhaal']
    truth_data['best movie musical or comedy'] = ['the grand budapest hotel', 'into the woods', 'birdman', 'st. vincent', 'pride']
    truth_data['best actress musical or comedy'] = ['amy adams', 'julianne moore', 'emily blunt', 'helen mirren', 'quvenzhane wallis']
    truth_data['best actor musical or comedy'] = ['michael keaton', 'bill murray', 'ralph fiennes', 'christoph waltz', 'joaquin phoenix']
    truth_data['best animated movie'] = ['how to train your dragon 2', 'the lego movie', 'big hero 6', 'the book of life', 'the boxtrolls']
    truth_data['best foreign movie'] = ['leviathan', 'ida', 'force majeure', 'gett: the trial of viviane amsalem', 'tangerines']
    truth_data['best supporting actress'] = ['patricia arquette', 'jessica chastain', 'keira knightley', 'meryl streep', 'emma stone']
    truth_data['best supporting actor'] = ['j.k. simmons', 'ethan hawke', 'robert duvall', 'edward norton', 'mark ruffalo']
    truth_data['best directory'] = ['richard linklater', 'ava duvernay', 'wes anderson', 'alejandro gonzalez inarritu', 'david fincher']
    truth_data['best screenplay'] = ['alejandro gonzalez inarritu, nicolas giacobone, alexander dinelaris, armando bo', 'wes anderson', 'gillian flynn', 'richard linklater', 'graham moore']
    truth_data['best original score'] = ['johann johannsson', 'alexandre desplat', 'trent reznor, atticus ross', 'antonio sanchez', 'hans zimmer']
    truth_data['best original song'] = ['selma', 'big eyes', 'noah', 'annie', 'the hunger games: mockingjay, part 1']
    truth_data['best tv series drama'] = ['the affair', 'downton abbey', 'game of thrones', 'house of cards', 'the good wife']
    truth_data['best actress tv drama'] = ['ruth wilson', 'viola davis', 'claire danes', 'julianna margulies', 'robin wright']
    truth_data['best actor tv drama'] = ['kevin spacey', 'clive owen', 'james spader', 'dominic west', 'liev schreiber']
    truth_data['best tv musical or comedy'] = ['transparent', 'orange is the new black', 'girls', 'jane the virgin', 'silicon valley']
    truth_data['best actress tv musical or comedy'] = ['gina roderiguez', 'julia louis-dreyfus', 'edie falco', 'lena dunham', 'taylor schilling']
    truth_data['best actor tv musical or comedy'] = ['jeffrey tambor', 'don cheadle', 'william h. macy', 'ricky gervais', 'louis c.k.']
    truth_data['best tv movie'] = ['fargo', 'olive kitteridge', 'the missing', 'true detective', 'the normal heart']
    truth_data['best actress tv movie'] = ['maggie gyllenhaal', 'jessica lange', 'france mcdormand', 'allison tolman', 'frances o\'connor']
    truth_data['best actor tv movie'] = ['billy bob thornton', 'martin freeman', 'matthew mcconaughey', 'woody harrelson', 'mark ruffalo']
    truth_data['best supporting actress tv movie'] = ['joanne froggatt', 'kathy bates', 'uzo aduba', 'michelle monaghan', 'allison janney']
    truth_data['best supporting actor tv movie'] = ['matt bomer', 'bill murray', 'jon voight', 'alan cumming', 'colin hanks']

    performer_movie['julianne moore'] = 'still alice'
    performer_movie['rosamund pike'] = 'gone girl'
    performer_movie['reese witherspoon'] = 'wild'
    performer_movie['felicity jones'] = 'the theory of everything'
    performer_movie['jennifer aniston'] = 'cake'
    performer_movie['eddie redmayne'] = 'the theory of everything'
    performer_movie['steve carell'] = 'foxcatcher'
    performer_movie['benedict cumberbatch'] = 'the imitation game'
    performer_movie['david oyelowo'] = 'selma'
    performer_movie['jake gyllenhaal'] = 'nightcrawler'
    performer_movie['julianne moore'] = 'maps to the stars'
    performer_movie['amy adams'] = 'big eyes'
    performer_movie['emily blunt'] = 'into the woods'
    performer_movie['helen mirren'] = 'the hundred foot journey'
    performer_movie['quvenzhane wallis'] = 'annie'
    performer_movie['michael keaton'] = 'birdman'
    performer_movie['bill murray'] = 'st. vincent'
    performer_movie['ralph fiennes'] = 'the grand budapest hotel'
    performer_movie['christoph waltz'] = 'big eyes'
    performer_movie['joaquin phoenix'] = 'inherent vice'
    performer_movie['jessica chastain'] = 'a most violent year'
    performer_movie['keira knightley'] = 'the imitation game'
    performer_movie['patricia arquette'] = 'boyhood'
    performer_movie['meryl streep'] = 'into the woods'
    performer_movie['emma stone'] = 'birdman'
    performer_movie['ethan hawke'] = 'boyhood'
    performer_movie['robert duvall'] = 'the judge'
    performer_movie['edward norton'] = 'birdman'
    performer_movie['j.k. simmons'] = 'whiplash'
    performer_movie['mark ruffalo'] = 'foxcatcher'
    performer_movie['ava duvernay'] = 'selma'
    performer_movie['wes anderson'] = 'the grand budapest hotel'
    performer_movie['alejandro gonzalez inarritu'] = 'birdman'
    performer_movie['david fincher'] = 'gone girl'
    performer_movie['richard linklater'] = 'boyhood'
    performer_movie['wes anderson'] = 'the grand budapest hotel'
    performer_movie['gillian flynn'] = 'gone girl'
    performer_movie['alejandro gonzalez inarritu, nicolas giacobone, alexander dinelaris, armando bo'] = 'birdman'
    performer_movie['richard linklater'] = 'boyhood'
    performer_movie['graham moore'] = 'the imitation game'
    performer_movie['alexandre desplat'] = 'the imitation game'
    performer_movie['johann johannsson'] = 'the theory of everything'
    performer_movie['trent reznor, atticus ross'] = 'gone girl'
    performer_movie['antonio sanchez'] = 'birdman'
    performer_movie['hans zimmer'] = 'interstellar'
    performer_movie['viola davis'] = 'how to get away with murder'
    performer_movie['claire danes'] = 'homeland'
    performer_movie['julianna margulies'] = 'the good wife'
    performer_movie['robin wright'] = 'house of cards'
    performer_movie['ruth wilson'] = 'the affiar'
    performer_movie['kevin spacey'] = 'house of cards'
    performer_movie['clive owen'] = 'the knick'
    performer_movie['james spader'] = 'the blacklist'
    performer_movie['dominic west'] = 'the affair'
    performer_movie['liev schreiber'] = 'ray donovan'
    performer_movie['julia louis dreyfus'] = 'veep'
    performer_movie['edie falco'] = 'nurse jackie'
    performer_movie['gina roderiguez'] = 'jane the virgin'
    performer_movie['lena dunham'] = 'girls'
    performer_movie['taylor schilling'] = 'orange is the new black'
    performer_movie['don cheadle'] = 'house of lies'
    performer_movie['william h. macy'] = 'shameless'
    performer_movie['ricky gervais'] = 'derek'
    performer_movie['jeffrey tambor'] = 'transparent'
    performer_movie['louis c.k.'] = 'louie'
    performer_movie['jessica lange'] = 'american horror story: freak show'
    performer_movie['maggie gyllenhaal'] = 'the honorable woman'
    performer_movie['frances mcdorman'] = 'olive kitteridge'
    performer_movie['allison tolman'] = 'fargo'
    performer_movie['frances o\'connor'] = 'the missing'
    performer_movie['martin freeman'] = 'fargo'
    performer_movie['matthew mcconaughey'] = 'true detective'
    performer_movie['billy bob thornton'] = 'fargo'
    performer_movie['mark ruffalo'] = 'the normal heart'
    performer_movie['kathy bates'] = 'american horror story: freak show'
    performer_movie['uzo aduba'] = 'orange is the new black'
    performer_movie['joanne froggatt'] = 'downton abbey'
    performer_movie['michelle monaghan'] = 'true detective'
    performer_movie['allison janney'] = 'mom'
    performer_movie['bill murray'] = 'olive kitteridge'
    performer_movie['jon voight'] = 'ray donovan'
    performer_movie['matt bomar'] = 'the normal heart'
    performer_movie['alan cumming'] = 'the good wife'
    performer_movie['colin hanks'] = 'fargo'

    return [truth_data, performer_movie]

if __name__ == "__main__":
    main()
