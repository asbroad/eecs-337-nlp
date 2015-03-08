from ingredient import Ingredient
from recipe import Recipe
from copy import copy
import random

# Ingredient parameters
# (name, vegitarian, fish, dairy, healthy, associated_cuisine, associated_prep)

class KnowledgeBase:

    def __init__(self):
        self.protein_dict = self.make_dict(self.hc_make_protein_list())
        self.veggie_dict = self.make_dict(self.hc_make_vegitable_list())
        self.spice_dict = self.make_dict(self.hc_make_spice_list())
        self.sauce_dict = self.make_dict(self.hc_make_sauce_list())

    def hc_make_protein_list(self):
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
        proteins.append(['portobello mushroom', True, False, False, True, ['Italian','Chinese'], 'cubed'])
        return proteins

    def hc_make_vegitable_list(self):
        veggies = []
        veggies.append(['onion', True, False, False, True, ['Italian', 'Chinese'], 'sliced'])
        veggies.append(['tomato', True, False, False, True, ['Italian'], 'sliced'])
        veggies.append(['mushroom', True, False, False, True, ['Italian', 'Chinese'], 'sliced'])
        veggies.append(['scallion', True, False, False, True, ['Chinese'], 'sliced'])
        return veggies

    def hc_make_spice_list(self):
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

    def hc_make_sauce_list(self):
        sauces = []
        sauces.append(['soy sauce', True, False, False, False, ['Chinese'], ''])
        sauces.append(['tomato sauce', True, False, False, True, ['Italian'], ''])
        sauces.append(['marinara', True, False, False, True, ['Italian'], ''])
        sauces.append(['beef broth', False, False, False, False, ['Italian','Chinese'], ''])
        sauces.append(['chicken broth', False, False, False, False, ['Italian','Chinese'], ''])
        sauces.append(['vegetable broth', True, False, False, True, ['Italian','Chinese'], ''])
        return sauces

    def make_dict(self,ingredients):
        ingredient_dict = {}
        for ingredient in ingredients:
            ingredient_dict[ingredient[0]] = Ingredient(ingredient[0], ingredient[1], ingredient[2], ingredient[3], ingredient[4], ingredient[5], ingredient[6] )
        return ingredient_dict

    def find_replacement_itm_cuisine(self,itm,cuisine,input_dict):
        all_dict_itms = input_dict.keys()
        if itm not in all_dict_itms:
            return False
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
            return False
        return possible_replacements[random.randint(0,len(possible_replacements)-1)]

    def find_replacement_fish(self,itm,input_dict):
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

    def find_replacement_vegetarian(self,itm,input_dict):
        all_dict_itms = input_dict.keys()
        if itm not in all_dict_itms:
            print(itm, 'not in dictionary')
            return itm
        is_fish = input_dict[itm].vegetarian
        if is_fish: # the current ingredient is already vegetarian
            return itm
        possible_replacements = []
        for key in input_dict.keys():
            cur_is_fish = input_dict[key].vegetarian
            if cur_is_fish:
                possible_replacements.append(input_dict[key])
        if len(possible_replacements) == 0:
            print('No replacement ingredients, no vegetarian')
            return itm
        return possible_replacements[random.randint(0,len(possible_replacements)-1)]


    def find_replacement_healthy(self,itm,input_dict):
        all_dict_itms = input_dict.keys()
        if itm not in all_dict_itms:
            print(itm, 'not in dictionary')
            return itm
        is_fish = input_dict[itm].healthy
        if is_fish: # the current ingredient is already healthy
            return itm
        possible_replacements = []
        for key in input_dict.keys():
            cur_is_fish = input_dict[key].healthy
            if cur_is_fish:
                possible_replacements.append(input_dict[key])
        if len(possible_replacements) == 0:
            print('No replacement ingredients, no healthy')
            return itm
        return possible_replacements[random.randint(0,len(possible_replacements)-1)]

    def transform_cuisine(self,cuisine_name,recipe):
        transformed_recipe = copy(recipe)
        transformed_recipe.ingredients = []
        for ingredient in recipe.ingredients:
            new_itm = False
            if itm in self.sauce_dict:
                new_itm = find_replacement_itm_cuisine(ingredient.name.lower(),cuisine_name,self.sauce_dict)
            elif itm in self.protein_dict:
                new_itm = find_replacement_itm_cuisine(ingredient.name.lower(),cuisine_name,self.sauce_dict)
            elif itm in self.veggie_dict:
                new_itm = find_replacement_itm_cuisine(ingredient.name.lower(),cuisine_name,self.sauce_dict)
            elif itm in self.spice_dict:
                new_itm = find_replacement_itm_cuisine(ingredient.name.lower(),cuisine_name,self.sauce_dict)

            if new_itm:
                new_itm.qty = ingredient.qty
                new_itm.measure = ingredient.measure
                new_itm.prep = ingredient.prep
            else:
                new_itm = ingredient

            transformed_recipe.ingredients.append(new_itm)

        return transformed_recipe

    def transform_diet(self,diet_name, recipe):
        return recipe

    def transform_other(self,other_name, recipe):
        return recipe

if __name__ == "__main__":

    kb = KnowledgeBase()
    rep_cuisine = kb.find_replacement_itm_cuisine('oregano', 'Chinese', kb.spice_dict)
    rep_fish = kb.find_replacement_fish('chicken', kb.protein_dict)
    rep_vegetarian = kb.find_replacement_vegetarian('chicken', kb.protein_dict)
    rep_healthy = kb.find_replacement_healthy('beef', kb.protein_dict)
    print(rep_cuisine)
    print(rep_fish)
    print(rep_vegetarian)
    print(rep_healthy)
