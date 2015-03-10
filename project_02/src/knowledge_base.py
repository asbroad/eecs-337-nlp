from ingredient import Ingredient
from recipe import Recipe
from copy import copy
import random

# Ingredient parameters
# (name, [diet], [healty], [cuisine])

class KnowledgeBase:

    def __init__(self):
        self.protein_dict = self.make_dict(self.hc_make_protein_list())
        self.veggie_dict = self.make_dict(self.hc_make_vegitable_list())
        self.spice_dict = self.make_dict(self.hc_make_spice_list())
        self.sauce_dict = self.make_dict(self.hc_make_sauce_list())

    def hc_make_protein_list(self):
        proteins = []
        #(['fake meat', ['fish', 'veg'], ['low-carb', 'low-fun'], ['fake', 'italian']])
        proteins.append(['chicken', [], ['low-fat', 'low-sodium'], ['italian', 'chinese']])
        proteins.append(['duck', [], ['low-sodium'], ['chinese']])
        proteins.append(['beef', [], ['low-fat'], ['italian', 'chinese']])
        proteins.append(['pork', [], [], ['italian', 'chinese']])
        proteins.append(['tofu', ['vegetarian'], ['low-sodium'], ['chinese']])
        #proteins.append(['ham', False, False, False, False, ['italian'], 'sliced'])
        #proteins.append(['sausage', False, False, False, False, ['italian'], 'sliced'])
        #proteins.append(['prosciutto', False, False, False, False, ['italian'], 'sliced'])
        #proteins.append(['halibut', False, True, False, True, ['chinese'], 'scaled'])
        #proteins.append(['trout', False, True, False, True, ['chinese'], 'scaled'])
        #proteins.append(['sea bass', False, True, False, True, ['chinese'], 'scaled'])
        #proteins.append(['salmon', False, True, False, True, ['italian','chinese'], 'scaled'])
        #proteins.append(['fish', False, True, False, True, ['italian','chinese'], 'scaled'])
        #proteins.append(['tilapia', False, True, False, True, ['italian'], 'scaled'])
        #proteins.append(['flounder', False, True, False, True, ['italian'], 'scaled'])
        #proteins.append(['tofu', True, False, False, True, ['chinese'], 'cubed'])
        #proteins.append(['meat substitute', True, False, False, True, ['chinese', 'italian'], 'extruded'])
        #proteins.append(['portobello mushroom', True, False, False, True, ['italian','chinese'], 'cubed'])
        return proteins

    def hc_make_vegitable_list(self):
        veggies = []
        veggies.append(['chicken-veg', [], ['low-fat', 'low-sodium'], ['italian', 'chinese']])
        veggies.append(['duck-veg', [], ['low-sodium'], ['chinese']])
        veggies.append(['beef-veg', [], ['low-fat'], ['italian', 'chinese']])
        veggies.append(['pork-veg', [], [], ['italian', 'chinese']])
        #veggies.append(['onion', True, False, False, True, ['italian', 'chinese'], 'sliced'])
        #veggies.append(['tomato', True, False, False, True, ['italian'], 'sliced'])
        #veggies.append(['mushroom', True, False, False, True, ['italian', 'chinese'], 'sliced'])
        #veggies.append(['scallion', True, False, False, True, ['chinese'], 'sliced'])
        #veggies.append(['bell pepper', True, False, False, True, ['chinese', "italian"], 'sliced'])
        #veggies.append(['red pepper', True, False, False, True, ['chinese', "italian"], 'sliced'])
        #veggies.append(['green pepper', True, False, False, True, ['chinese', "italian"], 'sliced'])
        #veggies.append(['lima beans', True, False, False, True, ['italian'], 'sliced'])
        #veggies.append(['celery', True, False, False, True, ['chinese'], 'sliced'])
        #veggies.append(['green onion', True, False, False, True, ['chinese'], 'sliced'])
        #veggies.append(['artichoke', True, False, False, True, ['italian'], 'crushed'])
        return veggies

    def hc_make_spice_list(self):
        spices = []
        spices.append(['chicken-spice', [], ['low-fat', 'low-sodium'], ['italian', 'chinese']])
        spices.append(['duck-spice', [], ['low-sodium'], ['chinese']])
        spices.append(['beef-spice', [], ['low-fat'], ['italian', 'chinese']])
        spices.append(['pork-spice', [], [], ['italian', 'chinese']])
        #spices.append(['basil', True, False, False, True, ['italian', 'chinese'], 'sliced'])
        #spices.append(['oregano', True, False, False, True, ['italian'], 'crushed'])
        #spices.append(['cilantro', True, False, False, True, ['italian'], 'crushed'])
        #spices.append(['crushed red pepper', True, False, False, True, ['chinese'], 'crushed'])
        #spices.append(['red pepper flakes', True, False, False, True, ['chinese'], 'crushed'])
        #spices.append(['garlic', True, False, False, True, ['italian', 'chinese'], 'diced'])
        #spices.append(['ginger', True, False, False, True, ['chinese'], 'diced'])
        #spices.append(['five spice', True, False, False, True, ['chinese'], 'ground'])
        return spices

    def hc_make_sauce_list(self):
        sauces = []
        sauces.append(['chicken-sauce', [], ['low-fat', 'low-sodium'], ['italian', 'chinese']])
        sauces.append(['duck-sauce', [], ['low-sodium'], ['chinese']])
        sauces.append(['beef-sauce', [], ['low-fat'], ['italian', 'chinese']])
        sauces.append(['pork-sauce', [], [], ['italian', 'chinese']])
        #sauces.append(['soy sauce', True, False, False, False, ['chinese'], ''])
        #sauces.append(['hot sauce', True, False, False, False, ['chinese'], ''])
        #sauces.append(['tomato sauce', True, False, False, True, ['italian'], ''])
        #sauces.append(['marinara', True, False, False, True, ['italian'], ''])
        #sauces.append(['beef broth', False, False, False, False, ['italian','chinese'], ''])
        #sauces.append(['fish sauce', False, True, False, True, ['italian','chinese'], ''])
        #sauces.append(['chicken broth', False, False, False, False, ['italian','chinese'], ''])
        #sauces.append(['vegetable broth', True, False, False, True, ['italian','chinese'], ''])
        return sauces

    def make_dict(self,ingredients):
        ingredient_dict = {}
        for ingredient in ingredients:
            ingredient_dict[ingredient[0]] = Ingredient(ingredient[0], ingredient[1], ingredient[2], ingredient[3])
        return ingredient_dict

    def find_replacement_itm_cuisine(self,itm,cuisine_name,input_dict):
