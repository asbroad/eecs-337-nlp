import urllib
import re


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
	#link = urllib.urlopen(url)


	'''Hard Coded URLs'''
	#link = urllib.urlopen("http://allrecipes.com/recipe/brown-rice-and-quinoa-sushi-rolls/")
	#link = urllib.urlopen("http://allrecipes.com/recipe/Boilermaker-Tailgate-Chili/")	
	#link = urllib.urlopen("http://allrecipes.com/recipe/jerk-chicken/")
	#page = link.read()

	'''Local Cached Webpages'''
	#f = open("../data/Burger.html")
	#f = open("../data/Cake.html")
	f = open("../data/Stir-Fry.html")
	page = f.read()

	ingredient_list = getIngredients(page)
	prettyPrintIngredients(ingredient_list)

	directions = getDirections(page)
	prettyPrintDirections(directions)




class ingredient:
	def __init__ (self, name, qty, measure):
		self.name = name
		self.qty = qty
		self.measure = measure



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

def prettyPrintIngredients(ingredient_list):
	for item in ingredient_list:
		line = "Name: {}:\nQty: {}\nMeasure: {}\n\n".format(item.name, item.qty, item.measure)
		print(line)

def getIngredients(page):
	regex = re.compile("<p class=\"fl-ing\" itemprop=\"ingredients\">(.*?)</p>", re.DOTALL)
	ingredients = re.findall(regex, page)
	print(ingredients)
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

		regex = re.compile("[0-9]+\s[0-9/]+|[0-9/]+|[0-9]+")
		ingredient_qty = re.findall(regex, ingredient_amount)
		if len(ingredient_qty) == 0:
			ingredient_qty = "to taste"
		else:
			ingredient_qty = ingredient_qty[0]

		ingredient_measure = ingredient_amount.replace(ingredient_qty, "")
		
		if ingredient_measure == "":
			ingredient_measure = "items"
		if ingredient_measure[0] == " ":
			ingredient_measure = ingredient_measure[1:]

		item = ingredient(ingredient_name, ingredient_qty, ingredient_measure)
		ingredient_list.append(item)

	if len(ingredient_list) == 0:
		print("Unable to retreive recipie: Bad URL")

	return ingredient_list



def generateURL():
	#Generates URL from recipie title.  
	#Note:Title must be exactly correct
	recipie_name = raw_input("Enter Name of Recipie\n> ")
	recipie_url = re.sub(" ", "-", recipie_name).lower()
	recipie_url = "http://allrecipes.com/recipe/" + recipie_url
	return recipie_url


def getCookingMethods():
	methods = ["Grill", "Pan-Fry", "Deep Fry", "Saute", "Boil", "Roast", "Bake", "Sear", "Poach", "Simmer", "Broil", "Steam", "Blanch", "Braise", "Stew"]
	return methods


if __name__ == "__main__":
    main()


