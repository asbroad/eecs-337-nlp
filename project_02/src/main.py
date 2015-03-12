from tools import hc_make_tool_list
from recipe import Recipe
from save_output import *
from nltk.tag import pos_tag
from ingredient import Ingredient
from collections import defaultdict
from knowledge_base import KnowledgeBase

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
	
	recipe = parse_recipe(page)
	kb = KnowledgeBase()
	tf_recipe = kb.transform_diet("vegetarian", recipe)
	prettyPrintRecipe(tf_recipe)


	save_output(url, tf_recipe)


if __name__ == "__main__":
    main()
