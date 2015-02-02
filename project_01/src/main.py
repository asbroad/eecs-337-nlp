#! /usr/bin/python
import json
import urllib
import re
from nltk.tag import pos_tag
from collections import defaultdict
import datetime
import xml.etree.ElementTree as ET

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
    tweet_file = open('../data/goldenglobes.json','r')
    # the below file doesn't work because it takes up too much memory to read in
    #tweet_file = open('/home/alex/Documents/School/Q2/NLP/data2105/goldenglobes2015.json','r')
    #tweets = read_in_tweets(tweet_file)
    #res = get_best_drama_actor(tweets)
    #print(res[0:25])
    movie_response = parse_wikipedia_movies()
    for itm in movie_response:
        print(itm)

    tv_response = parse_wikipedia_tv()
    for itm in tv_response:
        print(itm)



''' Parse wikipedia for movies '''
def parse_wikipedia_movies():
    tree = ET.parse('70th_Golden_Globe_Awards.xml')
    root = tree.getroot()
    body = tree.find('body')
    content_div = body.findall('div')[2]
    body_content_div = content_div.findall('div')[2]
    mw_content_div = body_content_div.findall('div')[3]
    wikitable = mw_content_div.find('table')

    best_movie_row = wikitable.findall('tr')[2]
    best_movie_drama_col = best_movie_row.findall('td')[0]
    best_movies_drama = best_movie_drama_col.findall('.//a')

    best_movies_drama_list = []
    for itm in best_movies_drama:
        val = itm.attrib['title']
        val_minus_wiki = val
        val_fixed = val_minus_wiki.replace('_', ' ')
        val_split = val_fixed.split('(')
        movie_name = val_split[0].strip()
        best_movies_drama_list.append(movie_name)

    best_movie_mus_or_com_col = best_movie_row.findall('td')[1]
    best_movies_mus_or_com = best_movie_mus_or_com_col.findall('.//a')

    best_movies_mus_or_com_list = []
    for itm in best_movies_mus_or_com:
        val = itm.attrib['title']
        val_minus_wiki = val
        val_fixed = val_minus_wiki.replace('_', ' ')
        val_split = val_fixed.split('(')
        movie_name = val_split[0].strip()
        best_movies_mus_or_com_list.append(movie_name)

    best_actor_row = wikitable.findall('tr')[5]
    best_actor_drama_col = best_actor_row.findall('td')[0]
    best_actor_drama = best_actor_drama_col.findall('.//li')

    best_actor_drama_list = []
    for idx in range(0,len(best_actor_drama)):
        if idx is 0:
            val = best_actor_drama[idx].find('b').find('a')
        else:
            val = best_actor_drama[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_drama_list.append(actor_name)

    best_actress_drama_col = best_actor_row.findall('td')[1]
    best_actress_drama = best_actress_drama_col.findall('.//li')

    best_actress_drama_list = []
    for idx in range(0,len(best_actress_drama)):
        if idx is 0:
            val = best_actress_drama[idx].find('b').find('a')
        else:
            val = best_actress_drama[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_drama_list.append(actress_name)

    best_actor_com_mus_row = wikitable.findall('tr')[8]
    best_actor_com_mus__col = best_actor_com_mus_row.findall('td')[0]
    best_actor_com_mus = best_actor_com_mus__col.findall('.//li')

    best_actor_com_mus_list = []
    for idx in range(0,len(best_actor_com_mus)):
        if idx is 0:
            val = best_actor_com_mus[idx].find('b').find('a')
        else:
            val = best_actor_com_mus[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_com_mus_list.append(actor_name)

    best_actress_com_mus__col = best_actor_com_mus_row.findall('td')[1]
    best_actress_com_mus = best_actress_com_mus__col.findall('.//li')

    best_actress_com_mus_list = []
    for idx in range(0,len(best_actress_com_mus)):
        if idx is 0:
            val = best_actress_com_mus[idx].find('b').find('a')
        else:
            val = best_actress_com_mus[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_com_mus_list.append(actress_name)

    best_actor_supporting_row = wikitable.findall('tr')[11]
    best_actor_supporting_col = best_actor_supporting_row.findall('td')[0]
    best_actor_supporting = best_actor_supporting_col.findall('.//li')

    best_actor_supporting_list = []
    for idx in range(0,len(best_actor_supporting)):
        if idx is 0:
            val = best_actor_supporting[idx].find('b').find('a')
        else:
            val = best_actor_supporting[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_supporting_list.append(actor_name)

    best_actress_supporting_col = best_actor_supporting_row.findall('td')[1]
    best_actress_supporting = best_actress_supporting_col.findall('.//li')

    best_actress_supporting_list = []
    for idx in range(0,len(best_actress_supporting)):
        if idx is 0:
            val = best_actress_supporting[idx].find('b').find('a')
        else:
            val = best_actress_supporting[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_supporting_list.append(actress_name)

    best_director_row = wikitable.findall('tr')[13]
    best_director_col = best_director_row.findall('td')[0]
    best_director = best_director_col.findall('.//li')

    best_director_list = []
    for idx in range(0,len(best_director)):
        if idx is 0:
            val = best_director[idx].find('b').find('a')
        else:
            val = best_director[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        director_name = val_split[0].strip()
        best_director_list.append(director_name)

    best_screenplay_col = best_director_row.findall('td')[1]
    best_screenplay = best_screenplay_col.findall('.//li')

    best_screenplay_list = []
    for idx in range(0,len(best_screenplay)):
        if idx is 0:
            val = best_screenplay[idx].find('b').find('a')
        else:
            val = best_screenplay[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        screenplay_title = val_split[0].strip()
        best_screenplay_list.append(screenplay_title)

    best_music_row = wikitable.findall('tr')[15]
    best_music_col = best_music_row.findall('td')[0]
    best_score = best_music_col.findall('.//li')

    best_score_list = []
    for idx in range(0,len(best_score)):
        if idx is 0:
            val = best_score[idx].find('b').find('a')
        else:
            val = best_score[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        score_title = val_split[0].strip()
        best_score_list.append(score_title)

    best_song_col = best_music_row.findall('td')[1]
    best_song = best_song_col.findall('.//li')

    best_song_list = []
    for idx in range(0,len(best_song)):
        if idx is 0:
            val = best_song[idx].find('b').find('a')
        else:
            val = best_song[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        song_title = val_split[0].strip()
        best_song_list.append(song_title)

    best_other_row = wikitable.findall('tr')[17]
    best_other_col = best_other_row.findall('td')[0]
    best_animated_film = best_other_col.findall('.//li')

    best_animated_list = []
    for idx in range(0,len(best_animated_film)):
        if idx is 0:
            val = best_animated_film[idx].find('i').find('b').find('a')
        else:
            val = best_animated_film[idx].find('i').find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        animated_title = val_split[0].strip()
        best_animated_list.append(animated_title)

    best_other_col = best_other_row.findall('td')[1]
    best_foreign = best_other_col.findall('.//li')

    best_foreign_list = []
    for idx in range(0,len(best_foreign)):
        if idx is 0:
            val = best_foreign[idx].find('b').find('i').find('a')
        else:
            val = best_foreign[idx].find('i').find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        foreign_title = val_split[0].strip()
        best_foreign_list.append(foreign_title)

    return [
    best_movies_drama_list,
    best_movies_mus_or_com_list,
    best_actor_drama_list,
    best_actress_drama_list,
    best_actor_com_mus_list,
    best_actress_com_mus_list,
    best_actor_supporting_list,
    best_actress_supporting_list,
    best_director_list,
    best_screenplay_list,
    best_score_list,
    best_song_list,
    best_animated_list,
    best_foreign_list
    ]

''' Parse wikipedia for tv '''
def parse_wikipedia_tv():
    tree = ET.parse('70th_Golden_Globe_Awards.xml')
    root = tree.getroot()
    body = tree.find('body')
    content_div = body.findall('div')[2]
    body_content_div = content_div.findall('div')[2]
    mw_content_div = body_content_div.findall('div')[3]
    wikitable = mw_content_div.findall('table')[2]

    best_tv_row = wikitable.findall('tr')[2]
    best_tv_drama_col = best_tv_row.findall('td')[0]
    best_tv_drama = best_tv_drama_col.findall('.//a')

    best_tv_drama_list = []
    for itm in best_tv_drama:
        val = itm.attrib['title']
        val_minus_wiki = val
        val_fixed = val_minus_wiki.replace('_', ' ')
        val_split = val_fixed.split('(')
        tv_name = val_split[0].strip()
        best_tv_drama_list.append(tv_name)

    best_tv_mus_or_com_col = best_tv_row.findall('td')[1]
    best_tv_mus_or_com = best_tv_mus_or_com_col.findall('.//a')

    best_tv_mus_or_com_list = []
    for itm in best_tv_mus_or_com:
        val = itm.attrib['title']
        val_minus_wiki = val
        val_fixed = val_minus_wiki.replace('_', ' ')
        val_split = val_fixed.split('(')
        tv_name = val_split[0].strip()
        best_tv_mus_or_com_list.append(tv_name)

    best_actor_row = wikitable.findall('tr')[5]
    best_actor_drama_col = best_actor_row.findall('td')[0]
    best_actor_drama = best_actor_drama_col.findall('.//li')

    best_actor_drama_list = []
    for idx in range(0,len(best_actor_drama)):
        if idx is 0:
            val = best_actor_drama[idx].find('b').find('a')
        else:
            val = best_actor_drama[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_drama_list.append(actor_name)

    best_actress_drama_col = best_actor_row.findall('td')[1]
    best_actress_drama = best_actress_drama_col.findall('.//li')

    best_actress_drama_list = []
    for idx in range(0,len(best_actress_drama)):
        if idx is 0:
            val = best_actress_drama[idx].find('b').find('a')
        else:
            val = best_actress_drama[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_drama_list.append(actress_name)

    best_actor_com_mus_row = wikitable.findall('tr')[8]
    best_actor_com_mus__col = best_actor_com_mus_row.findall('td')[0]
    best_actor_com_mus = best_actor_com_mus__col.findall('.//li')

    best_actor_com_mus_list = []
    for idx in range(0,len(best_actor_com_mus)):
        if idx is 0:
            val = best_actor_com_mus[idx].find('b').find('a')
        else:
            val = best_actor_com_mus[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_com_mus_list.append(actor_name)

    best_actress_com_mus__col = best_actor_com_mus_row.findall('td')[1]
    best_actress_com_mus = best_actress_com_mus__col.findall('.//li')

    best_actress_com_mus_list = []
    for idx in range(0,len(best_actress_com_mus)):
        if idx is 0:
            val = best_actress_com_mus[idx].find('b').find('a')
        else:
            val = best_actress_com_mus[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_com_mus_list.append(actress_name)

    best_actor_miniseries_row = wikitable.findall('tr')[11]
    best_actor_miniseries_col = best_actor_miniseries_row.findall('td')[0]
    best_actor_miniseries = best_actor_miniseries_col.findall('.//li')

    best_actor_miniseries_list = []
    for idx in range(0,len(best_actor_miniseries)):
        if idx is 0:
            val = best_actor_miniseries[idx].find('b').find('a')
        else:
            val = best_actor_miniseries[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_miniseries_list.append(actor_name)

    best_actress_miniseries_col = best_actor_miniseries_row.findall('td')[1]
    best_actress_miniseries = best_actress_miniseries_col.findall('.//li')

    best_actress_miniseries_list = []
    for idx in range(0,len(best_actress_miniseries)):
        if idx is 0:
            val = best_actress_miniseries[idx].find('b').find('a')
        else:
            val = best_actress_miniseries[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_miniseries_list.append(actress_name)


    best_actor_supporting_row = wikitable.findall('tr')[14]
    best_actor_supporting_col = best_actor_supporting_row.findall('td')[0]
    best_actor_supporting = best_actor_supporting_col.findall('.//li')

    best_actor_supporting_list = []
    for idx in range(0,len(best_actor_supporting)):
        if idx is 0:
            val = best_actor_supporting[idx].find('b').find('a')
        else:
            val = best_actor_supporting[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_supporting_list.append(actor_name)

    best_actress_supporting_col = best_actor_supporting_row.findall('td')[1]
    best_actress_supporting = best_actress_supporting_col.findall('.//li')

    best_actress_supporting_list = []
    for idx in range(0,len(best_actress_supporting)):
        if idx is 0:
            val = best_actress_supporting[idx].find('b').find('a')
        else:
            val = best_actress_supporting[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_supporting_list.append(actress_name)

    best_miniseries_row = wikitable.findall('tr')[16]
    best_miniseries_col = best_miniseries_row.findall('td')[0]
    best_miniseries = best_miniseries_col.findall('.//li')

    best_miniseries_list = []
    for idx in range(0,len(best_miniseries)):
        if idx is 0:
            val = best_miniseries[idx].find('i').find('b').find('a')
        else:
            val = best_miniseries[idx].find('i').find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        miniseries_title = val_split[0].strip()
        best_miniseries_list.append(miniseries_title)

    return [
    best_tv_drama_list,
    best_tv_mus_or_com_list,
    best_actor_drama_list,
    best_actress_drama_list,
    best_actor_com_mus_list,
    best_actress_com_mus_list,
    best_actor_miniseries_list,
    best_actress_miniseries_list,
    best_actor_supporting_list,
    best_actress_supporting_list,
    best_miniseries_list
    ]


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
