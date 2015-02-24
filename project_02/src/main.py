import xml.etree.ElementTree as ET
import urllib
import re
import HTMLParser

def main():
	
	'''User-Inputted Recipie Title'''
	url = generateURL()
	link = urllib.urlopen(url)
	page = link.read()

	'''Hard Coded URLs'''
	#link = urllib.urlopen("http://allrecipes.com/recipe/brown-rice-and-quinoa-sushi-rolls/")
	#link = urllib.urlopen("http://allrecipes.com/recipe/Boilermaker-Tailgate-Chili/")
	#page = link.read()

	'''Local Webpages'''
	#f = open("../data/Burger.html")
	#f = open("../data/Cake.html")
	#f = open("../data/Stir-Fry.html")
	#page = f.read()

	regex = re.compile("<span id=\"lblIngAmount\" class=\"ingredient-amount\">(.*?)</span>")
	amounts = re.findall(regex, page)
	regex = re.compile("<span id=\"lblIngName\" class=\"ingredient-name\">(.*?)</span>")
	ingredients = re.findall(regex, page)

	if len(ingredients) == 0:
		print("Invalid URL")
	else:
		print(ingredients)
		print(amounts)




def generateURL():
	#Generates URL from recipie title.  
	#Note:Title must be exactly correct
	recipie_name = raw_input("Enter Name of Recipie\n> ")
	recipie_url = re.sub(" ", "-", recipie_name).lower()
	recipie_url = "http://allrecipes.com/recipe/" + recipie_url
	return recipie_url


if __name__ == "__main__":
    main()