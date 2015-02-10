#! /usr/bin/python
from read_tweets import *
from scrape_2013_data import *
from scrape_2015_data import *
from match_options import *

def get_winner(category, tweets, parsed_list, qty = 1):

    if category == 'host':
        lot_hosts = ['host']
        res = get_bigram_list_match_tweets(tweets, lot_hosts)
        return res[0:2]

    if category == 'best movie drama':
        lot_best_drama_movie = ['best', 'picture'] # Number 3 response with this
        res = get_unigram_list_match_tweets_lax(tweets, lot_best_drama_movie)#, lot_best_drama_movie_opt)

    if category == 'best actress drama':
        lot_best_actress_drama_movie = ['best', 'drama', 'actress'] # Number 1 response with this
        lot_best_actress_drama_movie_opt = ['movie', 'film']
        res = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actress_drama_movie, lot_best_actress_drama_movie_opt)

    if category == 'best actor drama':
        lot_best_actor_drama_movie = ['best', 'drama', 'actor'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_actor_drama_movie)

    if category == 'best movie musical or comedy':
        lot_best_mus_com_movie = ['best', 'picture'] # Number 3 response with this
        lot_best_mus_com_movie_opt = ['com', 'mus']
        res = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_mus_com_movie, lot_best_mus_com_movie_opt)

    if category == 'best actress musical or comedy':
        lot_best_actress_mus_com = ['best', 'actress'] # Number 1 response with this
        lot_best_actress_mus_com_opt = ['com', 'mus']
        res = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actress_mus_com, lot_best_actress_mus_com_opt)

    if category == 'best actor musical or comedy':
        lot_best_actor_mus_com = ['best', 'actor'] # Number 1 response with this
        lot_best_actor_mus_com_opt = ['com', 'mus']
        res = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actor_mus_com, lot_best_actor_mus_com_opt)

    if category == 'best animated movie':
        lot_best_animated_film = ['best', 'animated'] # Number 1 response with this
        res = get_unigram_list_match_tweets_lax(tweets, lot_best_animated_film)

    if category == 'best foreign movie':
        lot_best_foreign_film = ['best', 'foreign', 'film', 'language'] # Number 1 response with this
        res = get_unigram_list_match_tweets_lax(tweets, lot_best_foreign_film)

    if category == 'best supporting actress':
        lot_best_supporting_actress = ['best', 'support', 'actress'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actress)

    if category == 'best supporting actor':
        lot_best_supporting_actor = ['best', 'support', 'actor'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actor)

    if category == 'best director':
        lot_best_director = ['best', 'director'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_director)

    if category == 'best screenplay':
        lot_best_screenplay = ['best', 'screenplay'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_screenplay)

    if category == 'best original score':
        lot_best_original_score = ['best', 'original', 'score'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_original_score)

    if category == 'best original song':
        lot_best_original_song = ['best', 'original', 'song'] # Number 1 response with this
        res = get_unigram_list_match_tweets_lax(tweets, lot_best_original_song)

    if category == 'best tv series drama':
        lot_best_drama_tv = ['best', 'drama', 'tv'] # Number 1 response with this
        res = get_unigram_list_match_tweets_lax(tweets, lot_best_drama_tv)

    if category == 'best actress tv drama':
        lot_best_actress_drama_tv = ['best', 'drama', 'actress'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_actress_drama_tv)

    if category == 'best actor tv drama':
        lot_best_actor_drama_tv = ['best', 'drama', 'actor', 'show']
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_actor_drama_tv)

    if category == 'best tv musical or comedy':
        lot_best_mus_com_tv = ['best', 'series', 'com'] # Number 8 response with this
        res = get_unigram_list_match_tweets_lax(tweets, lot_best_mus_com_tv)#, lot_best_mus_com_tv_opt)

    if category == 'best actress tv musical or comedy':
        lot_best_actress_tv_mus_com = ['best', 'actress', 'tv'] # Number 1 response with this, but it's weak
        lot_best_actress_tv_mus_com_opt = ['com', 'mus']
        res = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actress_tv_mus_com, lot_best_actress_tv_mus_com_opt)

    if category == 'best actor tv musical or comedy':
        lot_best_actor_tv_mus_com = ['best', 'actor', 'tv'] # Number 1 response with this
        lot_best_actor_tv_mus_com_opt = ['com', 'mus']
        res = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actor_tv_mus_com, lot_best_actor_tv_mus_com_opt)

    if category == 'best tv movie':
        lot_best_miniseries = ['best', 'miniseries'] # Number 3 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_miniseries)

    if category == 'best actress tv movie':
        lot_best_actress_miniseries = ['best', 'actress', 'miniseries'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_actress_miniseries)

    if category == 'best actor tv movie':
        lot_best_actor_miniseries = ['best', 'actor', 'miniseries'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_actor_miniseries)

    if category == 'best supporting actress tv movie':
        lot_best_supporting_actress_tv = ['best', 'support', 'actress', 'series'] # Tied for first like this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actress_tv)

    if category == 'best supporting actor tv movie':
        lot_best_supporting_actor_tv = ['best', 'support', 'actor', 'series'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actor_tv)

    return get_best_match(res[0], parsed_list[category][:])[0:qty]
