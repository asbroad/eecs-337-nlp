from Tkinter import *
import json
import os
import main
from main import *
from read_tweets import *
from scrape_2013_data import *
from scrape_2015_data import *
from match_options import *
from unused_files import *
from get_winner import*
from save_output import *
root = Tk()
root.title('Golden Globes Predictor')
root.geometry('600x500')
v1 = StringVar(root)
v1.set('GoldenGlobe')
v2 = StringVar(root)
v2.set('Select a Year')
yr=v2.get()
#Year function
def printYear(yr):
	if yr == "2013":
		print yr
		#tweets = []
		#parsed_list = []
		#Twitter JSON files
		#tweet_file = open('../data/gg15mini_half.json','r')
		global tweets
		global parsed_list
		tweet_file = open('../data/goldenglobes.json','r')
		#Read in JSON file
		tweets = read_in_tweets_2013(tweet_file)
		#Golden Globe Wikipedia XML files
		xml_file_2013 = '70th_Golden_Globe_Awards.xml'
		#Parse Wiki Pages
		parsed_movie_list = parse_2013_wikipedia_movies(xml_file_2013)
		parsed_tv_list = parse_2013_wikipedia_tv(xml_file_2013)
		parsed_presenter_list = parse_2013_wikipedia_presenters(xml_file_2013)
		parsed_list = dict(parsed_movie_list.items() + parsed_tv_list.items())
		om1 = OptionMenu(root,v1,'Hosts','Best Motion Picture - Drama','Best Performance by an Actress in a Motion Picture - Drama','Best Performance by an Actor in a Motion Picture - Drama','Best Motion Picture - Comedy Or Musical','Best Performance by an Actress in a Motion Picture - Comedy Or Musical','Best Performance by an Actor in a Motion Picture - Comedy Or Musical','Best Animated Feature Film','Best Foreign Language Film','Best Performance by an Actress In A Supporting Role in a Motion Picture','Best Performance by an Actor In A Supporting Role in a Motion Picture','Best Director - Motion Picture','Best Screenplay - Motion Picture','Best Original Score - Motion Picture','Best Original Song - Motion Picture','Best Television Series - Drama','Best Performance by an Actress In A Television Series - Drama','Best Performance by an Actor In A Television Series - Drama','Best Television Series - Comedy Or Musical','Best Performance by an Actor In A Television Series - Comedy Or Musical','Best Mini-Series Or Motion Picture Made for Television','Best Performance by an Actress In A Mini-series or Motion Picture Made for Television','Best Performance by an Actor in a Mini-Series or Motion Picture Made for Television','Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television','Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television','Winners','Awards','Presenters','Nominees','Awards to Winners','Awards to Presenters','Awards to Nominees',command=printOption)
		om1.bind("Button-1>",printOption)
		om1.grid(row=0,column=1,columnspan = 1,stick = E + W+ N + S)

	elif yr=="2015":
		global tweets
		global parsed_list
		print yr
		tweet_file = open('../data/gg15mini_half.json','r')
		#tweet_file = open('gg15mini_half.json','r')
		''' Read in JSON file '''
		tweets = read_in_tweets_2015(tweet_file)
		''' Golden Globe Wikipedia XML files '''
		xml_file_2015 = '72nd_Golden_Globe_Awards.xml'
		''' Parse Wiki Pages '''
		parsed_movie_list = parse_2015_wikipedia_movies(xml_file_2015)
		parsed_tv_list = parse_2015_wikipedia_tv(xml_file_2015)
		parsed_presenter_list = parse_2015_wikipedia_presenters(xml_file_2015)
		parsed_list = dict(parsed_movie_list.items() + parsed_tv_list.items())
		om1 = OptionMenu(root,v1,'Hosts','Best Motion Picture - Drama','Best Performance by an Actress in a Motion Picture - Drama','Best Performance by an Actor in a Motion Picture - Drama','Best Motion Picture - Comedy Or Musical','Best Performance by an Actress in a Motion Picture - Comedy Or Musical','Best Performance by an Actor in a Motion Picture - Comedy Or Musical','Best Animated Feature Film','Best Foreign Language Film','Best Performance by an Actress In A Supporting Role in a Motion Picture','Best Performance by an Actor In A Supporting Role in a Motion Picture','Best Director - Motion Picture','Best Screenplay - Motion Picture','Best Original Score - Motion Picture','Best Original Song - Motion Picture','Best Television Series - Drama','Best Performance by an Actress In A Television Series - Drama','Best Performance by an Actor In A Television Series - Drama','Best Television Series - Comedy Or Musical','Best Performance by an Actor In A Television Series - Comedy Or Musical','Best Mini-Series Or Motion Picture Made for Television','Best Performance by an Actress In A Mini-series or Motion Picture Made for Television','Best Performance by an Actor in a Mini-Series or Motion Picture Made for Television','Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television','Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television','Winners','Awards','Presenters','Nominees','Awards to Winners','Awards to Presenters','Awards to Nominees',command=printOption)
		om1.bind("Button-1>",printOption)
		om1.grid(row=0,column=1,columnspan = 1,stick = E + W+ N + S)
		#return (tweets,parsed_list)

