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
root = Tk()
root.title('Golden Globes Predictor')
root.geometry('200x100')
#Option function
def printOption(x):
	if x == "Hosts":
		print(v1.get())
	if x == "Best movie drama":
		print(v1.get())
	if x == "Best actress drama":
		print(v1.get())
	if x == "Best actor drama":
		print(v1.get())
	if x == "Best movie musical or comedy":
		print(v1.get())
	if x == "Best actress musical or comedy":
		print(v1.get())
	if x == "Best actor musical or comedy":
		print(v1.get())
	if x == "Best animated movie":
		print(v1.get())
	if x == "Best foreign movie":
		print(v1.get())
	if x == "Best supporting actress":
		print(v1.get())
	if x == "Best supporting actor":
		print(v1.get())
	if x == "Best director":
		print(v1.get())
	if x == "Best screenplay":
		print(v1.get())
	if x == "Best original score":
		print(v1.get())
	if x == "Best original song":
		print(v1.get())
	if x == "Best tv series drama":
		print(v1.get())
	if x == "Best actress tv drama":
		print(v1.get())
	if x == "Best actor tv drama":
		print(v1.get())
	if x == "Best tv musical or comedy":
		print(v1.get())
	if x == "Best actor tv musical or comedy":
		print(v1.get())
	if x == "Best tv movie":
		print(v1.get())
	if x == "Best actress tv movie":
		print(v1.get())
	if x == "Best actor tv movie":
		print(v1.get())
	if x == "Best supporting actress tv movie":
		print(v1.get())
	if x == "Best supporting actor tv movie":
		print(v1.get())
#Start function
def run():
	print'Please Wait for A Moment......'
	x=v1.get()
	if x == "Hosts":
		print(v1.get())
	if x == "Best movie drama":
		print(v1.get())
		winner = get_winner('best movie drama', tweets, parsed_list)
        print(winner)
	if x == "Best actress drama":
		print(v1.get())
	if x == "Best actor drama":
		print(v1.get())
	if x == "Best movie musical or comedy":
		print(v1.get())
	if x == "Best actress musical or comedy":
		print(v1.get())
	if x == "Best actor musical or comedy":
		print(v1.get())
	if x == "Best animated movie":
		print(v1.get())
	if x == "Best foreign movie":
		print(v1.get())
	if x == "Best supporting actress":
		print(v1.get())
	if x == "Best supporting actor":
		print(v1.get())
	if x == "Best director":
		print(v1.get())
	if x == "Best screenplay":
		print(v1.get())
	if x == "Best original score":
		print(v1.get())
	if x == "Best original song":
		print(v1.get())
	if x == "Best tv series drama":
		print(v1.get())
	if x == "Best actress tv drama":
		print(v1.get())
	if x == "Best actor tv drama":
		print(v1.get())
	if x == "Best tv musical or comedy":
		print(v1.get())
	if x == "Best actor tv musical or comedy":
		print(v1.get())
	if x == "Best tv movie":
		print(v1.get())
	if x == "Best actress tv movie":
		print(v1.get())
	if x == "Best actor tv movie":
		print(v1.get())
	if x == "Best supporting actress tv movie":
		print(v1.get())
	if x == "Best supporting actor tv movie":
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
	os.system('python main.py')
#Write file function
os.system('python save_output.py')

v1 = StringVar(root)
v1.set('GoldenGlobe')
om1 = OptionMenu(root,v1
,'Hosts'
,'Best movie drama'
,'Best actress drama'
,'Best actor drama'
,'Best movie musical or comedy'
,'Best actress musical or comedy'
,'Best actor musical or comedy'
,'Best animated movie'
,'Best foreign movie'
,'Best supporting actress'
,'Best supporting actor'
,'Best director'
,'Best screenplay'
,'Best original score'
,'Best original song'
,'Best tv series drama'
,'Best actress tv drama'
,'Best actor tv drama'
,'Best tv musical or comedy'
,'Best actor tv musical or comedy'
,'Best tv movie'
,'Best actress tv movie'
,'Best actor tv movie'
,'Best supporting actress tv movie'
,'Best supporting actor tv movie'
,'Winners'
,'Awards'
,'Presenters'
,'Nominees'
,'Awards to Winners'
,'Awards to Presenters'
,'Awards to Nominees',
command=printOption)
om1.bind("Button-1>",printOption)
om1.grid(row=0,column=0,columnspan = 2,stick = E + W+ N + S)
e = StringVar()
json = Button(root,text='WRITE FILE',activeforeground='white',activebackground='red')
json.grid(row=6,column=1,stick =E + W+ N + S)
quit = Button(root,text='QUIT',command=root.quit,activeforeground='white',activebackground='red')
quit.grid(row=7,column=0,columnspan = 2,stick = E + W+ N + S)
start = Button(root,text='START',command=run,activeforeground='white',activebackground='red')
start.bind("Button-1>",start)
start.grid(row=6,column=0,stick = E + W + N + S)
root.mainloop()
