#! /usr/bin/python
from read_tweets import *# read_in_tweets_2013, read_in_tweets_2015
from scrape_2013_data import *# parse_2013_wikipedia_movies, parse_2013_wikipedia_tv, parse_2013_wikipedia_presenters
from scrape_2015_data import *# parse_2015_wikipedia_movies, parse_2015_wikipedia_tv, parse_2015_wikipedia_presenters
from match_options import *#get_best_match, get_bigram_list_match_tweets, get_bigram_list_match_tweets_lax, get_bigram_list_match_tweets_either_or_lax, get_unigram_list_match_tweets_lax, get_unigram_list_match_tweets_either_or_lax, pairThings

def get_winner(category, tweets, parsed_list):
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

    query_options = {}
    #Movie
    query_options['best movie drama'] = get_unigram_list_match_tweets_lax(tweets, lot_best_drama_movie)#, lot_best_drama_movie_opt)
    query_options['best actress drama'] = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actress_drama_movie, lot_best_actress_drama_movie_opt)
    query_options['best actor drama'] = get_bigram_list_match_tweets_lax(tweets, lot_best_actor_drama_movie)
    query_options['best movie musical or comedy'] = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_mus_com_movie, lot_best_mus_com_movie_opt)
    query_options['best actress musical or comedyres_best_actress'] = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actress_mus_com, lot_best_actress_mus_com_opt)
    query_options['best actor musical or comedyres_best_actor'] = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actor_mus_com, lot_best_actor_mus_com_opt)
    query_options['best animated movie'] = get_unigram_list_match_tweets_lax(tweets, lot_best_animated_film)
    query_options['best foreign movie'] = get_unigram_list_match_tweets_lax(tweets, lot_best_foreign_film)
    query_options['best supporting actress'] = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actress)
    query_options['best supporting actor'] = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actor)
    query_options['best director'] = get_bigram_list_match_tweets_lax(tweets, lot_best_director)
    query_options['best screenplay'] = get_bigram_list_match_tweets_lax(tweets, lot_best_screenplay)
    query_options['best original score'] = get_bigram_list_match_tweets_lax(tweets, lot_best_original_score)
    query_options['best original song'] = get_unigram_list_match_tweets_lax(tweets, lot_best_original_song)
    #TV
    query_options['best tv series drama'] = get_unigram_list_match_tweets_lax(tweets, lot_best_drama_tv)
    query_options['best actress tv drama'] = get_bigram_list_match_tweets_lax(tweets, lot_best_actress_drama_tv)
    query_options['best actor tv drama'] = get_bigram_list_match_tweets_lax(tweets, lot_best_actor_drama_tv)
    query_options['best tv musical or comedy'] = get_unigram_list_match_tweets_lax(tweets, lot_best_mus_com_tv)#, lot_best_mus_com_tv_opt)
    query_options['best actress tv musical or comedy'] = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actress_tv_mus_com, lot_best_actress_tv_mus_com_opt)
    query_options['best actor tv musical or comedy'] = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actor_tv_mus_com, lot_best_actor_tv_mus_com_opt)
    query_options['best tv movie'] = get_bigram_list_match_tweets_lax(tweets, lot_best_miniseries)
    query_options['best actress tv movie'] = get_bigram_list_match_tweets_lax(tweets, lot_best_actress_miniseries)
    query_options['best actor tv movie'] = get_bigram_list_match_tweets_lax(tweets, lot_best_actress_miniseries)
    query_options['best supporting actress tv movie'] = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actress_tv)
    query_options['best supporting actor tv movie'] = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actor_tv)
    
    return get_best_match(query_options[category][0], parsed_list[category][:])

