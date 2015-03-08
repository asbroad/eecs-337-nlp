from Tkinter import *
import json
import os
import main
from main import *
from ingredient import *
from knowledge_base import *
from save_output import *
from tools import *
from recipe import *
root = Tk()
root.title('Recipe Transformer')
root.geometry('600x500')
v2 = StringVar(root)
v2.set('Normal')
diet=v2.get()
v3 = StringVar(root)
v3.set('Type the Url or Name of Recipe Here')
url=v3.get()
url=Entry(root,textvariable=v3,width = 40)
url.grid(row=0,column=0,columnspan=3,stick =E + W+ N + S)
global recipie_name
recipie_name = v3.get()
recipie_url = re.sub(" ", "-", recipie_name).lower()
#find function
def find():
	global recipie_name
	recipie_name = v3.get()
	recipie_url = re.sub(" ", "-", recipie_name).lower()
	if recipie_name.startswith('www'):
		recipie_url = recipie_name
		#result=Label(root,text="Your original recipe is:")
		#result.grid(row=4,column=0,columnspan=4,stick =W)
		t=Label(root,text = recipie_url)
		t.grid(row=5,column=0,columnspan=4,stick =W)

	else:
		recipie_url = "http://allrecipes.com/recipe/" + recipie_url
		#result=Label(root,text="Your original recipe is:")
		#result.grid(row=4,column=0,columnspan=4,stick =W)
		t=Label(root,text = recipie_url)
		t.grid(row=5,column=0,columnspan=4,stick =W)

#go function
def go():
	result=Label(root,text="Your transformed recipe is:")
	result.grid(row=6,column=0,columnspan=4,stick =W)
#restart function
def restart():
	root.destroy()
	os.system('python gui.py')
#Write file function
def write_file():
	result=Label(root,text="Please check the folder to see the result")
	result.grid(row=7,column=0,columnspan=4,stick =W)

find = Button(root,text='Find Recipe',command=find,activeforeground='white',activebackground='red')
find.bind("Button-1>",find)
find.grid(row=0,column=3,columnspan=1,stick =E + W+ N + S)
instruction=Label(root,text="Please choose what kind of transformation you want to do.")
instruction.grid(row=1,column=0,columnspan=4,stick =W)
cuisine=OptionMenu(root,v2,'Itlian','Chinese')
cuisine.bind("Button-1>")
cuisine.grid(row=2,column=0,columnspan = 1,stick = E + W+ N + S)
diet=OptionMenu(root,v2,'Vegetarian','Vegan','Pescatarian','...')
diet.bind("Button-1>")
diet.grid(row=2,column=1,columnspan = 1,stick = E + W+ N + S)
other=OptionMenu(root,v2,'...','...')
other.bind("Button-1>")
other.grid(row=2,column=2,columnspan = 1,stick = E)

result=Label(root,text="Your original recipe is:")
result.grid(row=4,column=0,columnspan=4,stick =W)


go = Button(root,text='GO',command=go,activeforeground='white',activebackground='red')
go.bind("Button-1>")
go.grid(row=3,column=0,columnspan = 1,stick = E + W + N + S)
file = Button(root,text='Write File',command=write_file,activeforeground='white',activebackground='red')
file.bind("Button-1>")
file.grid(row=3,column=1,columnspan = 1,stick = E + W + N + S)
restart = Button(root,text='Restart',command=restart,activeforeground='white',activebackground='red')
restart.grid(row=3,column=2,columnspan = 1,stick = E + W + N + S)
quit = Button(root,text='QUIT',command=root.quit,activeforeground='white',activebackground='red')
quit.grid(row=3,column=3,columnspan = 1,stick = E + W+ N + S)
#t1 = Text(root) 
#t1.grid(row=6,column=0,columnspan = 2,stick = E + W+ N + S)

#class PrintToT1(object): 
#     def write(self, s): 
#         t1.insert(END, s) 
#sys.stdout = PrintToT1() 
#x=v1.get()
mainloop() 
root.mainloop()