#        if(diet_name == "vegetarian"):
        all_dict_itms = input_dict.keys()
        if itm not in all_dict_itms:
            return False
        is_cuisine = input_dict[itm].isCuisine(cuisine_name)
        if is_cuisine: # the current ingredient is already in the diet
            return False
        possible_replacements = []
        for key in input_dict.keys():
            cur_is_cuisine = input_dict[key].isDiet(cuisine_name)
            if cur_is_cuisine:
                possible_replacements.append(input_dict[key])
        if len(possible_replacements) == 0:
            print('No replacement ingredients')
            return False
        return possible_replacements[random.randint(0,len(possible_replacements)-1)]


    def find_replacement_itm_healthy(self,itm,health_name,input_dict):
#        if(diet_name == "vegetarian"):
        all_dict_itms = input_dict.keys()
        if itm not in all_dict_itms:
            return False
        is_healthy = input_dict[itm].isHealthy(cuisine_name)
        if is_healthy: # the current ingredient is already in the diet
            return False
        possible_replacements = []
        for key in input_dict.keys():
            cur_is_healthy = input_dict[key].isHealthy(cuisine_name)
            if cur_is_healthy:
                possible_replacements.append(input_dict[key])
        if len(possible_replacements) == 0:
            print('No replacement ingredients')
            return False
        return possible_replacements[random.randint(0,len(possible_replacements)-1)]


    def find_replacement_diet(self,itm,diet_name,input_dict):
#        if(diet_name == "vegetarian"):
        all_dict_itms = input_dict.keys()
        if itm not in all_dict_itms:
            return False
        is_diet = input_dict[itm].isDiet(diet_name)
        if is_diet: # the current ingredient is already in the diet
            return False
        possible_replacements = []
        for key in input_dict.keys():
            cur_is_diet = input_dict[key].isDiet(diet_name)
            if cur_is_diet:
                possible_replacements.append(input_dict[key])
        if len(possible_replacements) == 0:
            print('No replacement ingredients')
            return False
        return possible_replacements[random.randint(0,len(possible_replacements)-1)]


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



    def transform_healthy(self,health_name,recipe):
        transformed_recipe = copy(recipe)
        transformed_recipe.ingredients = []
        for ingredient in recipe.ingredients:
            new_itm = False
            for itm in self.sauce_dict.keys():
                if itm in ingredient.name or not new_itm:
                    new_itm = self.find_replacement_itm_healthy(ingredient.name.lower(),health_name,self.sauce_dict)
            if not new_itm:
                for itm in self.protein_dict.keys():
                    if itm in ingredient.name or not new_itm:
                        new_itm = self.find_replacement_itm_healthy(ingredient.name.lower(),health_name,self.protein_dict)
            if not new_itm:
                for itm in self.veggie_dict.keys():
                    if itm in ingredient.name or not new_itm:
                        new_itm = self.find_replacement_itm_healthy(ingredient.name.lower(),health_name,self.veggie_dict)
            if not new_itm:
                for itm in self.spice_dict.keys():
                    if itm in ingredient.name or not new_itm:
                        new_itm = self.find_replacement_itm_healthy(ingredient.name.lower(),health_name,self.spice_dict)

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
