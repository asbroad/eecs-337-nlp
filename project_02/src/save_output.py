import json

def save_output(recipe_url, ingredients_list, primary_cooking_method, other_cooking_methods, cooking_tools):

    formatted_results = {}

    ingredients = []
    for ingredient in ingredients_list:
        ingredient_dict = {}
        ingredient_dict['name'] = 'temp'
        ingredient_dict['quantity'] = 'temp'
        ingredient_dict['measurement'] = 'temp'
        ingredient_dict['descriptor'] = 'temp'
        ingredient_dict['preparation'] = 'temp'
        ingredient_dict['prep-description'] = 'temp'
        ingredients.append(ingredient_dict)

    formatted_results['ingredients'] = ingredients
    formatted_results['primary cooking method'] = primary_cooking_method
    formatted_results['cooking methods'] = other_cooking_methods
    formatted_results['cooking tools'] = cooking_tools

    split_url = recipe_url.split('/')
    if recipe_url.endswith('/'):
        recipe_title = str(split_url[-2])
    else:
        recipe_title = str(split_url[-1])
    output_filename = "../output/"+recipe_title + '.json'

    with open(output_filename, 'w') as outfile:
        json.dump(formatted_results, outfile)

    print('Finished writing to file : ', output_filename)
