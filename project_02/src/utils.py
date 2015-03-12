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
		line = "Name: {}\nQty: {}\nMeasure: {}\nPrep: {}\nPrep Description: {}\n".format(item.name, item.qty, item.measure, item.prep, item.prep_description)
		print(line)

def prettyPrintTools(tool_list):
	for item in tool_list:
		line = "Name: {}\nUse: {}\n\n".format(item.name, item.use)
		print(line)


def prettyPrintRecipe(recipe):
	print("--------------------------------------------")
	print(recipe.name)
	print("--------------------------------------------")
	print("\nIngredients:\n")
	prettyPrintIngredients(recipe.ingredients)

	print("\nTools:\n")
	for tool in recipe.tools:
		print(tool.name)
	print("\n")
	print("Main Cooking Method: {}".format(recipe.main_method[0]))
	for method in recipe.other_methods:
		print("Additional Method: {}".format(method[0]))
	print("\n")
	print("\nDirections:\n")
	prettyPrintDirections(recipe.directions)


def transformQty(multiplier, recipe):
	ingredients = recipe.ingredients
	for ingredient in ingredients:
		ingredient.qty = ingredient.qty * multiplier

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
	method_list = hc_make_method_list()

	directions = getDirections(page)
	recipe_tools = select_tools(directions, tool_list)

	methods = select_methods(directions, method_list)

	if len(methods) > 1:
		other_methods = methods[1:]
	else:
		other_methods = []

	if len(methods) > 0:
		main_method = methods[0]
	else:
		main_method = "none found"

	res = Recipe(recipe_title, recipe_ingredients, recipe_tools, main_method, other_methods, directions)
	return res

def select_methods(directions, methods):
	d = defaultdict(int)
	for direction in directions:
		for method in methods:
			if method in direction.lower():
				d[method] += 1

	sorted_vals = sorted(d.iteritems(), key =lambda (k,v): v, reverse=True)
	return sorted_vals
	#return list(set(res))


def select_tools(directions, tools):
	res = []

	for direction in directions:
		for tool in tools:
			for use in tool.use:
				if use in direction.lower():
					res.append(tool)

		#tagged_direction = pos_tag(direction.split())
		#print(tagged_direction)

	return list(set(res))

def getDirections(page):
	regex = re.compile("<li><span class=\"plaincharacterwrap break\">(.*?)</span></li>")
	directions = re.findall(regex, page)

	return directions

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
	
		#check for *ly *ed (e.g. thinly sliced) structure
		regex = "([A-Za-z]+ly) ([A-Za-z]+ed)"
		res = re.findall(regex, ingredient_name)

		if res:
			ingredient_prep_description = res[0][0]
			ingredient_prep = res[0][1]

			ingredient_name = ingredient_name.replace(ingredient_prep, "")
			ingredient_name = ingredient_name.replace(ingredient_prep_description, "")
		else:	#if not found check for comma split
			split_name = ingredient_name.split(", ")
			if len(split_name) > 1:
				ingredient_name = split_name[0]
				ingredient_prep = split_name[len(split_name)-1]
				ingredient_prep_description = ""
			else:	#otherwise no description
				ingredient_prep = ""
				ingredient_prep_description = ""
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

		item.ingredient_from_recipie(ingredient_name, ingredient_qty, ingredient_measure, ingredient_prep, ingredient_prep_description)
		ingredient_list.append(item)

	if len(ingredient_list) == 0:
		print("Unable to retreive recipie: Bad URL")

	return ingredient_list


def hc_make_method_list():
	#list generated by consulting chef Gaston Bleu, owner of Le Fancie Restrantue
	methods = ["Grill", "Stir-Fry", "Flambe", "Fry", "Pan-Fry", "Deep Fry", "Saute", "Boil", "Roast", "Bake", "Sear", "Poach", "Simmer", "Broil", "Steam", "Blanch", "Braise", "Stew"]
	return [method.lower() for method in methods]