from read_tweets import *
from scrape_2013_data import *
from scrape_2015_data import *
from match_options import *
from get_winner import*
from save_output import *
from datetime import *

#What's the buzz?
#show starts at 5pm pacific time
#red carpet starts at 3ish?

def gg_hist(name, tweets, max_bins = 20):
	subSet = []
	bins = [list() for _ in xrange(max_bins)]
	for tweet in tweets:
		tweetText = tweet[0].lower()
		if match_all_words(tweetText, name.lower().split()):
			subSet.append(tweet)

	print(len(subSet))

	for tweet in subSet:
		bin = classifyTimeStamp(tweet, max_bins)
		bins[bin].append(tweet)

	return bins


def classifyTimeStamp(tweet, num_bins):
	val = tweet[1][0:-3]
	time = datetime.fromtimestamp(int(val))
	event_start = datetime(2015, 1, 11, 16, 0 ,0)
	diff = time - event_start
	bin_size = timedelta(minutes = 15)
	res = 0
	if diff < timedelta(0):
		#tweet before start of event
		return 0
	else:
		while diff > bin_size:
			res = res + 1
			diff = diff - bin_size
			#print(diff)
	
	if res > num_bins-1:
		res = num_bins-1


	return res

'''
def main():
	year = '2015'
	[tweets, parsed_list, parsed_presenter_list] = load_data(year)
	print("data Loaded")

	#bin = classifyTimeStamp(tweets[0])
	#print(bin)

	res = red_carpet_vs_gg("Amy Adams", tweets)
	for bin in res:
		print(len(bin))

def load_data(year='2013'):
    if year == '2013':
        tweet_file = open('../data/goldenglobes.json','r')
        tweets = read_in_tweets_2013(tweet_file)
        print("Tweets Loaded")
        xml_file_2013 = '70th_Golden_Globe_Awards.xml'
        parsed_movie_list = parse_2013_wikipedia_movies(xml_file_2013)
        parsed_tv_list = parse_2013_wikipedia_tv(xml_file_2013)
        parsed_presenter_list = parse_2013_wikipedia_presenters(xml_file_2013)
        parsed_list = dict(parsed_movie_list.items() + parsed_tv_list.items())
        print("XML Parsed")
    elif year == '2015':
        #tweet_file = open('../data/gg15trimmed.json','r') # this file doesn't work, because it take up too much memory to read in
        tweet_file = open('../data/gg15mini_half.json','r')
        #tweet_file = open('gg15mini_half.json','r')
        tweets = read_in_tweets_2015(tweet_file)
        print("Tweets Loaded")
        xml_file_2015 = '72nd_Golden_Globe_Awards.xml'
        parsed_movie_list = parse_2015_wikipedia_movies(xml_file_2015)
        parsed_tv_list = parse_2015_wikipedia_tv(xml_file_2015)
        parsed_presenter_list = parse_2015_wikipedia_presenters(xml_file_2015)
        parsed_list = dict(parsed_movie_list.items() + parsed_tv_list.items())
        print("XML Parsed")
    return [tweets, parsed_list, parsed_presenter_list]


if __name__ == "__main__":
    main()
'''