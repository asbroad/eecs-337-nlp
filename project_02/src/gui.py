from Tkinter import *
import json
#import os

from utils import *
from save_output import *
from main import *
from urllib import *

from knowledge_base import KnowledgeBase



def runGui():
	global root
	root = Tk()
	root.title('Recipe Transformer')
	root.geometry('650x500')

	global v0
	v0 = StringVar(root)
	v0.set('Cuisine')

	global v1
	v1 = StringVar(root)
	v1.set('Diet')

	global v2
	v2 = StringVar(root)
	v2.set('Health')

	global v3
	v3 = StringVar(root)
	v3.set('Type the Url or Name of Recipe Here')

	global v4
	v4 = StringVar(root)
	v4.set('Single Recipe')

	global url
	url = "temp-name"

	global tf_recipe
	tf_recipe = "dummy-recipe"


	url_entry=Entry(root,textvariable=v3)
	url_entry.grid(row=0,column=0,columnspan=3,sticky =E + W+ N + S)

	cuisine_dropdown = OptionMenu(root,v0,'None','Italian','Chinese')
	cuisine_dropdown.grid(row=2,column=0,columnspan = 1,sticky = E + W+ N + S)

	diet_dropdown = OptionMenu(root,v1,'None','Vegetarian','Vegan','Pescatarian')
	diet_dropdown.grid(row=2,column=1,columnspan = 1,sticky = E + W+ N + S)

	health_dropdown = OptionMenu(root,v2,'None','Low Fat','Low Sodium')
	health_dropdown.grid(row=2,column=2,columnspan = 1,sticky = E + W+ N + S)

	qty_dropdown = OptionMenu(root,v4,'Single Recipe','Double Recipe','Triple Recipe')
	qty_dropdown.grid(row=2,column=3,columnspan = 1,sticky = E + W + N + S)

	find_button = Button(root,text='Find Recipe',activeforeground='white',activebackground='red')
	find_button.grid(row=0,column=3,columnspan=1,sticky =E + W+ N + S)
	find_button.bind("<Button-1>", find_callback)

	go_button = Button(root,text='Transform Recipe', activeforeground='white',activebackground='red')
	go_button.grid(row=3,column=0,sticky = E + W + N + S)
	go_button.bind("<Button-1>", go_callback)

	write_button = Button(root,text='Write File',activeforeground='white',activebackground='red')
	write_button.grid(row=3,column=1,columnspan = 1,sticky = E + W + N + S)
	write_button.bind("<Button-1>", write_callback)

	restart_button = Button(root,text='Restart',activeforeground='white',activebackground='red')
	restart_button.grid(row=3,column=2,sticky = E + W + N + S)
	restart_button.bind("<Button-1>", restart_callback)

	quit_button = Button(root,text='QUIT',activeforeground='white',activebackground='red')
	quit_button.grid(row=3,column=3,sticky = E + W+ N + S)
	quit_button.bind("<Button-1>", quit_callback)

	t1 = Text(root)
	t1.grid(row=4, column=0,rowspan=60,columnspan = 4,sticky = S)

	sys.stdout = RedirectText(t1)

	root.mainloop()


#find function
def find_callback(event):
	global url
	recipie_name = v3.get()
	url = re.sub(" ", "-", recipie_name).lower()
	if '.com' in recipie_name:
		url = recipie_name
		#result=Label(root,text="Your original recipe is:")
		#result.grid(row=4,column=0,columnspan=4,sticky =W)
	else:
		url = "http://www.allrecipes.com/recipe/" + url
		#result=Label(root,text="Your original recipe is:")
		#result.grid(row=4,column=0,columnspan=4,sticky =W)
	print("Accessing: {}".format(url))



#go function
def go_callback(event):
	global url
	global v0
	global v1
	global v2
	global v4
	global tf_recipe

	if "temp-name" in url:
		print("Error: No recipe found.  Select recipe to transform.")
	else:
		print("Transforming Recipe")
		link = urllib.urlopen(url)
		page = link.read()
		recipe = parse_recipe(page)
		kb = KnowledgeBase()
		tf_recipe = kb.transform_cuisine(v0.get().lower(), recipe)
		tf_recipe = kb.transform_diet(v1.get().lower(), tf_recipe)
		tf_recipe = kb.transform_healthy(v2.get().lower(), tf_recipe)
		qty = v4.get().lower()

		if "single" in qty:
			tf_recipe = transformQty(1, tf_recipe)
		elif "double" in qty:
			tf_recipe = transformQty(2, tf_recipe)
		elif "triple" in qty:
			tf_recipe = transformQty(3, tf_recipe)
		else:
			print("Error: Invalid QTY")

		prettyPrintRecipe(tf_recipe)

def write_callback(event):
	global url
	global tf_recipe

	save_output(url, tf_recipe)

#restart function
def restart_callback(event):
	root.destroy()
	runGui()

def quit_callback(event):
	root.destroy()



class RedirectText(object):
    def __init__(self, text_ctrl):
        self.output = text_ctrl

    def write(self, string):
        self.output.insert(END, string)


if __name__ == "__main__":
    runGui()
