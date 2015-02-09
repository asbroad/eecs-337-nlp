#! /usr/bin/python
from read_tweets import read_in_tweets_2013, read_in_tweets_2015
from scrape_2013_data import parse_2013_wikipedia_movies, parse_2013_wikipedia_tv, parse_2013_wikipedia_presenters
from scrape_2015_data import parse_2015_wikipedia_movies, parse_2015_wikipedia_tv, parse_2015_wikipedia_presenters
from match_options import get_bigram_list_match_tweets, get_bigram_list_match_tweets_lax, get_bigram_list_match_tweets_either_or_lax, get_unigram_list_match_tweets_lax, get_unigram_list_match_tweets_either_or_lax, pairThings
from unused_files import get_academy_info # GET RID OF THIS BY USING SCRAPED DATA INSTEAD

'''
Some ideas...
1. Print out a visual of a timeline of the event (the 2013 data is about 4hrs of data) and print popularity of people at given time
points, maybe try and analyze if people's names show up as they are presenting or if the have just won or lost an award?
'''

''' main function '''
def main():
    ''' Twitter JSON files '''
    tweet_file = open('../data/goldenglobes.json','r')
    #tweet_file = open('../data/gg15trimmed.json','r') # this file doesn't work, because it take up too much memory to read in
    #tweet_file = open('../data/gg15mini.json','r')
    #tweet_file = open('gg15mini_half.json','r')

    ''' Read in JSON file '''
    tweets = read_in_tweets_2013(tweet_file)
    #tweets = read_in_tweets_2015(tweet_file)

    ''' Golden Globe Wikipedia XML files '''
    # xml_file_2013 = '70th_Golden_Globe_Awards.xml'
    # xml_file_2015 = '72nd_Golden_Globe_Awards.xml'

    ''' Lists of terms to search for in tweets by catagory '''
    ''' lot = List of Terms '''

    ''' OVERALL SECTION '''
    # HOSTS
    # BIGRAMS
    lot_hosts = ['host']

    ''' MOVIE SECTION '''
    # BEST MOVIE, DRAMA
    # UNIGRAM
    lot_best_drama_movie = ['best', 'picture'] # Number 3 response with this
    #lot_best_drama_movie_opt = ['film', 'movie']
    # BEST MOVIE, MUS OR COM
    # BIGRAM
    lot_best_mus_com_movie = ['best', 'picture'] # Number 3 response with this
    lot_best_mus_com_movie_opt = ['com', 'mus']
    # BEST ACTOR/ACTRESS, DRAMA
    # BIGRAMS
    lot_best_actor_drama_movie = ['best', 'drama', 'actor'] # Number 1 response with this
    lot_best_actress_drama_movie = ['best', 'drama', 'actress'] # Number 1 response with this
    lot_best_actress_drama_movie_opt = ['movie', 'film']
    # BEST ACTOR/ACTRESS, COMEDY OR MUSICAL
    # BIGRAMS
    lot_best_actor_mus_com = ['best', 'actor'] # Number 1 response with this
    lot_best_actor_mus_com_opt = ['com', 'mus']
    lot_best_actress_mus_com = ['best', 'actress'] # Number 1 response with this
    lot_best_actress_mus_com_opt = ['com', 'mus']
    # BEST SUPPORTING ACTOR/ACTRESS, ALL MOVIES
    # BIGRAMS
    lot_best_supporting_actor = ['best', 'support', 'actor'] # Number 1 response with this
    lot_best_supporting_actress = ['best', 'support', 'actress'] # Number 1 response with this
    # BEST DIRECTOR
    #BIGRAM
    lot_best_director = ['best', 'director'] # Number 1 response with this
    # BEST SCREENPLAY
    # BIGRAM
    lot_best_screenplay = ['best', 'screenplay'] # Number 1 response with this
    # BEST ORIGINAL SCORE
    # BIGRAM
    lot_best_original_score = ['best', 'original', 'score'] # Number 1 response with this
    # BEST ORIGINAL SONG
    # UNIGRAM
    lot_best_original_song = ['best', 'original', 'song'] # Number 1 response with this
    # BEST ANIMATED FEATURE FILM
    # UNIGRAM
    lot_best_animated_film = ['best', 'animated'] # Number 1 response with this
    # BEST FOREIGN LANGUAGE FILM
    # UNIGRAM
    lot_best_foreign_film = ['best', 'foreign', 'film', 'language'] # Number 1 response with this

    ''' TV SECTION '''
    # BEST TV, DRAMA
    # UNIGRAM
    lot_best_drama_tv = ['best', 'drama', 'tv'] # Number 1 response with this
    # BEST TV, MUS OR COM
    # UNIGRAM
    lot_best_mus_com_tv = ['best', 'series', 'com'] # Number 8 response with this
    # BEST ACTOR/ACTRESS, DRAMA
    # BIGRAMS - this one we may need to match up with the nominations
    lot_best_actor_drama_tv = ['best', 'drama', 'actor', 'show'] # Number 2 response with this
    # lot_best_actor_drama_tv = ['best', 'drama', 'actor'] # Number 3 response with this
    lot_best_actress_drama_tv = ['best', 'drama', 'actress'] # Number 1 response with this
    # BEST ACTOR/ACTRESS, COMEDY OR MUSICAL
    # BIGRAMS
    lot_best_actor_tv_mus_com = ['best', 'actor', 'tv'] # Number 1 response with this
    lot_best_actor_tv_mus_com_opt = ['com', 'mus']
    lot_best_actress_tv_mus_com = ['best', 'actress', 'tv'] # Number 1 response with this, but it's weak
    lot_best_actress_tv_mus_com_opt = ['com', 'mus']
    # BEST ACTOR/ACTRESS, MINISERIES/TV FILM
    lot_best_actor_miniseries = ['best', 'actor', 'miniseries'] # Number 1 response with this
    lot_best_actress_miniseries = ['best', 'actress', 'miniseries'] # Number 1 response with this
    # BEST SUPPORTING ACTOR/ACTRESS, ALL TV
    # BIGRAMS
    lot_best_supporting_actor_tv = ['best', 'support', 'actor', 'series'] # Number 1 response with this
    lot_best_supporting_actress_tv = ['best', 'support', 'actress', 'series'] # Tied for first like this
    # BEST MINISERIES or TV FILM
    # BIGRAMS
    lot_best_miniseries = ['best', 'miniseries'] # Number 3 response with this

    ''' Analysis '''

    ''' hosts '''
    res_hosts = get_bigram_list_match_tweets(tweets, lot_hosts)

    ''' movie awards '''
    # res_best_drama_movie = get_unigram_list_match_tweets_lax(tweets, lot_best_drama_movie)#, lot_best_drama_movie_opt)
    # res_best_mus_com_movie = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_mus_com_movie, lot_best_mus_com_movie_opt)
    # res_best_drama_actor = get_bigram_list_match_tweets_lax(tweets, lot_best_actor_drama_movie)
    # res_best_drama_actress = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actress_drama_movie, lot_best_actress_drama_movie_opt)
    # res_best_actor_mus_com = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actor_mus_com, lot_best_actor_mus_com_opt)
    # res_best_actress_mus_com = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actress_mus_com, lot_best_actress_mus_com_opt)
    # res_best_supporting_actor = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actor)
    # res_best_supporting_actress = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actress)
    # res_best_director = get_bigram_list_match_tweets_lax(tweets, lot_best_director)
    # res_best_screenplay = get_bigram_list_match_tweets_lax(tweets, lot_best_screenplay)
    # res_best_original_score = get_bigram_list_match_tweets_lax(tweets, lot_best_original_score)
    # res_best_original_song = get_unigram_list_match_tweets_lax(tweets, lot_best_original_song)
    # res_best_animated_film = get_unigram_list_match_tweets_lax(tweets, lot_best_animated_film)
    # res_best_foreign_film = get_unigram_list_match_tweets_lax(tweets, lot_best_foreign_film)
    #
    # ''' tv awards '''
    # res_best_drama_tv = get_unigram_list_match_tweets_lax(tweets, lot_best_drama_tv)
    # res_best_mus_com_tv = get_unigram_list_match_tweets_lax(tweets, lot_best_mus_com_tv)#, lot_best_mus_com_tv_opt)
    # res_best_drama_actor_tv = get_bigram_list_match_tweets_lax(tweets, lot_best_actor_drama_tv)
    # res_best_drama_actress_tv = get_bigram_list_match_tweets_lax(tweets, lot_best_actress_drama_tv)
    # res_best_actor_tv_mus_com = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actor_tv_mus_com, lot_best_actor_tv_mus_com_opt)
    # res_best_actress_tv_mus_com = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actress_tv_mus_com, lot_best_actress_tv_mus_com_opt)
    # res_best_actor_miniseries = get_bigram_list_match_tweets_lax(tweets, lot_best_actor_miniseries)
    # res_best_actress_miniseries = get_bigram_list_match_tweets_lax(tweets, lot_best_actress_miniseries)
    # res_best_supporting_actor_tv = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actor_tv)
    # res_best_supporting_actress_tv = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actress_tv)
    # res_best_miniseries = get_bigram_list_match_tweets_lax(tweets, lot_best_miniseries)

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
