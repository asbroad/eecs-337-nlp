from read_tweets import *
from scrape_2013_data import *
from scrape_2015_data import *
from match_options import *
from get_winner import*
from save_output import *
from datetime import *
import random

#What's the buzz?
#show starts at 5pm pacific time
#red carpet starts at 3ish?

ignore_list = ['will', 'ferrell', 'kristen', 'wiig', 'bill', 'hader', 'golden', 'globes', 'globe', 'goldenglobes', '#goldenglobes', 'oscars']


def find_subset(name, tweetsIn):
	subSet = []
	for tweet in tweetsIn:
		tweetText = tweet[0].lower()
		if match_all_words(tweetText, name.lower().split()):
			subSet.append(tweet)
	return subSet


def gg_typical_tweet(name, tweetsIn):
	if(len(tweetsIn) < 100):
		print("Warning: Low Number of tweets. Tweet will be partially generated with default values.")
	random.shuffle(tweetsIn)
	sampledTweets = tweetsIn[0:min(2000, len(tweetsIn))]
	top_hashtags = find_hashtag(sampledTweets)
	other = get_bigram_list_match_tweets(sampledTweets, name.split())[1][0]
	if len(top_hashtags) >= 3:
		hashtags = random.sample(set(top_hashtags[0:min(10, len(top_hashtags))]), 3)
	else:
		hashtags = [("#goldenglobes", -1), ("#redcarpet", -1), ("#gg", -1)]
		for idx in range(0,len(top_hashtags)):
			hashtags[idx] = top_hashtags[idx]
	myTweet = "{} at the #goldenglobes2015 is amazing.  Looking forward to {}! {} {} {}".format(name, other, hashtags[0][0], hashtags[1][0], hashtags[2][0])
	return myTweet



def find_hashtag(tweetsIn):
	d = defaultdict(int)
	for tweet in tweetsIn:
		tweetText = tweet[0].lower().split()
		for token in tweetText:
			#print(token)
			if token[0] == "#":
				d[token] += 1

	for key in ignore_list:

		for dKey in d.keys():
			if key in dKey:
				del d[dKey]

	pos_hosts = sorted(d.iteritems(), key =lambda (k,v): v, reverse=True)

	return pos_hosts



def gg_hist(name, tweetsIn, max_bins = 20, start_time = datetime(2015, 1, 11, 16, 0 ,0)):
	#subSet = find_subset(name, tweets)
	bins = [list() for _ in xrange(max_bins)]

	for tweet in tweetsIn:
		bin = classifyTimeStamp(tweet, max_bins, start_time)
		bins[bin].append(tweet)

	return bins

def classifyTimeStamp(tweet, num_bins, start_time):
	val = tweet[1][0:-3]
	time = datetime.fromtimestamp(int(val))
	diff = time - start_time
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

def printHist(histogram, start_time = datetime(2015, 1, 11, 16, 0 ,0), bin_size = timedelta(minutes = 15)):
	for idx in range(0, len(histogram)):
		bin_time = start_time + idx * bin_size
		pretty = "{} - {}".format(bin_time, len(histogram[idx]))
		if idx == 0:
			print("-Red Carpet-")
		elif idx == 8:
			print("-Main Event-")
		elif idx == 17:
			print("-Afterparties-")

		print(pretty)

def interpHist(name, hist):
	maxBin = 0
	maxBinSize = 0
	for idx in range(0, len(hist)):
		if len(hist[idx]) > maxBinSize:
			maxBinSize = len(hist[idx])
			maxBin = idx
	
	if maxBin < 6:
		print("{} was a huge hit on the Red Carpet".format(name))
	elif maxBin < 17:
		print("{} stole the show at the Award Ceremony".format(name))
	else:
		print("{} was the life of the Afterparty".format(name))


def main():
	year = '2015'
	name = raw_input("Enter name of Actor/Actress: ")
	print("Loading Tweets for {}".format(name))
	[tweets, parsed_list, parsed_presenter_list] = load_data(year)
	subSet = find_subset(name, tweets)
	print("Histogram of Twitter Activity for {}: ".format(name))
	hist = gg_hist(name, subSet)
	printHist(hist)
	interpHist(name, hist)
	print("Generating Tweet for {}:".format(name))
	customTweet = gg_typical_tweet(name, subSet)
	print(customTweet)
	



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