year=OptionMenu(root,v2,'2013','2015',command=printYear)
year.bind("Button-1>",printYear)
year.grid(row=0,column=0,columnspan = 1,stick = E + W+ N + S)
#Option function
def printOption(x):
	#tweets,parsed_list=printYear(yr)
	if x == "Hosts":
		print(v1.get())
	if x == "Best Motion Picture - Drama":
		print(v1.get())
	if x == "Best Performance by an Actress in a Motion Picture - Drama":
		print(v1.get())
	if x == "Best Performance by an Actor in a Motion Picture - Drama":
		print(v1.get())
	if x == "Best Motion Picture - Comedy Or Musical":
		print(v1.get())
	if x == "Best Performance by an Actress in a Motion Picture - Comedy Or Musical":
		print(v1.get())
	if x == "Best Performance by an Actor in a Motion Picture - Comedy Or Musical":
		print(v1.get())
	if x == "Best Animated Feature Film":
		print(v1.get())
	if x == "Best Foreign Language Film":
		print(v1.get())
	if x == "Best Performance by an Actress In A Supporting Role in a Motion Picture":
		print(v1.get())
	if x == "Best Performance by an Actor In A Supporting Role in a Motion Picture":
		print(v1.get())
	if x == "Best Director - Motion Picture":
		print(v1.get())
	if x == "Best Screenplay - Motion Picture":
		print(v1.get())
	if x == "Best Original Score - Motion Picture":
		print(v1.get())
	if x == "Best Original Song - Motion Picture":
		print(v1.get())
	if x == "Best Television Series - Drama":
		print(v1.get())
	if x == "Best Performance by an Actress In A Television Series - Drama":
		print(v1.get())
	if x == "Best Performance by an Actor In A Television Series - Drama":
		print(v1.get())
	if x == "Best Television Series - Comedy Or Musical":
		print(v1.get())
	if x == "Best Performance by an Actor In A Television Series - Comedy Or Musical":
		print(v1.get())
	if x == "Best Mini-Series Or Motion Picture Made for Television":
		print(v1.get())
	if x == "Best Performance by an Actress In A Mini-series or Motion Picture Made for Television":
		print(v1.get())
	if x == "Best Performance by an Actor in a Mini-Series or Motion Picture Made for Television":
		print(v1.get())
	if x == "Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television":
		print(v1.get())
	if x == "Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television":
		print(v1.get())
	if x == "Winners":
		print("This year's Golden Globe Winners are")
	if x == "Awards":
		print("This year's Golden Globe Awards are")
	if x == "Presenters":
		print("This year's Presenters in Golden Globe are:")
	if x == "Nominees":
		print("This year's Nominees of Golden Globe Award are:")
	if x == "Awards to Winners":
		print("Awards to Winners")
	if x == "Awards to Presenters":
		print("This year's Golden Globe Awards to Presenters are:")
	if x == "Awards to Nominees":
		print("This year's Golden Globe Awards to Nominees are:")
	if x == "Awards":
		print(v1.get())
	if x == "Presenters":
		print(v1.get())
	if x == "Nominees":
		print(v1.get())
	if x == "Awards to Winners":
		print(v1.get())
	if x == "Awards to Presenters'":
		print(v1.get())
	if x == "Awards to Nominees'":
		print(v1.get())
