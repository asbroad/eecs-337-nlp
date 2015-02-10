from Tkinter import *
import json
import os
import main
from main import *
from read_tweets import *#read_in_tweets_2013, read_in_tweets_2015
from scrape_2013_data import *#parse_2013_wikipedia_movies, parse_2013_wikipedia_tv, parse_2013_wikipedia_presenters
from scrape_2015_data import *#parse_2015_wikipedia_movies, parse_2015_wikipedia_tv, parse_2015_wikipedia_presenters
from match_options import *#get_bigram_list_match_tweets, get_bigram_list_match_tweets_lax, get_bigram_list_match_tweets_either_or_lax, get_unigram_list_match_tweets_lax, get_unigram_list_match_tweets_either_or_lax, pairThings
from unused_files import *#get_academy_info # GET RID OF THIS BY USING SCRAPED DATA INSTEAD
root = Tk()
root.title('Golden Globes Predictor')
root.geometry('200x100')
#Option function
def printOption(x):
	if x == "Hosts":
		print(v1.get())
	if x == "Winners":
		print(v1.get())
	if x == "Awards":
		print(v1.get())
	if x == "Presenters":
		print(v1.get())
	if x == "Nominees":
		print(v1.get())
	if x == "Awards to Winners":
		print(v1.get())
	if x == "Awards to Presenters":
		print(v1.get())
	if x == "Awards to Nominees":
		print(v1.get())
#Start function
def run():
	print'Please Wait for A Moment......'
	x=v1.get()
	if x == "Hosts":
		print("This year's Hosts in Golden Globe Award are:")
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
	os.system('python main.py')
#Number function
def func(event):
    print("You hit return.")
#Write file function
os.system('python save_output.py')

v1 = StringVar(root)
v1.set('GoldenGlobe')
om1 = OptionMenu(root,v1,'Hosts','Winners','Awards','Presenters','Nominees','Awards to Winners','Awards to Presenters','Awards to Nominees',command=printOption)
om1.bind("Button-1>",printOption)
om1.grid(row=0,column=0,columnspan = 2,stick = E + W+ N + S)
e = StringVar()
#entry = Entry(root,textvariable = e)
#e.set('1')
#entry.bind("<Return>",func)
#entry.grid(row=1,column=1)
#Label(root,text="Number:").grid(row=1,column=0,sticky=W)
#Label(root,text="Result:").grid(row=3,sticky=W)
#root.lbResults = Listbox(root)
#root.lbResults.bind(("Button-1>",results))
#root.lbResults.grid(row = 4,column = 0,columnspan = 2,stick = E + W + N + S)
json = Button(root,text='WRITE FILE',activeforeground='white',activebackground='red')
json.grid(row=6,column=1,stick =E + W+ N + S)
quit = Button(root,text='QUIT',command=root.quit,activeforeground='white',activebackground='red')
quit.grid(row=7,column=0,columnspan = 2,stick = E + W+ N + S)
start = Button(root,text='START',command=run,activeforeground='white',activebackground='red')
start.bind("Button-1>",start)
start.grid(row=6,column=0,stick = E + W + N + S)
root.mainloop()
