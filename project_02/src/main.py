from tools import hc_make_tool_list
from recipe import Recipe
from save_output import save_output, return_ans_dict
from nltk.tag import pos_tag
from ingredient import Ingredient
from collections import defaultdict
from knowledge_base import KnowledgeBase
from utils import *
import sys

def autograder_version(url):
	link = urllib.urlopen(url)
	page = link.read()
	recipe = parse_recipe(page)
	recipe = unabridgeMeasure(recipe)
	return return_ans_dict(recipe)


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


	if len(sys.argv) < 2 :
		recipe = parse_recipe(page)
		recipe = unabridgeMeasure(recipe)
		prettyPrintRecipe(recipe)
		save_output(url, recipe)
	elif len(sys.argv) == 2:
		case_num = int(sys.argv[1])
		if case_num < 1 or case_num > 8:
			print('You can only pick from [1-8]')
			return
		recipe = parse_recipe(page)
		recipe = unabridgeMeasure(recipe)
		kb = KnowledgeBase()
		if case_num == 1:
			tf_recipe = kb.transform_cuisine("italian", recipe)
		elif case_num == 2:
			tf_recipe = kb.transform_cuisine("chinese", recipe)
		elif case_num == 3:
			tf_recipe = kb.transform_diet("vegetarian", recipe)
		elif case_num == 4:
			tf_recipe = kb.transform_diet("pescatarian", recipe)
		elif case_num == 5:
			tf_recipe = kb.transform_healthy("low-fat", recipe)
		elif case_num == 6:
			tf_recipe = kb.transform_healthy("low-sodium", recipe)
		elif case_num == 7:
			tf_recipe = transformQty(2, recipe)
		elif case_num == 8:
			tf_recipe = transformQty(3, recipe)

		prettyPrintRecipe(tf_recipe)
		save_output(url, tf_recipe)
	else:
		print('Too many arguments. You can either either just call main.py to see the recipe or pass in a single integer to select a transformation.')



if __name__ == "__main__":
    main()
