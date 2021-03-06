from ingredient import Ingredient
from recipe import Recipe
from copy import copy
import random
import string

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
        proteins.append(['chicken', [], ['low-fat', 'low-sodium'], ['italian', 'chinese']])
        proteins.append(['duck', [], ['low-sodium'], ['chinese']])
        proteins.append(['beef', [], ['low-fat'], ['italian', 'chinese']])
        proteins.append(['pork', [], [], ['italian', 'chinese']])
        proteins.append(['ham', [], [], ['italian']])
        proteins.append(['sausage', [], [], ['italian']])
        proteins.append(['prosciutto', [], [], ['italian']])
        proteins.append(['halibut', ['pescatarian'], ['low-sodium','low-fat'], ['chinese']])
        proteins.append(['trout', ['pescatarian'], ['low-sodium','low-fat'], ['chinese']])
        proteins.append(['sea bass', ['pescatarian'], ['low-sodium','low-fat'], ['chinese']])
        proteins.append(['salmon', ['pescatarian'], ['low-sodium','low-fat'], ['italian','chinese']])
        proteins.append(['fish', ['pescatarian'], ['low-sodium','low-fat'], ['italian','chinese']])
        proteins.append(['tilapia', ['pescatarian'], ['low-sodium','low-fat'], ['italian']])
        proteins.append(['flounder', ['pescatarian'], ['low-sodium','low-fat'], ['italian']])
        proteins.append(['meat substitute', ['vegetarian'], ['low-sodium','low-fat'], ['italian','chinese']])
        proteins.append(['portobello mushroom', ['vegetarian'], ['low-sodium','low-fat'], ['chinese']])
        return proteins

    def hc_make_vegitable_list(self):
        veggies = []
        veggies.append(['onion', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['italian']])
        veggies.append(['tomato', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['italian']])
        veggies.append(['mushroom', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['italian', 'chinese']])
        veggies.append(['scallion', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['chinese']])
        veggies.append(['bell pepper', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['chinese', "italian"]])
        veggies.append(['red pepper', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['chinese', "italian"]])
        veggies.append(['green pepper', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['chinese', "italian"]])
        veggies.append(['lima beans', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['italian']])
        veggies.append(['celery', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['chinese']])
        veggies.append(['green onion', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['chinese']])
        veggies.append(['artichoke', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['italian']])
        return veggies

    def hc_make_spice_list(self):
        spices = []
        spices.append(['chicken-spice', [], ['low-fat', 'low-sodium'], ['italian', 'chinese']])
        spices.append(['duck-spice', [], ['low-sodium'], ['chinese']])
        spices.append(['beef-spice', [], ['low-fat'], ['italian', 'chinese']])
        spices.append(['pork-spice', [], [], ['italian', 'chinese']])
        spices.append(['basil', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['italian', 'chinese']])
        spices.append(['oregano', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['italian']])
        spices.append(['cilantro', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['italian']])
        spices.append(['crushed red pepper', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['chinese']])
        spices.append(['red pepper flakes', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['chinese']])
        spices.append(['garlic',  ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['italian', 'chinese']])
        spices.append(['ginger',  ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'],  ['chinese']])
        spices.append(['five spice',  ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'],  ['chinese']])
        spices.append(['cinnamon', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['italian']])
        return spices

    def hc_make_sauce_list(self):
        sauces = []
        sauces.append(['soy sauce', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['chinese']])
        sauces.append(['hot sauce', ['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['italian', 'chinese']])
        sauces.append(['tomato sauce',['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'], ['italian']])
        sauces.append(['marinara', ['vegetarian', 'pescatarian'], ['low-sodium'],['italian']])
        sauces.append(['beef broth',[], ['low-fat'], ['italian','chinese']])
        sauces.append(['fish sauce', ['pescatarian'],['low-fat', 'low-sodium'],['italian','chinese']])
        sauces.append(['chicken broth', [], ['low-fat', 'low-sodium'],['italian','chinese']])
        sauces.append(['vegetable broth',['vegetarian', 'pescatarian'], ['low-fat', 'low-sodium'],['italian','chinese']])
        return sauces

    def make_dict(self,ingredients):
        ingredient_dict = {}
        for ingredient in ingredients:
            ingredient_dict[ingredient[0]] = Ingredient(ingredient[0], ingredient[1], ingredient[2], ingredient[3])
        return ingredient_dict

    def find_replacement_itm_cuisine(self,itm,cuisine_name,input_dict):
        all_dict_itms = input_dict.keys()
        if itm not in all_dict_itms:
            return False
        is_cuisine = input_dict[itm].isCuisine(cuisine_name)
        if is_cuisine: # the current ingredient is already in the diet
            return False
        possible_replacements = []
        
        for key in input_dict.keys():
            cur_is_cuisine = input_dict[key].isCuisine(cuisine_name)
            if cur_is_cuisine:
                possible_replacements.append(input_dict[key])
        #print possible_replacements
        if len(possible_replacements) == 0:
            return False
        return possible_replacements[random.randint(0,len(possible_replacements)-1)]


    def find_replacement_itm_healthy(self,itm,health_name,input_dict):
        all_dict_itms = input_dict.keys()
        if itm not in all_dict_itms:
            return False
        is_healthy = input_dict[itm].isHealthy(health_name)
        if is_healthy: # the current ingredient is already in the diet
            return False
        possible_replacements = []
        for key in input_dict.keys():
            cur_is_healthy = input_dict[key].isHealthy(health_name)
            if cur_is_healthy:
                possible_replacements.append(input_dict[key])
        if len(possible_replacements) == 0:
            #print('No replacement ingredients')
            return False
        return possible_replacements[random.randint(0,len(possible_replacements)-1)]


    def find_replacement_diet(self,itm,diet_name,input_dict):
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
            #print('No replacement ingredients')
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
                    if new_itm:
                        new_directions = self.replace_directions(itm, new_itm.name, transformed_recipe.directions)
                        transformed_recipe.directions = new_directions
            if not new_itm:
                for itm in self.protein_dict.keys():
                    if itm in ingredient.name or not new_itm:
                        new_itm = self.find_replacement_itm_cuisine(ingredient.name.lower(),cuisine_name,self.protein_dict)
                        if new_itm:
                            new_directions = self.replace_directions(itm, new_itm.name, transformed_recipe.directions)
                            transformed_recipe.directions = new_directions
            if not new_itm:
                for itm in self.veggie_dict.keys():
                    if itm in ingredient.name or not new_itm:
                        new_itm = self.find_replacement_itm_cuisine(ingredient.name.lower(),cuisine_name,self.veggie_dict)
                        if new_itm:
                            new_directions = self.replace_directions(itm, new_itm.name, transformed_recipe.directions)
                            transformed_recipe.directions = new_directions
            if not new_itm:
                for itm in self.spice_dict.keys():
                    if itm in ingredient.name or not new_itm:
                        new_itm = self.find_replacement_itm_cuisine(ingredient.name.lower(),cuisine_name,self.spice_dict)
                        if new_itm:
                            new_directions = self.replace_directions(itm, new_itm.name, transformed_recipe.directions)
                            transformed_recipe.directions = new_directions

            if new_itm:
                print("Replace {} with {}".format(ingredient.name, new_itm.name))
                new_itm.qty = ingredient.qty
                new_itm.measure = ingredient.measure
                new_itm.prep_description = ingredient.prep_description
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
                    if new_itm:
                        new_directions = self.replace_directions(itm, new_itm.name, transformed_recipe.directions)
                        transformed_recipe.directions = new_directions
            if not new_itm:
                for itm in self.protein_dict.keys():
                    if itm in ingredient.name or not new_itm:
                        new_itm = self.find_replacement_itm_healthy(ingredient.name.lower(),health_name,self.protein_dict)
                        if new_itm:
                            new_directions = self.replace_directions(itm, new_itm.name, transformed_recipe.directions)
                            transformed_recipe.directions = new_directions
            if not new_itm:
                for itm in self.veggie_dict.keys():
                    if itm in ingredient.name or not new_itm:
                        new_itm = self.find_replacement_itm_healthy(ingredient.name.lower(),health_name,self.veggie_dict)
                        if new_itm:
                            new_directions = self.replace_directions(itm, new_itm.name, transformed_recipe.directions)
                            transformed_recipe.directions = new_directions
            if not new_itm:
                for itm in self.spice_dict.keys():
                    if itm in ingredient.name or not new_itm:
                        new_itm = self.find_replacement_itm_healthy(ingredient.name.lower(),health_name,self.spice_dict)
                        if new_itm:
                            new_directions = self.replace_directions(itm, new_itm.name, transformed_recipe.directions)
                            transformed_recipe.directions = new_directions

            if new_itm:
                print("Replace {} with {}".format(ingredient.name, new_itm.name))
                new_itm.prep_description = ingredient.prep_description
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
                    if new_itm:
                        new_directions = self.replace_directions(itm, new_itm.name, transformed_recipe.directions)
                        transformed_recipe.directions = new_directions
            if not new_itm:
                for itm in self.protein_dict.keys():
                    if itm in ingredient.name.lower() and not new_itm:
                        new_itm = self.find_replacement_diet(itm, diet_name, self.protein_dict)
                        if new_itm:
                            new_directions = self.replace_directions(itm, new_itm.name, transformed_recipe.directions)
                            transformed_recipe.directions = new_directions
            if not new_itm:
                for itm in self.veggie_dict.keys():
                    if itm in ingredient.name.lower() and not new_itm:
                        new_itm = self.find_replacement_diet(itm, diet_name, self.veggie_dict)
                        if new_itm:
                            new_directions = self.replace_directions(itm, new_itm.name, transformed_recipe.directions)
                            transformed_recipe.directions = new_directions
            if not new_itm:
                for itm in self.spice_dict.keys():
                    if itm in ingredient.name.lower() and not new_itm:
                        new_itm = self.find_replacement_diet(itm, diet_name, self.spice_dict)
                        if new_itm:
                            new_directions = self.replace_directions(itm, new_itm.name, transformed_recipe.directions)
                            transformed_recipe.directions = new_directions

            if new_itm:
                print("Replace {} with {}".format(ingredient.name, new_itm.name))
                new_itm.qty = ingredient.qty
                new_itm.measure = ingredient.measure
                new_itm.prep = ingredient.prep
                new_itm.prep_description = ingredient.prep_description
            else:
                new_itm = ingredient

            transformed_recipe.ingredients.append(new_itm)

        return transformed_recipe


    def replace_directions(self, old_itm, new_itm, directions):
        new_directions = []
        for d in directions:
            if old_itm in d:
                d_new = string.replace(d, old_itm, new_itm)
                new_directions.append(d_new)
            else:
                new_directions.append(d)

        return new_directions

    def transform_other(self,other_name, recipe):
        return recipe



if __name__ == "__main__":

    kb = KnowledgeBase()
