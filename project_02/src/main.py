import urllib
import re


#Fix this
from tools import hc_make_tool_list
from save_output import *
from nltk.tag import pos_tag
from ingredient import Ingredient


'''
To Do:
Extract Cooking methods
extract spices - perhaps use wikipedia to obtain list?
extract tools - should be assosciated with secondary cooking methods (e.g bowl - stir)

Build syntax for recipie

'''

def main():

	'''User-Inputted Recipie Title'''
	#url = generateURL()

	'''Hard Coded URLs'''
	# url = "http://allrecipes.com/recipe/brown-rice-and-quinoa-sushi-rolls/"
	# url = "http://allrecipes.com/recipe/Boilermaker-Tailgate-Chili/"
	#url = "http://allrecipes.com/recipe/jerk-chicken/"
	#link = urllib.urlopen(url)
	#page = link.read()

	'''Local Cached Webpages'''
	# url = "../data/Burger"
	# url = "../data/Cake"
	url = "../data/Stir-Fry"
	f = open(url + ".html")
	page = f.read()

	#makeVegetarian(ingredient_list)
	#ingredient_list = getIngredients(page)
	#prettyPrintIngredients(ingredient_list)

	parse_recipe(page)
#
#	directions = getDirections(page)
#	prettyPrintDirections(directions)
#
#	meat_list = getMeats()
#	prettyPrintMeats(meat_list)
#
	#tool_list = getTools()
	#prettyPrintTools(tool_list)
	#print(tool_list)

	#save_output(url, [], '', [], [])



def getMeats():
	f = open("../data/meat_list.html")
	meatsPage = f.read()

	regex = re.compile("<li>(.*?)</li>")
	meats = re.findall(regex, meatsPage)

	for idx in range(0, len(meats)):
		regex = re.compile("[a-zA-Z]+\s*[a-zA-Z]*")
		meats[idx] = re.findall(regex, meats[idx])[0]

	return meats


def parse_recipe(page):
	recipe_ingredients = getIngredients(page)

	regex = re.compile("<h1 id=\"itemTitle\" class=\"plaincharacterwrap fn\" itemprop=\"name\">(.*?)</h1>")
	recipe_title = re.findall(regex, page)[0]

	tool_list = hc_make_tool_list()
	directions = getDirections(page)
	mytools = select_tools(directions, tool_list)
	prettyPrintTools(mytools)



	prettyPrintDirections(directions)


def select_tools(directions, tools):
	res = []

	for direction in directions:
		for word in direction.lower().split():
			for tool in tools:
				if tool.isUse(word):
					res.append(tool)

		#tagged_direction = pos_tag(direction.split())
		#print(tagged_direction)

	return list(set(res))


def generate_directions(directions, tool_list):
	return 0






def makeVegetarian(ingredient_list):
	for ingredient in ingredient_list:
		ingredient.name = "Soy " + ingredient.name



def getDirections(page):
	regex = re.compile("<li><span class=\"plaincharacterwrap break\">(.*?)</span></li>")
	directions = re.findall(regex, page)

	return directions

def prettyPrintDirections(directions):
	idx = 1;
	for direction in directions:
		line = "Step {}: ".format(idx)
		line = line + direction
		print(line)
		idx += 1

def prettyPrintMeats(meat_list):
	for meat in meat_list:
		print(meat)

def prettyPrintIngredients(ingredient_list):
	for item in ingredient_list:
		line = "Name: {}\nQty: {}\nMeasure: {}\nPrep: {}\n\n".format(item.name, item.qty, item.measure, item.prep)
		print(line)

def prettyPrintTools(tool_list):
	for item in tool_list:
		line = "Name: {}\nUse: {}\n\n".format(item.name, item.use)
		print(line)


def getIngredients(page):
	regex = re.compile("<p class=\"fl-ing\" itemprop=\"ingredients\">(.*?)</p>", re.DOTALL)
	ingredients = re.findall(regex, page)
	ingredient_list = []

	for entry in ingredients:
		regex = "<span id=\"lblIngAmount\" class=\"ingredient-amount\">(.*?)</span>"
		ingredient_amount = re.findall(regex, entry)
		if len(ingredient_amount) == 0:
			ingredient_amount = ""
		else:
			ingredient_amount = ingredient_amount[0]

		regex = "<span id=\"lblIngName\" class=\"ingredient-name\">(.*?)</span>"
		ingredient_name = re.findall(regex, entry)[0]



		split_name = ingredient_name.split(", ")
		if len(split_name) > 1:
			ingredient_style = split_name[len(split_name)-1]
		else:
			ingredient_style = ""
		ingredient_name = split_name[0]

		regex = re.compile("[0-9]+\s[0-9/]+|[0-9/]+|[0-9]+")
		ingredient_qty = re.findall(regex, ingredient_amount)
		if len(ingredient_qty) == 0:
			ingredient_qty = "to taste"
		else:
			ingredient_qty = ingredient_qty[0]

		ingredient_measure = ingredient_amount.replace(ingredient_qty, "")
		ingredient_qty = str2num(ingredient_qty)

		if ingredient_measure == "":
			ingredient_measure = "items"
		if ingredient_measure[0] == " ":
			ingredient_measure = ingredient_measure[1:]
		item = Ingredient(ingredient_name)
		item.ingredient_from_recipie(ingredient_name, ingredient_qty, ingredient_measure, ingredient_style)
		ingredient_list.append(item)

	if len(ingredient_list) == 0:
		print("Unable to retreive recipie: Bad URL")

	return ingredient_list


def str2num(strIn):
	res = 0
	regex = re.compile("[0-9/]+")
	numbers = re.findall(regex, strIn)
	for number in numbers:
		regex = re.compile("([0-9]+)/([0-9]+)")
		vals = re.findall(regex, number);
		if vals:
			val = vals[0]
			res = res + float(val[0])/float(val[1])
		else:
			res = res + float(number)
	return res

def generateURL():
	#Generates URL from recipie title.
	#Note:Title must be exactly correct
	recipie_name = raw_input("Enter Name of Recipie\n> ")
	recipie_url = re.sub(" ", "-", recipie_name).lower()
	recipie_url = "http://allrecipes.com/recipe/" + recipie_url
	return recipie_url

def generate_url():
	return 'http://allrecipes.com/recipe/jerk-chicken'

def getCookingMethods():
	#list generated by consulting chef Gaston Bleu, owner of Le Fancie Restrantue
	methods = ["Grill", "Stir-Fry", "Flambe", "Fry", "Pan-Fry", "Deep Fry", "Saute", "Boil", "Roast", "Bake", "Sear", "Poach", "Simmer", "Broil", "Steam", "Blanch", "Braise", "Stew"]
	return methods


if __name__ == "__main__":
    main()
