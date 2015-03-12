import json

def save_output(recipe_url, recipe):

    formatted_results = {}

    ingredients = []
    for ingredient in recipe.ingredients:
        ingredient_dict = {}
        ingredient_dict['name'] = ingredient.name
        ingredient_dict['quantity'] = ingredient.qty
        ingredient_dict['measurement'] = ingredient.measure
        ingredient_dict['descriptor'] = ingredient.description
        ingredient_dict['preparation'] = ingredient.prep
        ingredient_dict['prep-description'] = ingredient.prep_description
        ingredients.append(ingredient_dict)

    formatted_results['ingredients'] = ingredients
    formatted_results['primary cooking method'] = recipe.main_method[0]
    formatted_results['cooking methods'] = [itm[0] for itm in recipe.other_methods]
    formatted_results['cooking tools'] = [tool.name for tool in recipe.tools]

    split_url = recipe_url.split('/')
    if recipe_url.endswith('/'):
        recipe_title = str(split_url[-2])
    else:
        recipe_title = str(split_url[-1])
    output_filename = "../output/"+recipe_title + '.json'

    with open(output_filename, 'w') as outfile:
        json.dump(formatted_results, outfile)

    print('Finished writing to file : ', output_filename)
