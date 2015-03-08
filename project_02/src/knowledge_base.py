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
        proteins.append(['chicken', False, False, False, True, ['italian', 'chinese'], 'sliced'])
        proteins.append(['duck', False, False, False, False, ['chinese'], 'sliced'])
        proteins.append(['beef', False, False, False, False, ['italian', 'chinese'], 'sliced'])
        proteins.append(['pork', False, False, False, False, ['italian', 'chinese'], 'sliced'])
        proteins.append(['ham', False, False, False, False, ['italian'], 'sliced'])
        proteins.append(['sausage', False, False, False, False, ['italian'], 'sliced'])
        proteins.append(['prosciutto', False, False, False, False, ['italian'], 'sliced'])
        proteins.append(['halibut', False, True, False, True, ['chinese'], 'scaled'])
        proteins.append(['trout', False, True, False, True, ['chinese'], 'scaled'])
        proteins.append(['sea bass', False, True, False, True, ['chinese'], 'scaled'])
        proteins.append(['salmon', False, True, False, True, ['italian','chinese'], 'scaled'])
        proteins.append(['fish', False, True, False, True, ['italian','chinese'], 'scaled'])
        proteins.append(['tilapia', False, True, False, True, ['italian'], 'scaled'])
        proteins.append(['flounder', False, True, False, True, ['italian'], 'scaled'])
        proteins.append(['tofu', True, False, False, True, ['chinese'], 'cubed'])
        proteins.append(['meat substitute', True, False, False, True, ['chinese', 'italian'], 'extruded'])
        proteins.append(['portobello mushroom', True, False, False, True, ['italian','chinese'], 'cubed'])
        return proteins

    def hc_make_vegitable_list(self):
        veggies = []
        veggies.append(['onion', True, False, False, True, ['italian', 'chinese'], 'sliced'])
        veggies.append(['tomato', True, False, False, True, ['italian'], 'sliced'])
        veggies.append(['mushroom', True, False, False, True, ['italian', 'chinese'], 'sliced'])
        veggies.append(['scallion', True, False, False, True, ['chinese'], 'sliced'])
        veggies.append(['bell pepper', True, False, False, True, ['chinese', "italian"], 'sliced'])
        veggies.append(['red pepper', True, False, False, True, ['chinese', "italian"], 'sliced'])
        veggies.append(['green pepper', True, False, False, True, ['chinese', "italian"], 'sliced'])
        veggies.append(['lima beans', True, False, False, True, ['italian'], 'sliced'])
        veggies.append(['celery', True, False, False, True, ['chinese'], 'sliced'])
        veggies.append(['green onion', True, False, False, True, ['chinese'], 'sliced'])
        veggies.append(['artichoke', True, False, False, True, ['italian'], 'crushed'])
        return veggies

    def hc_make_spice_list(self):
        spices = []
        spices.append(['basil', True, False, False, True, ['italian', 'chinese'], 'sliced'])
        spices.append(['oregano', True, False, False, True, ['italian'], 'crushed'])
        spices.append(['cilantro', True, False, False, True, ['italian'], 'crushed'])
        spices.append(['crushed red pepper', True, False, False, True, ['chinese'], 'crushed'])
        spices.append(['red pepper flakes', True, False, False, True, ['chinese'], 'crushed'])
        spices.append(['garlic', True, False, False, True, ['italian', 'chinese'], 'diced'])
        spices.append(['ginger', True, False, False, True, ['chinese'], 'diced'])
        spices.append(['five spice', True, False, False, True, ['chinese'], 'ground'])
        return spices

    def hc_make_sauce_list(self):
        sauces = []
        sauces.append(['soy sauce', True, False, False, False, ['chinese'], ''])
        sauces.append(['hot sauce', True, False, False, False, ['chinese'], ''])
        sauces.append(['tomato sauce', True, False, False, True, ['italian'], ''])
        sauces.append(['marinara', True, False, False, True, ['italian'], ''])
        sauces.append(['beef broth', False, False, False, False, ['italian','chinese'], ''])
        sauces.append(['fish sauce', False, True, False, True, ['italian','chinese'], ''])
        sauces.append(['chicken broth', False, False, False, False, ['italian','chinese'], ''])
        sauces.append(['vegetable broth', True, False, False, True, ['italian','chinese'], ''])
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
            return False
        possible_replacements = []
        for key in input_dict.keys():
            cur_associated_cuisines = input_dict[key].associated_cuisine
            if cuisine in cur_associated_cuisines:
                possible_replacements.append(input_dict[key])
        if len(possible_replacements) == 0:
            print('No replacement ingredients, no ingredients associated with : ' + cuisine)
            return False
        return possible_replacements[random.randint(0,len(possible_replacements)-1)]


    def find_replacement_diet(self,itm,diet_name,input_dict):
        if(diet_name == "vegetarian"):
            all_dict_itms = input_dict.keys()
            if itm not in all_dict_itms:
                return False
            is_veg = input_dict[itm].vegetarian
            if is_veg: # the current ingredient is already vegetarian
                return False
            possible_replacements = []
            for key in input_dict.keys():
                cur_is_veg = input_dict[key].vegetarian
                if cur_is_veg:
                    possible_replacements.append(input_dict[key])
            if len(possible_replacements) == 0:
                print('No replacement ingredients, no vegetarian')
                return False
            return possible_replacements[random.randint(0,len(possible_replacements)-1)]

        elif(diet_name == "pescetarian"):
            all_dict_itms = input_dict.keys()
            if itm not in all_dict_itms:
                return False
            is_fish = input_dict[itm].fish
            if is_fish: # the current ingredient is already vegetarian
                return False
            possible_replacements = []
            for key in input_dict.keys():
                cur_is_fish = input_dict[key].fish
                if cur_is_fish:
                    possible_replacements.append(input_dict[key])
            if len(possible_replacements) == 0:
                print('No replacement ingredients, no fish')
                return False
            return possible_replacements[random.randint(0,len(possible_replacements)-1)]

        elif(diet_name == "healthy"):
            all_dict_itms = input_dict.keys()
            if itm not in all_dict_itms:
                return False
            is_healthy = input_dict[itm].healthy
            if is_healthy: # the current ingredient is already vegetarian
                return False
            possible_replacements = []
            for key in input_dict.keys():
                cur_is_healthy = input_dict[key].healthy
                if cur_is_healthy:
                    possible_replacements.append(input_dict[key])
            if len(possible_replacements) == 0:
                print('No replacement ingredients, no healthy')
                return False
            return possible_replacements[random.randint(0,len(possible_replacements)-1)]
        else:
            print("Invalid Diet")
            return False

    def transform_cuisine(self,cuisine_name,recipe):
        transformed_recipe = copy(recipe)
        transformed_recipe.ingredients = []
        for ingredient in recipe.ingredients:
            new_itm = False
            for itm in self.sauce_dict.keys():
                if itm in ingredient.name or not new_itm:
                    new_itm = self.find_replacement_itm_cuisine(ingredient.name.lower(),cuisine_name,self.sauce_dict)
            if not new_itm:
                for itm in self.protein_dict.keys():
                    if itm in ingredient.name or not new_itm:
                        new_itm = self.find_replacement_itm_cuisine(ingredient.name.lower(),cuisine_name,self.protein_dict)
            if not new_itm:
                for itm in self.veggie_dict.keys():
                    if itm in ingredient.name or not new_itm:
                        new_itm = self.find_replacement_itm_cuisine(ingredient.name.lower(),cuisine_name,self.veggie_dict)
            if not new_itm:
                for itm in self.spice_dict.keys():
                    if itm in ingredient.name or not new_itm:
                        new_itm = self.find_replacement_itm_cuisine(ingredient.name.lower(),cuisine_name,self.spice_dict)

            if new_itm:
                #print(ingredient.name)
                #print("Trans")
                #print(new_itm.name)
                new_itm.qty = ingredient.qty
                new_itm.measure = ingredient.measure
                new_itm.prep = ingredient.prep
            else:
                new_itm = ingredient

            transformed_recipe.ingredients.append(new_itm)

        return transformed_recipe

    def transform_diet(self,diet_name, recipe):
        transformed_recipe = copy(recipe)
        transformed_recipe.ingredients = []
        for ingredient in recipe.ingredients:
            new_itm = False
            for itm in self.sauce_dict.keys():
                if itm in ingredient.name.lower() and not new_itm:
                    new_itm = self.find_replacement_diet(itm, diet_name, self.sauce_dict)
            if not new_itm:
                for itm in self.protein_dict.keys():
                    if itm in ingredient.name.lower() and not new_itm:
                        new_itm = self.find_replacement_diet(itm, diet_name, self.protein_dict)
            if not new_itm:
                for itm in self.veggie_dict.keys():
                    if itm in ingredient.name.lower() and not new_itm:
                        new_itm = self.find_replacement_diet(itm, diet_name, self.veggie_dict)
            if not new_itm:
                for itm in self.spice_dict.keys():
                    if itm in ingredient.name.lower() and not new_itm:
                        new_itm = self.find_replacement_diet(itm, diet_name, self.spice_dict)

            if new_itm:
                print(ingredient.name)
                print("Trans")
                print(new_itm.name)
                new_itm.qty = ingredient.qty
                new_itm.measure = ingredient.measure
                new_itm.prep = ingredient.prep
            else:
                new_itm = ingredient

            transformed_recipe.ingredients.append(new_itm)

        return transformed_recipe









    def transform_other(self,other_name, recipe):
        return recipe

if __name__ == "__main__":

    kb = KnowledgeBase()
    rep_cuisine = kb.find_replacement_itm_cuisine('oregano', 'chinese', kb.spice_dict)
    rep_fish = kb.find_replacement_fish('chicken', kb.protein_dict)
    rep_vegetarian = kb.find_replacement_vegetarian('chicken', kb.protein_dict)
    rep_healthy = kb.find_replacement_healthy('beef', kb.protein_dict)
    print(rep_cuisine)
    print(rep_fish)
    print(rep_vegetarian)
    print(rep_healthy)
