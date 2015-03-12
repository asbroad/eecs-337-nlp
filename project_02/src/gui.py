from Tkinter import *
#import json
#import os

from utils import *

from knowledge_base import KnowledgeBase



def runGui():
	root = Tk()
	root.title('Recipe Transformer')
	root.geometry('580x500')
	v0 = StringVar(root)
	v0.set('None')
	
	v1 = StringVar(root)
	v1.set('Normal')
	
	v2 = StringVar(root)
	v2.set('Normal')

	v3 = StringVar(root)
	v3.set('Type the Url or Name of Recipe Here')




	url_entry=Entry(root,textvariable=v3)
	url_entry.grid(row=0,column=0,columnspan=3,sticky =E + W+ N + S)

	global recipie_name

	find_button = Button(root,text='Find Recipe',command=find,activeforeground='white',activebackground='red')
	find_button.bind("Button-1>",find_button)
	find_button.grid(row=0,column=3,columnspan=1,sticky =E + W+ N + S)

	cuisine=OptionMenu(root,v0,'Italian','Chinese')
	cuisine.bind("Button-1>")
	cuisine.grid(row=2,column=0,columnspan = 1,sticky = E + W+ N + S)
	
	diet=OptionMenu(root,v1,'Vegetarian','Vegan','Pescatarian')
	diet.bind("Button-1>")
	diet.grid(row=2,column=1,columnspan = 1,sticky = E + W+ N + S)
	
	other=OptionMenu(root,v2,'low fat','low sodium')
	other.bind("Button-1>")
	other.grid(row=2,column=2,columnspan = 1,sticky = E + W+ N + S)
	
	go_button = Button(root,text='GO',command= lambda: go(v0, v1, v2, v3),activeforeground='white',activebackground='red')
	go_button.bind("Button-1>", go_button)
	go_button.grid(row=3,column=0,sticky = E + W + N + S)


	file_button = Button(root,text='Write File',command=write_file,activeforeground='white',activebackground='red')
	file_button.bind("Button-1>")
	file_button.grid(row=3,column=1,columnspan = 1,sticky = E + W + N + S)
	

	file = Button(root,text='Write File',command=write_file,activeforeground='white',activebackground='red')
	file.bind("Button-1>")
	file.grid(row=3,column=1,sticky = E + W + N + S)

	restart_button = Button(root,text='Restart',command=restart,activeforeground='white',activebackground='red')
	restart_button.grid(row=3,column=2,sticky = E + W + N + S)
	
	quit_button = Button(root,text='QUIT',command=root.quit,activeforeground='white',activebackground='red')
	quit_button.grid(row=3,column=3,sticky = E + W+ N + S)
	
	t1 = Text(root) 
	t1.grid(row=4, column=0,rowspan=60,columnspan = 4,sticky = S)
	
	sys.stdout = RedirectText(t1)

	mainloop() 
	root.mainloop()


#find function
def find():
	root = Tk()
	v3 = StringVar(root)

	recipie_name = v3.get()
	recipie_url = re.sub(" ", "-", recipie_name).lower()
	if recipie_name.startswith('www'):
		recipie_url = recipie_name
		#result=Label(root,text="Your original recipe is:")
		#result.grid(row=4,column=0,columnspan=4,sticky =W)
		t=Label(root,text = recipie_url)
		t.grid(row=5,column=0,columnspan=4,sticky =W)

	else:
		recipie_url = "http://allrecipes.com/recipe/" + recipie_url
		#result=Label(root,text="Your original recipe is:")
		#result.grid(row=4,column=0,columnspan=4,sticky =W)
		t=Label(root,text = recipie_url)
		t.grid(row=5,column=0,columnspan=4,sticky =W)

	return recipie_url

#go function
def go(v0, v1, v2, v3):

	url = "../data/Stir-Fry"
	f = open(url + ".html")
	page = f.read()

	recipe = parse_recipe(page)
	kb = KnowledgeBase()
	cuisine_recipe = kb.transform_cuisine(v0.get().lower(), recipe)
	tf_recipe = kb.transform_diet(v1.get().lower(), recipe)
	prettyPrintRecipe(recipe)






#restart function
def restart():
	root.destroy()
	os.system('python gui.py')
#Write file function
def write_file():
	result=Label(root,text="Please check the folder to see the result")
	result.grid(row=7,column=0,columnspan=4,sticky =W)



class RedirectText(object):
    def __init__(self, text_ctrl):
        self.output = text_ctrl

    def write(self, string):
        self.output.insert(END, string)


if __name__ == "__main__":
    runGui()


