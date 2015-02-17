#! /usr/bin/python
from read_tweets import *
from scrape_2013_data import *
from scrape_2015_data import *
from match_options import *
from get_winner import*
from save_output import *
from pair_winners_to_movies import *
import operator
import nltk

''' main function '''
def main():

    year = '2015'
    save_filename = 'test.json'

    [tweets, parsed_list, parsed_presenter_list] = load_data(year)

    ''' Analysis '''

    hosts = get_winner('host', tweets, parsed_list)

    all_winners = []
    all_nominees = []
    all_structured_awards = []

    ##########################################################

    award_title = 'Best Motion Picture - Drama'
    best_movie_drama = get_winner(award_title, tweets, parsed_list)
    best_movie_drama_noms = parsed_list.get(award_title)
    best_movie_drama_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_movie_drama)
    all_nominees.append(best_movie_drama_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_movie_drama_noms
    temp_dict['winner'] = best_movie_drama
    temp_dict['presenters'] = best_movie_drama_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Motion Picture - Comedy Or Musical'
    best_movie_musical_or_comedy = get_winner(award_title, tweets, parsed_list)
    best_movie_musical_or_comedy_noms = parsed_list.get(award_title)
    best_movie_musical_or_comedy_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_movie_musical_or_comedy)
    all_nominees.append(best_movie_musical_or_comedy_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_movie_musical_or_comedy_noms
    temp_dict['winner'] = best_movie_musical_or_comedy
    temp_dict['presenters'] = best_movie_musical_or_comedy_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Performance by an Actor in a Motion Picture - Drama'
    best_actor_drama = get_winner(award_title, tweets, parsed_list)
    best_actor_drama_noms = parsed_list.get(award_title)
    best_actor_drama_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_actor_drama)
    all_nominees.append(best_actor_drama_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_actor_drama_noms
    temp_dict['winner'] = best_actor_drama
    temp_dict['presenters'] = best_actor_drama_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Performance by an Actress in a Motion Picture - Drama'
    best_actress_drama = get_winner(award_title, tweets, parsed_list)
    best_actress_drama_noms = parsed_list.get(award_title)
    best_actress_drama_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_actress_drama)
    all_nominees.append(best_actress_drama_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_actress_drama_noms
    temp_dict['winner'] = best_actress_drama
    temp_dict['presenters'] = best_actress_drama_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Performance by an Actor in a Motion Picture - Comedy Or Musical'
    best_actor_musical_or_comedy = get_winner(award_title, tweets, parsed_list)
    best_actor_musical_or_comedy_noms = parsed_list.get(award_title)
    best_actor_musical_or_comedy_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_actor_musical_or_comedy)
    all_nominees.append(best_actor_musical_or_comedy_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_actor_musical_or_comedy_noms
    temp_dict['winner'] = best_actor_musical_or_comedy
    temp_dict['presenters'] = best_actor_musical_or_comedy_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Performance by an Actress in a Motion Picture - Comedy Or Musical'
    best_actress_musical_or_comedy = get_winner(award_title, tweets, parsed_list)
    best_actress_musical_or_comedy_noms = parsed_list.get(award_title)
    best_actress_musical_or_comedy_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_actress_musical_or_comedy)
    all_nominees.append(best_actress_musical_or_comedy_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_actress_musical_or_comedy_noms
    temp_dict['winner'] = best_actress_musical_or_comedy
    temp_dict['presenters'] = best_actress_musical_or_comedy_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Performance by an Actor In A Supporting Role in a Motion Picture'
    best_supporting_actor = get_winner(award_title, tweets, parsed_list)
    best_supporting_actor_noms = parsed_list.get(award_title)
    best_supporting_actor_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_supporting_actor)
    all_nominees.append(best_supporting_actor_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_supporting_actor_noms
    temp_dict['winner'] = best_supporting_actor
    temp_dict['presenters'] = best_supporting_actor_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Performance by an Actress In A Supporting Role in a Motion Picture'
    best_supporting_actress = get_winner(award_title, tweets, parsed_list)
    best_supporting_actress_noms = parsed_list.get(award_title)
    best_supporting_actress_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_supporting_actress)
    all_nominees.append(best_supporting_actress_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_supporting_actress_noms
    temp_dict['winner'] = best_supporting_actress
    temp_dict['presenters'] = best_supporting_actress_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Director - Motion Picture'
    best_director = get_winner(award_title, tweets, parsed_list)
    best_director_noms = parsed_list.get(award_title)
    best_director_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_director)
    all_nominees.append(best_director_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_director_noms
    temp_dict['winner'] = best_director
    temp_dict['presenters'] = best_director_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Screenplay - Motion Picture'
    best_screenplay = get_winner(award_title, tweets, parsed_list)
    best_screenplay_noms = parsed_list.get(award_title)
    [best_screenplay, best_screenplay_noms] = fix_names_to_movie(year, award_title, best_screenplay_noms, best_screenplay)
    best_screenplay_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_screenplay)
    all_nominees.append(best_screenplay_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_screenplay_noms
    temp_dict['winner'] = best_screenplay
    temp_dict['presenters'] = best_screenplay_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Original Score - Motion Picture'
    best_original_score = get_winner(award_title, tweets, parsed_list)
    best_original_score_noms = parsed_list.get(award_title)
    [best_original_score, best_original_score_noms] = fix_names_to_movie(year, award_title, best_original_score_noms, best_original_score)
    best_original_score_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_original_score)
    all_nominees.append(best_original_score_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_original_score_noms
    temp_dict['winner'] = best_original_score
    temp_dict['presenters'] = best_original_score_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Original Song - Motion Picture'
    best_original_song = get_winner(award_title, tweets, parsed_list)
    best_original_song_noms = parsed_list.get(award_title)
    [best_original_song, best_original_song_noms] = fix_names_to_movie(year, award_title, best_original_song_noms, best_original_song)
    best_original_song_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_original_song)
    all_nominees.append(best_original_song_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_original_song_noms
    temp_dict['winner'] = best_original_song
    temp_dict['presenters'] = best_original_song_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Animated Feature Film'
    best_animated_movie = get_winner(award_title, tweets, parsed_list)
    best_animated_movie_noms = parsed_list.get(award_title)
    best_animated_movie_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_animated_movie)
    all_nominees.append(best_animated_movie_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_animated_movie_noms
    temp_dict['winner'] = best_animated_movie
    temp_dict['presenters'] = best_animated_movie_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Foreign Language Film'
    best_foreign_movie = get_winner(award_title, tweets, parsed_list)
    best_foreign_movie_noms = parsed_list.get(award_title)
    best_foreign_movie_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_foreign_movie)
    all_nominees.append(best_foreign_movie_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_foreign_movie_noms
    temp_dict['winner'] = best_foreign_movie
    temp_dict['presenters'] = best_foreign_movie_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Television Series - Drama'
    best_tv_series_drama = get_winner(award_title, tweets, parsed_list)
    best_tv_series_drama_noms = parsed_list.get(award_title)
    best_tv_series_drama_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_tv_series_drama)
    all_nominees.append(best_tv_series_drama_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_tv_series_drama_noms
    temp_dict['winner'] = best_tv_series_drama
    temp_dict['presenters'] = best_tv_series_drama_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Television Series - Comedy Or Musical'
    best_tv_musical_or_comedy = get_winner(award_title, tweets, parsed_list)
    best_tv_musical_or_comedy_noms = parsed_list.get(award_title)
    best_tv_musical_or_comedy_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_tv_musical_or_comedy)
    all_nominees.append(best_tv_musical_or_comedy_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_tv_musical_or_comedy_noms
    temp_dict['winner'] = best_tv_musical_or_comedy
    temp_dict['presenters'] = best_tv_musical_or_comedy_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Performance by an Actor In A Television Series - Drama'
    best_actor_tv_drama = get_winner(award_title, tweets, parsed_list)
    best_actor_tv_drama_noms = parsed_list.get(award_title)
    best_actor_tv_drama_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_actor_tv_drama)
    all_nominees.append(best_actor_tv_drama_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_actor_tv_drama_noms
    temp_dict['winner'] = best_actor_tv_drama
    temp_dict['presenters'] = best_actor_tv_drama_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Performance by an Actress In A Television Series - Drama'
    best_actress_tv_drama = get_winner(award_title, tweets, parsed_list)
    best_actress_tv_drama_noms = parsed_list.get(award_title)
    best_actress_tv_drama_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_actress_tv_drama)
    all_nominees.append(best_actress_tv_drama_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_actress_tv_drama_noms
    temp_dict['winner'] = best_actress_tv_drama
    temp_dict['presenters'] = best_actress_tv_drama_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Performance by an Actor In A Television Series - Comedy Or Musical'
    best_actor_tv_musical_or_comedy = get_winner(award_title, tweets, parsed_list)
    best_actor_tv_musical_or_comedy_noms = parsed_list.get(award_title)
    best_actor_tv_musical_or_comedy_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_actor_tv_musical_or_comedy)
    all_nominees.append(best_actor_tv_musical_or_comedy_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_actor_tv_musical_or_comedy_noms
    temp_dict['winner'] = best_actor_tv_musical_or_comedy
    temp_dict['presenters'] = best_actor_tv_musical_or_comedy_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Performance by an Actress In A Television Series - Comedy Or Musical'
    best_actress_tv_musical_or_comedy = get_winner(award_title, tweets, parsed_list)
    best_actress_tv_musical_or_comedy_noms = parsed_list.get(award_title)
    best_actress_tv_musical_or_comedy_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_actress_tv_musical_or_comedy)
    all_nominees.append(best_actress_tv_musical_or_comedy_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_actress_tv_musical_or_comedy_noms
    temp_dict['winner'] = best_actress_tv_musical_or_comedy
    temp_dict['presenters'] = best_actress_tv_musical_or_comedy_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Performance by an Actor in a Mini-Series or Motion Picture Made for Television'
    best_actor_tv_movie = get_winner(award_title, tweets, parsed_list)
    best_actor_tv_movie_noms = parsed_list.get(award_title)
    best_actor_tv_movie_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_actor_tv_movie)
    all_nominees.append(best_actor_tv_movie_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_actor_tv_movie_noms
    temp_dict['winner'] = best_actor_tv_movie
    temp_dict['presenters'] = best_actor_tv_movie_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Performance by an Actress In A Mini-series or Motion Picture Made for Television'
    best_actress_tv_movie = get_winner(award_title, tweets, parsed_list)
    best_actress_tv_movie_noms = parsed_list.get(award_title)
    best_actress_tv_movie_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_actress_tv_movie)
    all_nominees.append(best_actress_tv_movie_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_actress_tv_movie_noms
    temp_dict['winner'] = best_actress_tv_movie
    temp_dict['presenters'] = best_actress_tv_movie_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television'
    best_supporting_actor_tv_movie = get_winner(award_title, tweets, parsed_list)
    best_supporting_actor_tv_movie_noms = parsed_list.get(award_title)
    best_supporting_actor_tv_movie_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_supporting_actor_tv_movie)
    all_nominees.append(best_supporting_actor_tv_movie_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_supporting_actor_tv_movie_noms
    temp_dict['winner'] = best_supporting_actor_tv_movie
    temp_dict['presenters'] = best_supporting_actor_tv_movie_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television'
    best_supporting_actress_tv_movie = get_winner(award_title, tweets, parsed_list)
    best_supporting_actress_tv_movie_noms = parsed_list.get(award_title)
    best_supporting_actress_tv_movie_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_supporting_actress_tv_movie)
    all_nominees.append(best_supporting_actress_tv_movie_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_supporting_actress_tv_movie_noms
    temp_dict['winner'] = best_supporting_actress_tv_movie
    temp_dict['presenters'] = best_supporting_actress_tv_movie_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    award_title = 'Best Mini-Series Or Motion Picture Made for Television'
    best_tv_movie = get_winner(award_title, tweets, parsed_list)
    best_tv_movie_noms = parsed_list.get(award_title)
    best_tv_movie_presenter = get_presenter_from_award(award_title, parsed_presenter_list)
    all_winners.append(best_tv_movie)
    all_nominees.append(best_tv_movie_noms)

    temp_dict = {}
    temp_dict['nominees'] = best_tv_movie_noms
    temp_dict['winner'] = best_tv_movie
    temp_dict['presenters'] = best_tv_movie_presenter

    structured_award = {award_title: temp_dict}
    all_structured_awards.append(structured_award)

    ##########################################################

    parsed_presenter_list_joined = reduce(operator.add, parsed_presenter_list[0])
    #parsed_nominee_list_joined =  reduce(operator.add, parsed_list.values())
    parsed_nominee_list_joined = reduce(operator.add, all_nominees)

    save_output(year, hosts, all_winners, parsed_list.keys(), parsed_presenter_list_joined, parsed_nominee_list_joined, all_structured_awards, save_filename)
    #save_output(year, hosts_in, all_winners_in, all_awards_in, all_presenters_in, all_nominees_in, all_structured_awards_in, output_filename)


def get_presenter_from_award(award, parsed_presenter_list):
    blacklist = set(['In', 'A', 'Or', 'Made', 'Series', 'Film', 'Role', 'Performance', 'Mr.', 'Miss','Golden','Globe,','Best', 'Globe'])
    special_list = set(['television','score','song','screenplay'])
    split_award = award.split()
    award = [word.lower() for word in split_award if ord(word[0]) > 0x40 and ord(word[0]) < 0x5B and word not in blacklist]
    for idx in xrange(len(parsed_presenter_list[1])):
        phrases = parsed_presenter_list[1][idx][0].split(' and Best ')
        main_words = [[word.lower() for word in phrases[0].split() if ord(word[0]) > 0x40 and ord(word[0]) < 0x5B and word not in blacklist]]
        try:
            main_words.append([word.lower() for word in phrases[1].split() if ord(word[0]) > 0x40 and ord(word[0]) < 0x5B and word not in blacklist])
        except IndexError:
            pass
        for main in main_words:
            if main[-1] in special_list:
                main.append('motion')
                main.append('picture')
            current_different = get_current_difference(award, main)
            if current_different == 0:
                return parsed_presenter_list[0][idx]

    return 'No match found'



def get_current_difference(true_award, parsed_award):
    t_award_diff = 0
    p_award_diff = 0

    for award in true_award:
        is_same = False
        for paward in parsed_award:
            if nltk.edit_distance(award, paward) <= 1:
                is_same = True
                break
        if not is_same:
            t_award_diff += 1

    for award in parsed_award:
        is_same = False
        for taward in true_award:
            if nltk.edit_distance(award, taward) <= 1:
                is_same = True
                break
        if not is_same:
            p_award_diff += 1

    return t_award_diff + p_award_diff



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
