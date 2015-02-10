#! /usr/bin/python
from read_tweets import *
from scrape_2013_data import *
from scrape_2015_data import *
from match_options import *
from get_winner import*
from save_output import *
'''
Some ideas...
1. Print out a visual of a timeline of the event (the 2013 data is about 4hrs of data) and print popularity of people at given time
points, maybe try and analyze if people's names show up as they are presenting or if the have just won or lost an award?
'''

''' main function '''
def main():

    year = '2013'

    if year == '2013':
        ''' Twitter JSON files '''
        tweet_file = open('../data/goldenglobes.json','r')
        ''' Read in JSON file '''
        tweets = read_in_tweets_2013(tweet_file)
        print("Tweets Loaded")
        ''' Golden Globe Wikipedia XML files '''
        xml_file_2013 = '70th_Golden_Globe_Awards.xml'
        ''' Parse Wiki Pages '''
        parsed_movie_list = parse_2013_wikipedia_movies(xml_file_2013)
        parsed_tv_list = parse_2013_wikipedia_tv(xml_file_2013)
        parsed_presenter_list = parse_2013_wikipedia_presenters(xml_file_2013)
        parsed_list = dict(parsed_movie_list.items() + parsed_tv_list.items())
        print("XML Parsed")
    elif year == '2015':
        ''' Twitter JSON files '''
        #tweet_file = open('../data/gg15trimmed.json','r') # this file doesn't work, because it take up too much memory to read in
        tweet_file = open('../data/gg15mini.json','r')
        #tweet_file = open('gg15mini_half.json','r')
        ''' Read in JSON file '''
        tweets = read_in_tweets_2015(tweet_file)
        print("Tweets Loaded")
        ''' Golden Globe Wikipedia XML files '''
        xml_file_2015 = '72nd_Golden_Globe_Awards.xml'
        ''' Parse Wiki Pages '''
        parsed_movie_list = parse_2015_wikipedia_movies(xml_file_2015)
        parsed_tv_list = parse_2015_wikipedia_tv(xml_file_2015)
        parsed_presenter_list = parse_2015_wikipedia_presenters(xml_file_2015)
        parsed_list = dict(parsed_movie_list.items() + parsed_tv_list.items())
        print("XML Parsed")

    # 'hosts need to be put back in'
    catagories = [
        'best movie drama',
        'best actress drama',
        'best actor drama'
        # 'best movie musical or comedy',
        # 'best actress musical or comedy',
        # 'best actor musical or comedy',
        # 'best animated movie',
        # 'best foreign movie',
        # 'best supporting actress',
        # 'best supporting actor',
        # 'best director',
        # 'best screenplay',
        # 'best original score',
        # 'best original song',
        # 'best tv series drama',
        # 'best actress tv drama',
        # 'best actor tv drama',
        # 'best tv musical or comedy',
        # 'best actress tv musical or comedy',
        # 'best actor tv musical or comedy',
        # 'best tv movie',
        # 'best actress tv movie',
        # 'best actor tv movie',
        # 'best supporting actress tv movie',
        # 'best supporting actor tv movie'
    ]

    for cat in catagories:
        winner = get_winner(cat, tweets, parsed_list)
        print(winner)


    #Pair award does not work yet, the function definition is commented out
    #res = pairAward('best movie drama', parsed_presenter_list[0], tweets)
    #print(res)

    #winner = get_winner('best movie drama', tweets, parsed_list)
    #print(winner)

    #print(parsed_presenter_list.items)


    #pairWinner(winner, parsed_presenter_list['best movie drama'])


    # ''' Testing Matching Code '''
    # tweet_file = open('gg15mini_half.json','r')
    # tweets = read_in_tweets_2015(tweet_file)
    # academyInfo = get_academy_info()
    # truthData = academyInfo[0]
    # topic = "best movie drama"
    # res = pairThings(topic, truthData[topic], tweets)
    # print(res)


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

if __name__ == "__main__":
    main()
