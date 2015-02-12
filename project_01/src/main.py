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
    save_filename = 'output.json'

    [tweets, parsed_list, parsed_presenter_list] = load_data(year)

    ''' Analysis '''

    hosts = get_winner('host', tweets, parsed_list)

    all_winners = []

    award_title ='best movie drama'
    best_movie_drama = get_winner(award_title, tweets, parsed_list)
    best_movie_drama_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best movie musical or comedy'
    best_movie_musical_or_comedy = get_winner(award_title, tweets, parsed_list)
    best_movie_musical_or_comedy_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best actor drama'
    best_actor_drama = get_winner(award_title, tweets, parsed_list)
    best_actor_drama_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best actress drama'
    best_actress_drama = get_winner(award_title, tweets, parsed_list)
    best_actress_drama_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best actor musical or comedy'
    best_actor_musical_or_comedy = get_winner(award_title, tweets, parsed_list)
    best_actor_musical_or_comedy_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best actress musical or comedy'
    best_actress_musical_or_comedy = get_winner(award_title, tweets, parsed_list)
    best_actress_musical_or_comedy_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best supporting actor'
    best_supporting_actor = get_winner(award_title, tweets, parsed_list)
    best_supporting_actor_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best supporting actress'
    best_supporting_actress = get_winner(award_title, tweets, parsed_list)
    best_supporting_actress_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best director'
    best_director = get_winner(award_title, tweets, parsed_list)
    best_director_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best screenplay'
    best_screenplay = get_winner(award_title, tweets, parsed_list)
    best_screenplay_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best original score'
    best_original_score = get_winner(award_title, tweets, parsed_list)
    best_original_score_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best original song'
    best_original_song = get_winner(award_title, tweets, parsed_list)
    best_original_song_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best animated movie'
    best_animated_movie = get_winner(award_title, tweets, parsed_list)
    best_animated_movie_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best foreign movie'
    best_foreign_movie = get_winner(award_title, tweets, parsed_list)
    best_foreign_movie_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best tv series drama'
    best_tv_series_drama = get_winner(award_title, tweets, parsed_list)
    best_tv_series_drama_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best tv musical or comedy'
    best_tv_musical_or_comedy = get_winner(award_title, tweets, parsed_list)
    best_tv_musical_or_comedy_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best actor tv drama'
    best_actor_tv_drama = get_winner(award_title, tweets, parsed_list)
    best_actor_tv_drama_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best actress tv drama'
    best_actress_tv_drama = get_winner(award_title, tweets, parsed_list)
    best_actress_tv_drama_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best actor tv musical or comedy'
    best_actor_tv_musical_or_comedy = get_winner(award_title, tweets, parsed_list)
    best_actor_tv_musical_or_comedy_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best actress tv musical or comedy'
    best_actress_tv_musical_or_comedy = get_winner(award_title, tweets, parsed_list)
    best_actress_tv_musical_or_comedy_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best actor tv movie'
    best_actor_tv_movie = get_winner(award_title, tweets, parsed_list)
    best_actor_tv_movie_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best actress tv movie'
    best_actress_tv_movie = get_winner(award_title, tweets, parsed_list)
    best_actress_tv_movie_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best supporting actor tv movie'
    best_supporting_actor_tv_movie = get_winner(award_title, tweets, parsed_list)
    best_supporting_actor_tv_movie_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best supporting actress tv movie'
    best_supporting_actress_tv_movie = get_winner(award_title, tweets, parsed_list)
    best_supporting_actress_tv_movie_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    award_title = 'best tv movie'
    best_tv_movie = get_winner(award_title, tweets, parsed_list)
    best_tv_movie_noms = parsed_list.get(award_title)
    all_winners.append(best_movie_drama)

    save_output(hosts, all_winners, parsed_list.keys(), parsed_presenter_list[0], parsed_list.values(), save_filename)
    #save_output(hosts_in, all_winners_in, all_awards_in, all_presenters_in, all_nominees_in, output_filename)


def load_data(year='2013'):
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
    return [tweets, parsed_list, parsed_presenter_list]

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
