import xml.etree.ElementTree as ET
import urllib
import re
import HTMLParser

def main():
	
	'''User-Inputted Recipie Title'''
	#url = generateURL()
	#link = urllib.urlopen(url)


	'''Hard Coded URLs'''
	#link = urllib.urlopen("http://allrecipes.com/recipe/brown-rice-and-quinoa-sushi-rolls/")
	#link = urllib.urlopen("http://allrecipes.com/recipe/Boilermaker-Tailgate-Chili/")
	link = urllib.urlopen("http://allrecipes.com/recipe/jerk-chicken/")
	
	page = link.read()

	'''Local Webpages'''
	#f = open("../data/Burger.html")
	#f = open("../data/Cake.html")
	#f = open("../data/Stir-Fry.html")
	#page = f.read()

	#ingredient_qty = getIngredients(page)
	#ingredients = ingredient_qty[0]
	#amounts = ingredient_qty[1]

	#directions = getDirections(page)

	#if len(ingredients) == 0:
	#	print("Invalid URL")
	#else:
		#fancyPrintIngredients(ingredient_qty)
		#print(ingredients)
		#print(amounts)
		#print(directions)



class ingredient:
	def __init__ (self, name, qty, measure):
		self.name = name
		self.qty = qty
		self.measure = measure



def getDirections(page):
	regex = re.compile("<li><span class=\"plaincharacterwrap break\">(.*?)</span></li>")
	directions = re.findall(regex, page)

	return directions


def getIngredients(page):
	regex = re.compile("<p class=\"fl-ing\" itemprop=\"ingredients\">(.*?)</p>", re.DOTALL)
	ingredients = re.findall(regex, page)

	ingredient_dict = {}

	for entry in ingredients:
		regex = "<span id=\"lblIngAmount\" class=\"ingredient-amount\">(.*?)</span>"
		ingredient_amount = re.findall(regex, entry)
		regex = "<span id=\"lblIngName\" class=\"ingredient-name\">(.*?)</span>"
		ingredient_name = re.findall(regex, entry)

		item = ingredient(ingredient_name, 0, ingredient_amount)

		ingredient_list.append(item)

	return ingredient_list



def generateURL():
	#Generates URL from recipie title.  
	#Note:Title must be exactly correct
	recipie_name = raw_input("Enter Name of Recipie\n> ")
	recipie_url = re.sub(" ", "-", recipie_name).lower()
	recipie_url = "http://allrecipes.com/recipe/" + recipie_url
	return recipie_url


if __name__ == "__main__":
    main()