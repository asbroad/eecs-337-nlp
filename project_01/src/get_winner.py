#! /usr/bin/python
from read_tweets import *
from scrape_2013_data import *
from scrape_2015_data import *
from match_options import *

def get_winner(category, tweets, parsed_list, qty = 1):

    if category == 'host':
        lot_hosts = ['host']
        res = get_bigram_list_match_tweets(tweets, lot_hosts)
        hs = res[0:2]
        return [name[0] for name in hs]

    if category == 'Best Motion Picture - Drama':
        lot_best_drama_movie = ['best', 'picture'] # Number 3 response with this
        res = get_unigram_list_match_tweets_lax(tweets, lot_best_drama_movie)#, lot_best_drama_movie_opt)

    if category == 'Best Performance by an Actress in a Motion Picture - Drama':
        lot_best_actress_drama_movie = ['best', 'drama', 'actress'] # Number 1 response with this
        lot_best_actress_drama_movie_opt = ['movie', 'film']
        res = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actress_drama_movie, lot_best_actress_drama_movie_opt)

    if category == 'Best Performance by an Actor in a Motion Picture - Drama':
        lot_best_actor_drama_movie = ['best', 'drama', 'actor'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_actor_drama_movie)

    if category == 'Best Motion Picture - Comedy Or Musical':
        lot_best_mus_com_movie = ['best', 'picture'] # Number 3 response with this
        lot_best_mus_com_movie_opt = ['com', 'mus']
        res = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_mus_com_movie, lot_best_mus_com_movie_opt)

    if category == 'Best Performance by an Actress in a Motion Picture - Comedy Or Musical':
        lot_best_actress_mus_com = ['best', 'actress'] # Number 1 response with this
        lot_best_actress_mus_com_opt = ['com', 'mus']
        res = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actress_mus_com, lot_best_actress_mus_com_opt)

    if category == 'Best Performance by an Actor in a Motion Picture - Comedy Or Musical':
        lot_best_actor_mus_com = ['best', 'actor'] # Number 1 response with this
        lot_best_actor_mus_com_opt = ['com', 'mus']
        res = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actor_mus_com, lot_best_actor_mus_com_opt)

    if category == 'Best Animated Feature Film':
        lot_best_animated_film = ['best', 'animated'] # Number 1 response with this
        res = get_unigram_list_match_tweets_lax(tweets, lot_best_animated_film)

    if category == 'Best Foreign Language Film':
        lot_best_foreign_film = ['best', 'foreign', 'film', 'language'] # Number 1 response with this
        res = get_unigram_list_match_tweets_lax(tweets, lot_best_foreign_film)

    if category == 'Best Performance by an Actress In A Supporting Role in a Motion Picture':
        lot_best_supporting_actress = ['best', 'support', 'actress'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actress)

    if category == 'Best Performance by an Actor In A Supporting Role in a Motion Picture':
        lot_best_supporting_actor = ['best', 'support', 'actor'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actor)

    if category == 'Best Director - Motion Picture':
        lot_best_director = ['best', 'director'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_director)

    if category == 'Best Screenplay - Motion Picture':
        lot_best_screenplay = ['best', 'screenplay'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_screenplay)

    if category == 'Best Original Score - Motion Picture':
        lot_best_original_score = ['best', 'original', 'score'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_original_score)

    if category == 'Best Original Song - Motion Picture':
        lot_best_original_song = ['best', 'original', 'song'] # Number 1 response with this
        res = get_unigram_list_match_tweets_lax(tweets, lot_best_original_song)

    if category == 'Best Television Series - Drama':
        lot_best_drama_tv = ['best', 'drama', 'tv'] # Number 1 response with this
        res = get_unigram_list_match_tweets_lax(tweets, lot_best_drama_tv)

    if category == 'Best Performance by an Actress In A Television Series - Drama':
        lot_best_actress_drama_tv = ['best', 'drama', 'actress'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_actress_drama_tv)

    if category == 'Best Performance by an Actor In A Television Series - Drama':
        lot_best_actor_drama_tv = ['best', 'drama', 'actor', 'show']
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_actor_drama_tv)

    if category == 'Best Television Series - Comedy Or Musical':
        lot_best_mus_com_tv = ['best', 'series', 'com'] # Number 8 response with this
        res = get_unigram_list_match_tweets_lax(tweets, lot_best_mus_com_tv)#, lot_best_mus_com_tv_opt)

    if category == 'Best Performance by an Actress In A Television Series - Comedy Or Musical':
        lot_best_actress_tv_mus_com = ['best', 'actress', 'tv'] # Number 1 response with this, but it's weak
        lot_best_actress_tv_mus_com_opt = ['com', 'mus']
        res = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actress_tv_mus_com, lot_best_actress_tv_mus_com_opt)

    if category == 'Best Performance by an Actor In A Television Series - Comedy Or Musical':
        lot_best_actor_tv_mus_com = ['best', 'actor', 'tv'] # Number 1 response with this
        lot_best_actor_tv_mus_com_opt = ['com', 'mus']
        res = get_bigram_list_match_tweets_either_or_lax(tweets, lot_best_actor_tv_mus_com, lot_best_actor_tv_mus_com_opt)

    if category == 'Best Mini-Series Or Motion Picture Made for Television':
        lot_best_miniseries = ['best', 'miniseries'] # Number 3 response with this
        res = get_unigram_list_match_tweets_lax(tweets, lot_best_miniseries)

    if category == 'Best Performance by an Actress In A Mini-series or Motion Picture Made for Television':
        lot_best_actress_miniseries = ['best', 'actress', 'miniseries'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_actress_miniseries)

    if category == 'Best Performance by an Actor in a Mini-Series or Motion Picture Made for Television':
        lot_best_actor_miniseries = ['best', 'actor', 'miniseries'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_actor_miniseries)

    if category == 'Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television':
        lot_best_supporting_actress_tv = ['best', 'support', 'actress', 'series'] # Tied for first like this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actress_tv)

    if category == 'Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television':
        lot_best_supporting_actor_tv = ['best', 'support', 'actor', 'series'] # Number 1 response with this
        res = get_bigram_list_match_tweets_lax(tweets, lot_best_supporting_actor_tv)

    # return get_best_match(res[0], parsed_list[category][:])[0:qty]
    return get_best_match(res, parsed_list[category][:])#[0:qty]