#Go function
def run():
	x=v1.get()
	if x == "Hosts":
		print(get_winner('host', tweets, parsed_list))
	if x == "Best Motion Picture - Drama":
		print(get_winner('Best Motion Picture - Drama', tweets, parsed_list))
	if x == "Best Performance by an Actress in a Motion Picture - Drama":
		print(get_winner('Best Performance by an Actress in a Motion Picture - Drama', tweets, parsed_list))
	if x == "Best Performance by an Actor in a Motion Picture - Drama":
		print(get_winner('Best Performance by an Actor in a Motion Picture - Drama', tweets, parsed_list))
	if x == "Best Motion Picture - Comedy Or Musical":
		print(get_winner('Best Motion Picture - Comedy Or Musical', tweets, parsed_list))
	if x == "Best Performance by an Actress in a Motion Picture - Comedy Or Musical":
		print(get_winner('Best Performance by an Actress in a Motion Picture - Comedy Or Musical', tweets, parsed_list))
	if x == "Best Performance by an Actor in a Motion Picture - Comedy Or Musical":
		print(get_winner('Best Performance by an Actor in a Motion Picture - Comedy Or Musical', tweets, parsed_list))
	if x == "Best Animated Feature Film":
		print(get_winner('Best Animated Feature Film', tweets, parsed_list))
	if x == "Best Foreign Language Film":
		print(get_winner('Best Foreign Language Film', tweets, parsed_list))
	if x == "Best Performance by an Actress In A Supporting Role in a Motion Picture":
		print(get_winner('Best Performance by an Actress In A Supporting Role in a Motion Picture', tweets, parsed_list))
	if x == "Best Performance by an Actor In A Supporting Role in a Motion Picture":
		print(get_winner('Best Performance by an Actor In A Supporting Role in a Motion Picture', tweets, parsed_list))
	if x == "Best Director - Motion Picture":
		print(get_winner('Best Director - Motion Picture', tweets, parsed_list))
	if x == "Best Screenplay - Motion Picture":
		print(get_winner('Best Screenplay - Motion Picture', tweets, parsed_list))
	if x == "Best Original Score - Motion Picture":
		print(get_winner('Best Original Score - Motion Picture', tweets, parsed_list))
	if x == "Best Original Song - Motion Picture":
		print(get_winner('Best Original Song - Motion Picture', tweets, parsed_list))
	if x == "Best Television Series - Drama":
		print(get_winner('Best Television Series - Drama', tweets, parsed_list))
	if x == "Best Performance by an Actress In A Television Series - Drama":
		print(get_winner('Best Performance by an Actress In A Television Series - Drama', tweets, parsed_list))
	if x == "Best Performance by an Actor In A Television Series - Drama":
		print(get_winner('Best Performance by an Actor In A Television Series - Drama', tweets, parsed_list))
	if x == "Best Television Series - Comedy Or Musical":
		print(get_winner('Best Television Series - Comedy Or Musical', tweets, parsed_list))
	if x == "Best Performance by an Actor In A Television Series - Comedy Or Musical":
		print(get_winner('Best Performance by an Actor In A Television Series - Comedy Or Musical', tweets, parsed_list))
	if x == "Best Mini-Series Or Motion Picture Made for Television":
		print(get_winner('Best Mini-Series Or Motion Picture Made for Television', tweets, parsed_list))
	if x == "Best Performance by an Actress In A Mini-series or Motion Picture Made for Television":
		print(get_winner('Best Performance by an Actress In A Mini-series or Motion Picture Made for Television', tweets, parsed_list))
	if x == "Best Performance by an Actor in a Mini-Series or Motion Picture Made for Television":
		print(get_winner('Best Performance by an Actor in a Mini-Series or Motion Picture Made for Television', tweets, parsed_list))
	if x == "Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television":
		print(get_winner('Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television', tweets, parsed_list))
	if x == "Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television":
		print(get_winner('Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television', tweets, parsed_list))


json = Button(root,text='WRITE FILE',activeforeground='white',activebackground='red')
json.grid(row=6,column=1,columnspan=1,stick =E + W+ N + S)
quit = Button(root,text='QUIT',command=root.quit,activeforeground='white',activebackground='red')
quit.grid(row=7,column=0,columnspan = 2,stick = E + W+ N + S)
start = Button(root,text='GO',command=run,activeforeground='white',activebackground='red')
start.bind("Button-1>",start)
start.grid(row=6,column=0,stick = E + W + N + S)
Label(root,text="Result:").grid(row=4,sticky=W)
t1 = Text(root) 
t1.grid(row=5,column=0,columnspan = 2,stick = E + W+ N + S)

class PrintToT1(object): 
     def write(self, s): 
         t1.insert(END, s) 
sys.stdout = PrintToT1() 
#x=v1.get()
mainloop() 
root.mainloop()
	
#os.system('python main.py')'''
