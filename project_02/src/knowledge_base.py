from ingredient import Ingredient
import random

# Ingredient parameters
# (name, vegitarian, fish, dairy, healthy, associated_cuisine, associated_prep)

def hc_make_protein_list():
    proteins = []
    proteins.append(['chicken', False, False, False, True, ['Italian', 'Chinese'], 'sliced'])
    proteins.append(['beef', False, False, False, False, ['Italian', 'Chinese'], 'sliced'])
    proteins.append(['halibut', False, True, False, True, ['Chinese'], 'scaled'])
    proteins.append(['trout', False, True, False, True, ['Chinese'], 'scaled'])
    proteins.append(['sea bass', False, True, False, True, ['Chinese'], 'scaled'])
    proteins.append(['salmon', False, True, False, True, ['Italian','Chinese'], 'scaled'])
    proteins.append(['tilapia', False, True, False, True, ['Italian'], 'scaled'])
    proteins.append(['flounder', False, True, False, True, ['Italian'], 'scaled'])
    proteins.append(['tofu', True, False, False, True, ['Chinese'], 'cubed'])
    return proteins

def hc_make_vegitable_list():
    veggies = []
    veggies.append(['onion', True, False, False, True, ['Italian', 'Chinese'], 'sliced'])
    veggies.append(['tomato', True, False, False, True, ['Italian'], 'sliced'])
    veggies.append(['mushroom', True, False, False, True, ['Italian', 'Chinese'], 'sliced'])
    veggies.append(['scallion', True, False, False, True, ['Chinese'], 'sliced'])
    return veggies

def hc_make_spice_list():
    spices = []
    spices.append(['pepper', True, False, False, True, ['Italian', 'Chinese'], 'ground'])
    spices.append(['salt', True, False, False, True, ['Italian', 'Chinese'], 'ground'])
    spices.append(['basil', True, False, False, True, ['Italian', 'Chinese'], 'sliced'])
    spices.append(['oregano', True, False, False, True, ['Italian'], 'crushed'])
    spices.append(['cilantro', True, False, False, True, ['Italian'], 'crushed'])
    spices.append(['red pepper', True, False, False, True, ['Italian', 'Chinese'], 'crushed'])
    spices.append(['garlic', True, False, False, True, ['Italian', 'Chinese'], 'diced'])
    spices.append(['ginger', True, False, False, True, ['Chinese'], 'diced'])
    spices.append(['five spice', True, False, False, True, ['Chinese'], 'ground'])
    return spices

def hc_make_sauce_list():
    sauces = []
    sauces.append(['soy sauce', True, False, False, False, ['Chinese'], ''])
    sauces.append(['tomato sauce', True, False, False, True, ['Italian'], ''])
    sauces.append(['marinara', True, False, False, True, ['Italian'], ''])
    return sauces

def make_dict(ingredients):
    ingredient_dict = {}
    for ingredient in ingredients:
        ingredient_dict[ingredient[0]] = Ingredient(ingredient[0], ingredient[1], ingredient[2], ingredient[3], ingredient[4], ingredient[5], ingredient[6] )
    return ingredient_dict

def find_replacement_itm_cuisine(itm,cuisine,input_dict):
    all_dict_itms = input_dict.keys()
    if itm not in all_dict_itms:
        print(itm, 'not in dictionary')
        return itm
    associated_cuisines = input_dict[itm].associated_cuisine
    if cuisine in associated_cuisines: # the current ingredient is already associated with the desired cuisine
        return itm
    possible_replacements = []
    for key in input_dict.keys():
        cur_associated_cuisines = input_dict[key].associated_cuisine
        if cuisine in cur_associated_cuisines:
            possible_replacements.append(input_dict[key])
    if len(possible_replacements) == 0:
        print('No replacement ingredients, no ingredients associated with : ' + cuisine)
        return itm
    return possible_replacements[random.randint(0,len(possible_replacements)-1)]

# (name, vegitarian, fish, dairy, healthy, associated_cuisine, associated_prep)

def find_replacement_fish(itm,input_dict):
    all_dict_itms = input_dict.keys()
    if itm not in all_dict_itms:
        print(itm, 'not in dictionary')
        return itm
    is_fish = input_dict[itm].fish
    if is_fish: # the current ingredient is already fish
        return itm
    possible_replacements = []
    for key in input_dict.keys():
        cur_is_fish = input_dict[key].fish
        if cur_is_fish:
            possible_replacements.append(input_dict[key])
    if len(possible_replacements) == 0:
        print('No replacement ingredients, no fish')
        return itm
    return possible_replacements[random.randint(0,len(possible_replacements)-1)]


if __name__ == "__main__":
    protein_dict = make_dict(hc_make_protein_list())
    veggie_dict = make_dict(hc_make_vegitable_list())
    spice_dict = make_dict(hc_make_spice_list())
    sauce_dict = make_dict(hc_make_sauce_list())
    rep_cuisine = find_replacement_itm_cuisine('oregano', 'Chinese', spice_dict)
    rep_fish = find_replacement_fish('chicken', protein_dict)
    print(rep_cuisine)
    print(rep_fish)
