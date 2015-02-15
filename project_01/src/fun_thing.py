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


def find_subset(name, tweets):
	subSet = []
	for tweet in tweets:
		tweetText = tweet[0].lower()
		if match_all_words(tweetText, name.lower().split()):
			subSet.append(tweet)
	print("subSet Generated")
	return subSet


def gg_typical_tweet(name, tweets):
	subSet = find_subset(name, tweets)
	random.shuffle(subSet)
	subSet = subSet[0:1000]
	print("sampled")
	top_hashtags = find_hashtag(subSet)
	other = get_bigram_list_match_tweets(subSet, name.split())[1][0]
	hashtags = random.sample(set(top_hashtags[0:10]), 3)

	myTweet = "{} at the #goldenglobes2015 is amazing.  Looking forward to {}! {} {} {}".format(name, other, hashtags[0][0], hashtags[1][0], hashtags[2][0])
	print(myTweet)



def find_hashtag(tweets):
	d = defaultdict(int)
	for tweet in tweets:
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



def gg_hist(name, tweets, max_bins = 20, start_time = datetime(2015, 1, 11, 16, 0 ,0)):
	subSet = find_subset(name, tweets)
	bins = [list() for _ in xrange(max_bins)]

	for tweet in subSet:
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
		print(pretty)

'''
def main():
	year = '2015'
	[tweets, parsed_list, parsed_presenter_list] = load_data(year)


	#res = find_hashtag(tweets)
	#print(res[0:5])
	#gg_typical_tweet("Tina Fey", tweets)
	#bin = classifyTimeStamp(tweets[0])
	#print(bin)
	hist = gg_hist("Tina Fey", tweets)
	printHist(hist)

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