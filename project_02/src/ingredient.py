

class Ingredient:
    def ingredient_from_recipie(self, name, qty, measure, prep):
        self.name = name
        self.qty = qty
        self.measure = measure
        self.prep = prep




    def __init__(self, name='', vegetarian=False, fish=False, dairy=False, healthy=None, associated_cuisine=[], prep=''):
        self.name = name
        self.prep = prep
        self.vegetarian = vegetarian
        self.fish = fish
        self.dairy = dairy
        self.healthy = healthy
        self.associated_cuisine = associated_cuisine
        self.qty = 0
        self.measure = ""


    def __str__(self):
        return str(self.name + '\nVegetarian? ' + str(self.vegetarian) + '\nFish? ' + str(self.fish) + '\nDairy? ' +
        str(self.dairy)  + '\nHealthy? ' + str(self.healthy) + '\nAssociated Cuisine(s) : ' +
        str(self.associated_cuisine) + '\nAssociated Prep : ' + self.prep)
