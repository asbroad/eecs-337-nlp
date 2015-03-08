from Tkinter import *
import json
import os
import main
from ingredient import *
from knowledge_base import *
from save_output import *
from tools import *
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
find = Button(root,text='Find Recipe',activeforeground='white',activebackground='red')
find.grid(row=0,column=3,columnspan=1,stick =E + W+ N + S)
instruction=Label(root,text="Please choose what kind of transformation do you want to do.")
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
go = Button(root,text='GO',activeforeground='white',activebackground='red')
go.bind("Button-1>")
go.grid(row=3,column=0,columnspan = 2,stick = E + W + N + S)
file = Button(root,text='Write File',activeforeground='white',activebackground='red')
file.bind("Button-1>")
file.grid(row=3,column=2,columnspan = 2,stick = E + W + N + S)
result=Label(root,text="Your transformed recipe is:")
result.grid(row=4,column=0,columnspan=4,stick =W)
t=Message(root,text = 'recipe.......')
t.grid(row=5,column=0,columnspan=4,stick =W)
root.mainloop()